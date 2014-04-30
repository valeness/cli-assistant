import urllib
import json as m_json
import os
import webbrowser

def start():
	
	print """Here we will set some variables that will allow you to 
	customize your commands. All commands follow this procedure 
	"[command] [string/query]". Please refer to the readme for more."""
	
	print "First, set your program shortcuts directory."
	directory = raw_input("Directory:")
	
	print "Google Command"
	google = raw_input("Command:")
	
	print "Command to Search Browser in Google"
	searchbrowser = raw_input("Command:")
	
	f = open('data.txt', 'w')
	f.write(directory+"\n") #Line 0
	f.write(google+"\n") #Line 1
	f.write(searchbrowser) #Line 2


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
		
	
	if "open" in command:
		query = command.replace("open ", "")
		
		pgrm = "%s%s.lnk" % (directory.rstrip('\n'), query)
		
		os.system(pgrm)
		
	if "wipe cache" in command:
		f = open('data.txt', 'w')
		f.write('')
		f.close()
		
	new = 2	
	
	if searchbrowser in command:
		query = command.replace(searchbrowser, "")
		url = ("http://www.google.com/search?q=" + query)
		webbrowser.open(url, new=new)
		
	
	shut = {'shut', 'quit', 'stop', 'kill', 'exit', 'close'}
	
	if command in shut:
		quit()
	elif "shut" in command:
		quit()
	elif "exit" in command:
		quit()
	elif "stop" in command:
		quit()

if len(open('data.txt').readlines()) < 1:
	start()
else:
	pass

f = open('data.txt', 'r')
lines = f.readlines()
directory = lines[0]
google = lines[1]
searchbrowser = lines[2]
f.close()

print "Directory: [%s]" % directory.rstrip('\n')
print "Commands:"
print "[%s]" % google.rstrip('\n')
print "[%s]" % searchbrowser.rstrip('\n')
print "open"
print "quit/kill/exit"

while 1:
	command()
