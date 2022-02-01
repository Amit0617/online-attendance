#!splinter/bin/python
import sys;
import os;
from datetime import datetime
commands = ' '.join(sys.argv[1:]);

print(commands)
if '-h' in commands:
	print('Usage: ./attendance.py LINK [OPTION]');
	print('Mark attendance online with given link');
	print('-b	Work in background in headless mode');
	print('-h	Print this help and exit');
	print('-s PATH/TO/DIRECTORY		Save screenshot at the given directory when script finds something wrong or unexpected')
	print('-sf PATH/TO/DIRECTORY	Save screenshot forcefully no matter what happens')

from splinter import Browser
browser = Browser('firefox', headless=("-b" in commands))
url = str(sys.argv[1]);

print("Visiting {}".format(url));
command_list = commands.split(' ');

def get_path(command_list):
	pos = command_list.index("-s") or command_list.index("-sf");
	#print(pos);
	#print(command_list);
	path = command_list[pos + 1];
	return path
	#print("{}splinter.png".format(path));
	
if "-s" in command_list:
	get_path(command_list);
	print (path)

elif "-sf" in command_list:
	get_path(command_list);
	print(path)
	
else:
	print('Screenshot not required')

#Browser Interactions
browser.visit(url);
#For surveyheart forms
if 'surveyheart' in url:
	browser.find_by_id('start_survey_button').click();
	browser.find_by_tag('textarea')[0].fill('YourName/RollNo');
	#browser.find_by_tag('textarea')[1].fill('YourName/RollNo');
	browser.find_by_id('submission').click();
#For google forms with 1 text input only
elif 'forms.gle' in url:
	browser.find_by_tag('input')[1].fill('YourName/RollNo');
	browser.find_by_class('appsMaterialWizButtonPaperbuttonFocusOverlay').click();
#For google forms with 2 test input only
elif 'forms.gle' in url:
	browser.find_by_tag('input')[2].fill('YourName/RollNo');
	browser.find_by_tag('input')[3].fill('YourName/RollNo');
	browser.find_by_class('appsMaterialWizButtonPaperbuttonFocusOverlay').click();
	
#Printing Status in terminal
if browser.find_by_id('submitted_success_text').visible or browser.is_text_present('Submitted') or browser.is_text_present('recorded') or browser.is_text_present('successfully'):
	print ("Attendance Marked Successfully!");
	if "-sf" in command_list:
		print ("Taking Screenshot...");
		print ("Screenshot  taken:{}{}.png".format(path,str(datetime.now())));
else:
	print ("Something went wrong");
	screenshot_path = browser.screenshot('{}splinter.png'.format(path,str(datetime.now())));
	print ("Screenshot taken:{}{}.png".format(path,str(datetime.now())));
browser.quit();

