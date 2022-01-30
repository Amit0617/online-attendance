#!splinter/bin/python
import sys;
import os;
commands = ' '.join(sys.argv[1:]);
#os.system("ls | grep splinter");
#os.system("source splinter/bin/activate");
'''
for arg in sys.argv[1:]:          
	if ' ' in arg:
		commands+= '"{}" '.format(arg)   
	else:
		commands+="{} ".format(arg)
'''

print(commands)
from splinter import Browser
browser = Browser('firefox', headless=("-h" in commands))
url = str(sys.argv[1]);
"""

"""
print(url);
command_list = commands.split(' ');
if "-s" in command_list:
	pos = command_list.index("-s");
	print(pos);
	print(command_list);
	screenshot_location = command_list[pos + 1];
	print("{}splinter.png".format(screenshot_location));


#Browser Interactions
browser.visit(url);
browser.find_by_id('start_survey_button').click();
browser.find_by_tag('textarea')[0].fill('YourName/RollNo');
#browser.find_by_tag('textarea')[1].fill('YourName/RollNo');
browser.find_by_id('submission').click();

#Printing Status
if browser.find_by_id('submitted_success_text').visible or browser.is_text_present('Submitted'):
	print ("Attendance Marked Successfully!");
		
else:
	print ("Something went wrong");
	screenshot_path = browser.screenshot('{}splinter.png'.format(screenshot_location));
	print ("Screenshot taken:{}splinter.png".format(screenshot_location));
browser.quit();
"""	
"""
