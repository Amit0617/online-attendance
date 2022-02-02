#!Attendance/bin/python
import sys;
import os;
from datetime import datetime
commands = ' '.join(sys.argv[1:]);

#print(commands)
if '-h' in commands:
	print('Usage: ./attendance.py LINK [OPTION]');
	print('Mark attendance online with given link');
	print('-b	Work in background (headless mode)');
	print('-h	Print this help and exit');
	print('-s \033[4mPATH/TO/DIRECTORY\033[0m	Save screenshot at the given directory when script finds something wrong or unexpected');
	print('-sf \033[4mPATH/TO/DIRECTORY\033[0m	Save screenshot forcefully no matter what happens');
	print('-sfd	Save screenshot forcefully no matter what happens at default location \033[4m/tmp\033[0m');
	sys.exit();

from splinter import Browser
browser = Browser('firefox', headless=("-b" in commands))
url = str(sys.argv[1]);

print("Visiting {}".format(url));
command_list = commands.split(' ');
path = "None";
def get_path(pos):
	#print(pos);
	#print(command_list);
	path = command_list[pos + 1];
	print(path);
	return path
	#print("{}splinter.png".format(path));

def take_ss():
		print ("Taking Screenshot...");
		ss_path = browser.screenshot("{}{}.png".format(path,str(datetime.now())))
		print ("Screenshot  taken:{}{}.png".format(path,str(datetime.now())))

def print_success():
	print ("Attendance Marked Successfully!");
	if "-sf" in command_list:
		take_ss();
	elif "-sfd" in command_list:
		ss_path = browser.screenshot();
		print("Screenshot taken: {}".format(ss_path));

if "-s" in command_list:
	pos = command_list.index("-s");
	path = get_path(pos);
	#print (path)

elif "-sf" in command_list:
	pos = command_list.index("-sf");
	path = get_path(pos);
	#print(path)
	
elif "-sfd" in command_list:
	#path = "~/Pictures/";
	print("Default Path:{}".format(path))

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
'''
elif 'forms.gle' in url:
	browser.find_by_tag('input')[1].fill('YourName/RollNo');
	browser.find_by_class('appsMaterialWizButtonPaperbuttonFocusOverlay').click();
'''
#For google forms with 2 test input only
if 'forms.gle' in url:
	browser.find_by_tag('input')[2].fill('YourName/RollNo');
	browser.find_by_tag('input')[3].fill('YourName/RollNo');
	browser.find_by_css('.appsMaterialWizButtonPaperbuttonLabel')[0].click();
#Comment out any one part of google forms above according to your condition	
	
#Printing Status in terminal		
if browser.is_text_present('Submitted'):
	print_success();
	
elif browser.is_text_present('recorded'):
	print_success();
	
elif browser.is_text_present('successfully'):
	print_success();
	
else:
	print ("Something went wrong");
	screenshot_path = browser.screenshot('{}splinter.png'.format(path,str(datetime.now())));
	print ("Screenshot taken:{}{}.png".format(path,str(datetime.now())));
browser.quit();

