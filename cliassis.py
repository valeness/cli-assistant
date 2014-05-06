#import necessary modules
import urllib
import json as m_json
import os
import webbrowser
#from twisted.internet import reactor
#from twisted.internet import protocol

#commented out for later implementation

##class MyProcessProtocol(protocol.ProcessProtocol):
#	def __init_(self, text):
#		self.text = text
		
#	def connectionMade(self):
#		self.transport.write(self.text)
#		self.transport.closeStdin()
		
	

#define the start function to set directry and commands
def start():
	
	#start setting variables for command precursor
	print """
	-----------------------------------------------------------------
	Here we will set some variables that will allow you to 
	customize your commands. All commands follow this procedure 
	"[command] [string/query]". End all directories with a backslash or
	else it will not work. Please refer to the readme for more.
	-----------------------------------------------------------------
	"""
	
	print "-----------------------------------------"
	print "First, set your program shortcuts directory. Remember the Backslash"
	print "-----------------------------------------"
	directory = raw_input("Directory:")
	
	print "-----------------------------------------"
	print "Google Command"
	print "-----------------------------------------"
	google = raw_input("Command:")
	
	print "-----------------------------------------"
	print "Command to Search Browser in Google"
	print "-----------------------------------------"
	searchbrowser = raw_input("Command:")
	
	print "-----------------------------------------"
	print "Command to Search in Duck. In Browser."
	print "-----------------------------------------"
	duckbrowser = raw_input("Command:")
	
	print "-----------------------------------------"
	print "Command to Open a file in your choosen directory."
	print "-----------------------------------------"
	openf = raw_input("Command:")
	
	print "-----------------------------------------"
	print "Command to List Available Prgrams"
	print "-----------------------------------------"
	lis = raw_input("Command:")
	
	
	#write custom commands to data.txt file | each on a new line
	f = open('data.txt', 'w')
	f.write(directory+"\n") #Line 0
	f.write(google+"\n") #Line 1
	f.write(searchbrowser+"\n") #Line 2
	f.write(duckbrowser+"\n") #Line 3
	f.write(openf+"\n") #Line 4
	f.write(lis+"\n") #Line 5
	f.close()

#processProtocol = MyProcessProtocol()

#define main function
def command():
	
	#input command
	command = raw_input(':> ')
	
	#start checking for command precursors and decide what to do
	#when you find it
	
	if google.rstrip('\n') in command:
		query = command.replace(google, "") #remove the precursor command
		query = urllib.urlencode ({ 'q' : query }) #encode the query
		response = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query).read() #send the query to google API
		json = m_json.loads(response)
		results = json['responseData']['results'] #gather the desired data
	
		#for each result, print the title and url
		for result in results:
			title = result['title']
			url = result['url']
			print (title + ';' + url)
		
	
	if openf.rstrip('\n') in command:
		query = command.replace("open ", "") #remove precursor
		pgrm = "%s%s.lnk" % (directory.rstrip('\n'), query) #join directory and program name
		os.startfile(pgrm)
#		reactor.spawnProcess(processProtocol, pgrm) #execute
#		reactor.run()
		
	#replace all data in data.txt with nil
	if "wipe cache" in command:
		f = open('data.txt', 'w')
		f.write('')
		f.close()
	
	#set variable to open new tab in browser
	new = 2	
	
	if searchbrowser.rstrip('\n') in command:
		query = command.replace(searchbrowser, "") #remove precursor
		url = ("http://www.google.com/search?q=" + query) #append query to end of google search
		webbrowser.open(url, new=new) #open url in new tab
		
	if duckbrowser in command:
		query = command.replace(duckbrowser, '')
		url = ("http://duckduckgo.com/?q=" + query)
		webbrowser.open(url, new=new)
		
	if lis in command:
		newdir = directory.replace("\\", "", 1) #clean up directory
		os.system('dir ' + newdir) #list contents of shortcut directory
	
	#create array for possible quit commands
	shut = {'shut', 'quit', 'stop', 'kill', 'exit', 'close'}
	
	#check to see if entered command is in {shut} array
	if command in shut:
		quit()
	#if it isn't specific, check if the string contains the following...
	#this allows for custom strings to still execute quit
	#such as "shut up" or "kill me"
	elif "shut" in command:
		quit()
	elif "exit" in command:
		quit()
	elif "stop" in command:
		quit()
	elif "kill" in command:
		quit()

#check to see if data.txt contains any data
#if it doesn't, call start() to assign variables
#if it does, continue
if len(open('data.txt').readlines()) < 1:
	start()
else:
	pass

#read variables from data.txt to be useable outside the start function
#and then reassign them
f = open('data.txt', 'r')
lines = f.readlines()
directory = lines[0].rstrip('\n')
google = lines[1].rstrip('\n')
searchbrowser = lines[2].rstrip('\n')
duckbrowser = lines[3].rstrip('\n')
openf = lines[4].rstrip('\n')
lis = lines[5].rstrip('\n')
f.close()

#show the user what his/her custom commands are
print "Directory: [%s]" % directory.rstrip('\n')
print "Commands:"
print "[%s]" % google.rstrip('\n')
print "[%s]" % searchbrowser.rstrip('\n')
print "[%s]" % openf.rstrip('\n')
print "[%s]" % duckbrowser.rstrip('\n')
print "[%s]" % lis.rstrip('\n')
print "[Wipe Cache]"
print "quit/kill/exit/shut"
print "-----------------------------------------"

#loop forever
#will ask for another command after one executes; infinitely
#will break if error occurs
while 1:
	command()
