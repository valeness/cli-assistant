import urllib
from bs4 import BeautifulSoup
import nltk
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

def language():
	url = raw_input('url>>')
	command = raw_input('command>>')		
	
	final = config.get('nicknames', url)

	response = urllib.urlopen(final).read()
		
	soup = BeautifulSoup(response)
	text = soup.get_text().encode('UTF-8')
	tokens = nltk.word_tokenize(text)
	text = nltk.Text(tokens)
	
	if 'search' in command:
		query = raw_input('query>>')
		print text.concordance(query)
		
	if 'len' in command:
		print len(text)
	
	if 'similar' in command:
		query = raw_input('query>>')
		print text.similar(query)
