Command Line Interface (CLI) Assistant
================

Like Siri, but cyberpunk as hell and CLI.

================

HOWTO:

1: Drop the 'cliassis.py' and 'config.py' file into your Python directory. (Usually located at C:\Python27) Your number may be different
2: Run the 'config.py' script with python by navigating to your python directory inside a command prompt (python config.py)
3: Next open up the config.cfg file that was created with notepad or another text editor.
4: You will need to edit the 'shortcut_directory' to a directory containing shortcuts to programs you wish to launch with CLI Assistant. (You can edit the other commands too, just be careful)
5: Lastly launch 'cliassis.py' like you did the config script and you're done!

================

Commands and Opening Programs:

Sadly, CLI Assistant can not search your computer for programs, you will need to specify a directory full of shortcuts
to programs that you want to open with CLI Assistant. My directory is "C:\shortcuts\"

**It is important that you end your directory with a backslash**
***All programs dropped in this directory need to end in .lnk, signifying that it is a shortcut***

Commands are executed by denoting a precursory string. The easiest way to explain this is through example.
If I want to google something, I would need to first type 'google' and then my search query. So to google "tony stark",
I would have to type "google tony stark". However, these commands are set by you to be custom, meaning that the precursor 
'google' could be anything. Like: "ubenflabin tony stark" would work perfectly fine if I set the google command to be 
'ubenflabin' on startup. 

================

Current Command/Config File Explanations

[directories]
#This directory is where you stick all your "program.lnk" shortcuts.
shortcut_directory = C:\shortcuts 

[commands]
#Edit this to choose the google command that will google search within your terminal and
#return the top 4 results complete with titles and full urls
google_command = google
#This command will launch google.com and automatically search your query.
google_browser = browse
#This command does the same thing as google_browser, but uses duckduckgo search.
duck_browser = duck
#This is the precursor command to opening files from your shorcut_directory. Make sure you only type the name of the file
#and not the extension. The program takes care of appending the '.lnk' and everything. So if I had a shortcut 'chrome.lnk'
#I would type 'open chrome' and it would take care of everything.
open_file = open
#Use this command to list what programs are in your shortcut_directory
list_shortcuts = list
#This isn't a precursor command. Just type 'blog' and it will initiate a function to email your
#blog address to post via email
blog_command = blog

[email]
#Your email
your_email = example@example.com
#The special email to post to your blog
blog_email = blog@example.com
#The address you have to visit in order for your blog to 'check' for emails and post them. 
blog_mail_url = yourdomain.com/blog/wp-mail.php



================

If you have any questions, concerns, or want to contribute to the project, please feel free to contact me at 
valeness84@gmail.com
