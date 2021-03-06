#import necessary modules
import urllib
import language
import json as m_json
import os
import webbrowser
import random
from lxml import etree
import time
import datetime
import ConfigParser
#actual sending function
import smtplib
#import the email modules
from email.mime.text import MIMEText
import language

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

#get variables from config.cfg
directory = config.get('directories', 'shortcut_directory')
google = config.get('commands', 'google_command')
searchbrowser = config.get('commands', 'google_browser')
duckbrowser = config.get('commands', 'duck_browser')
openf = config.get('commands', 'open_file')
lis = config.get('commands', 'list_shortcuts')
blog = config.get('commands', 'blog_command')
sender = config.get('email', 'your_email')
receiver = config.get('email', 'blog_email')
weburl = config.get('email', 'blog_mail_url')
journal = config.get('commands', 'journal')
search = config.get('commands', 'search_journal')
word = config.get('language', 'keyword_context')
add = config.get('commands', 'add_nickname')
joke = 'joke'
nick = 'add'

#define main function
def command():
	
	#input command
	command = raw_input(':> ')
	
	#start checking for command precursors and decide what to do
	#when you find it
	
	if google in command:
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
		os.system('dir ' + directory) #list contents of shortcut directory
	
	if joke in command:
		random.choice(jokes)()
		
	if 'tries' in command:
		print 'Loops: %s' % tries
		
	if blog in command:
		post()
		
	if journal in command:
		document, article = write()
		
	if search in command:
		query = command.replace(search + ' ', "") #remove precursor
		post = open('journal.txt', 'r')
		postf = str(post.read())
		
		root = etree.fromstring(postf)
		
		articles = root.xpath('//article[contains(@tags, "%s")]' % query)
				
		for article in articles:
			print etree.tostring(article, pretty_print=True)
			
	if word in command:
		language.language()	
	
	if nick in command:
		site = raw_input('website>>')
		name = raw_input('nickname>>')
		nickdic[site] = name
		
	if add in command:
		name = raw_input('name>>')
		url = raw_input('url>>')
		config.set('nicknames', name, url)
		print 'Done!'
		
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


#show the user what his/her custom commands are
print "Directory: [%s]" % directory.rstrip('\n')
print "Commands:"
print "[%s]" % google.rstrip('\n')
print "[%s]" % searchbrowser.rstrip('\n')
print "[%s]" % openf.rstrip('\n')
print "[%s]" % duckbrowser.rstrip('\n')
print "[%s]" % lis.rstrip('\n')
print "[%s]" % blog.rstrip('\n')
print "[Wipe Cache]"
print "quit/kill/exit/shut"
print "-----------------------------------------"

#set joke functions
def joke1():
	print 'Why did the Rabbit cross the road?'
	loop = 0
	while loop == 0:
		ans = raw_input('reply:').lower()
		if 'why' in ans:
			print 'To eat the chicken!'
			loop = 1
			break
		print 'Go on! Ask why!'	

def joke2():
	print 'Glenn'

#create array for jokes
jokes = [joke1, joke2]

tries = 0

def post():
	post = open('mail.txt', 'w')
	title = raw_input('title>>')
	while 1:
		message = raw_input('>>')
		post.write(message + '\n')
		
		if '[done]' in message:
			post = open('mail.txt', 'r')
			msg = MIMEText(post.read())
			post.close
			
			msg['Subject'] = title
			msg['From'] = sender
			msg['To'] = receiver
			s = smtplib.SMTP('smtp.gmail.com:587')
			s.starttls()
			user = raw_input('Username/Email>>')
			password = raw_input('Password>>')
			s.login(user, password)
			s.sendmail(sender, [receiver], msg.as_string())
			s.quit()
			print 'Do you want to post this message?'
			print 'This requires your browser. Only accepts yes/no'
			print '---------------------------------'
			send = raw_input('choice>>')
			
			new = 2
			
			if 'yes' in send:
				webbrowser.open(weburl, new=new)
				break
			elif 'no' in send:
				break

def write():
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	
		post = open('post.txt', 'w')
		document = etree.Element('document')
		title = raw_input('title>>')
	
		while 1:
			message = raw_input('post>>')
			post.write(message + '\n')
			if '[done]' in message:
				tags = raw_input('tags>>')
				break
			
			

		post = open('post.txt', 'r')
		postf = post.read()

		article = etree.SubElement(document, 'article', title=title, date=st, tags=tags)
		article.text = postf
		
		post.close()
	
		with open('journal.xml', 'a') as file:
			file.write(etree.tostring(article, pretty_print=True) + '\n')
			file.close()
			
		return document, article
			
def email():
	pass

#loop forever
#will ask for another command after one executes; infinitely
#will break if error occurs
while 1:
	command()
	tries = tries + 1
