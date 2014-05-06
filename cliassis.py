import urllib
import json as m_json
import os
import webbrowser

def start():
	
	print """Here we will set some variables that will allow you to 
	customize your commands. All commands follow this procedure 
	"[command] [string/query]". End all directories with a backslash or
	else it will not work. Please refer to the readme for more.
	-----------------------------------------------------------------
	"""
	
	print "First, set your program shortcuts directory. Remember the Backslash"
	print "-----------------------------------------"
	directory = raw_input("Directory:")
	
	print "Google Command"
	print "-----------------------------------------"
	google = raw_input("Command:")
	
	print "Command to Search Browser in Google"
	print "-----------------------------------------"
	searchbrowser = raw_input("Command:")
	
	print "Command to Search in Duck. In Browser."
	print "-----------------------------------------"
	duckbrowser = raw_input("Command:")
	
	print "Command to Open a file in your choosen directory."
	print "-----------------------------------------"
	openf = raw_input("Command:")
	
	print "Command to List Available Prgrams"
	print "-----------------------------------------"
	lis = raw_input("Command:")
	
	f = open('data.txt', 'w')
	f.write(directory+"\n") #Line 0
	f.write(google+"\n") #Line 1
	f.write(searchbrowser+"\n") #Line 2
	f.write(duckbrowser+"\n") #Line 3
	f.write(openf+"\n") #Line 4
	f.write(lis+"\n") #Line 5
	f.close()


def command():
	command = raw_input(':> ')
	if google.rstrip('\n') in command:
		query = command.replace(google, "")
		query = urllib.urlencode ({ 'q' : query })
		response = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query).read()
		json = m_json.loads(response)
		results = json['responseData']['results']
	
		for result in results:
			title = result['title']
			url = result['url']
			print (title + ';' + url)
		
	
	if openf.rstrip('\n') in command:
		query = command.replace("open ", "")
		
		pgrm = "%s%s.lnk" % (directory.rstrip('\n'), query)
		
		os.system(pgrm)
		
	if "wipe cache" in command:
		f = open('data.txt', 'w')
		f.write('')
		f.close()
		
	new = 2	
	
	if searchbrowser.rstrip('\n') in command:
		query = command.replace(searchbrowser, "")
		url = ("http://www.google.com/search?q=" + query)
		webbrowser.open(url, new=new)
		
	if duckbrowser in command:
		query = command.replace(duckbrowser, '')
		url = ("http://duckduckgo.com/?q=" + query)
		webbrowser.open(url, new=new)
		
	if lis in command:
		newdir = directory.replace("\\", "", 1)
		os.system('dir ' + newdir)
	
	shut = {'shut', 'quit', 'stop', 'kill', 'exit', 'close'}
	
	if command in shut:
		quit()
	elif "shut" in command:
		quit()
	elif "exit" in command:
		quit()
	elif "stop" in command:
		quit()
	elif "kill" in command:
		quit()

if len(open('data.txt').readlines()) < 1:
	start()
else:
	pass

f = open('data.txt', 'r')
lines = f.readlines()
directory = lines[0].rstrip('\n')
google = lines[1].rstrip('\n')
searchbrowser = lines[2].rstrip('\n')
duckbrowser = lines[3].rstrip('\n')
openf = lines[4].rstrip('\n')
lis = lines[5].rstrip('\n')
f.close()

print "Directory: [%s]" % directory.rstrip('\n')
print "Commands:"
print "[%s]" % google.rstrip('\n')
print "[%s]" % searchbrowser.rstrip('\n')
print "[%s]" % openf.rstrip('\n')
print "[%s]" % duckbrowser.rstrip('\n')
print "[%s]" % lis.rstrip('\n')
print "[Wipe Cache]"
print "quit/kill/exit/shut"

while 1:
	command()
