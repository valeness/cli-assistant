import ConfigParser
import os

config = ConfigParser.RawConfigParser()
config.add_section('directories')
config.add_section('commands')
config.add_section('email')
config.add_section('language')
config.add_section('nicknames')

config.set('directories', 'shortcut_directory', 'C:\shortcuts')
config.set('commands', 'google_command', 'google')
config.set('commands', 'google_browser', 'browse')
config.set('commands', 'duck_browser', 'duck')
config.set('commands', 'open_file', 'open')
config.set('commands', 'list_shortcuts', 'list')
config.set('commands', 'blog_command', 'blog')
config.set('email', 'your_email', 'example@example.com')
config.set('email', 'blog_email', 'blog@example.com')
config.set('email', 'blog_mail_url', 'yourdomain.com/blog/wp-content.php')
config.set('commands', 'journal', 'write')
config.set('commands', 'search_journal', 'search')
config.set('commands', 'language_processing', 'key')
config.set('commands', 'add_nickname', 'add')

config.set('language', 'keyword_context', 'search')

config.set('nicknames', 'python', 'http://python.org')
config.set('nicknames', 'vales', 'http://valeness.tk')

with open('config.cfg', 'wb') as configfile:
	config.write(configfile)
	print 'Configuration Complete!'

print 'Open Configuration file?'
ans = raw_input(':>')

if 'no' in ans:
	quit()
else:
	os.startfile('config.cfg')
