#!Attendance/bin/python
import sys;
import os;
from datetime import datetime
commands = ' '.join(sys.argv[1:]);

#print(commands)
def print_help():
    print('Usage: ./attendance.py LINK [OPTION]');
    print('Mark attendance online with given link');
    print('-b    Work in background (headless mode)');
    print('-h    Print this help and exit');
    print('-s \033[4mPATH/TO/DIRECTORY\033[0m    Save screenshot at the given directory when script finds something wrong or unexpected');
    print('-sf \033[4mPATH/TO/DIRECTORY\033[0m    Save screenshot forcefully no matter what happens');
    print('-sfd    Save screenshot forcefully no matter what happens at default location \033[4m/tmp\033[0m');
    sys.exit();

if '-h' in commands:
    print_help();

elif len(sys.argv) <= 1:
    print_help();

from splinter import Browser
browser = Browser('firefox', headless=("-b" in commands))
url = str(sys.argv[1]);

print("Visiting {}".format(url));
command_list = commands.split(' ');
path = "None";

#get path from given position
def get_path(pos):
    #path should be next word in string or next element of list
    path = command_list[pos + 1];
    print(path);
    return path

#take screenshot and tell its location
def take_ss():
    print ("Taking Screenshot...");
    ss_path = browser.screenshot("{}{}.png".format(path,str(datetime.now())))
    print ("Screenshot taken:{}.png".format(ss_path))

#greet if successful
def print_success():
    print ("Attendance Marked Successfully!");

    #when forceful screenshot is requested
    if "-sf" in command_list:
        take_ss();

    #when save at default location forcefully is requested
    elif "-sfd" in command_list:

        #default location is /tmp by library support
        ss_path = browser.screenshot();
        print("Screenshot taken: {}".format(ss_path));

if "-s" in command_list:
    pos = command_list.index("-s");
    path = get_path(pos);

elif "-sf" in command_list:
    pos = command_list.index("-sf");
    path = get_path(pos);

elif "-sfd" in command_list:
    print("Default Path:{}".format(path))

else:
    print('Screenshot not required')

#Browser Interactions
browser.visit(url);

#For surveyheart forms
if 'surveyheart' in url:
    browser.find_by_id('Start').click();
    browser.find_by_tag('textarea')[0].fill('YourName/RollNo');
    #uncomment following line for two input surveyheart form
    #browser.find_by_tag('textarea')[1].fill('YourName/RollNo');
    browser.find_by_id('Submit').click();

#For google forms with 2 test input only
elif 'forms.gle' in url or 'docs.google.com/forms' in url:
    browser.find_by_tag('input')[2].fill('YourName/RollNo');
    browser.find_by_tag('input')[3].fill('YourName/RollNo');
    browser.find_by_css('.NPEfkd.RveJvd.snByac')[0].click();

#For google forms with 1 text input only
'''
elif 'forms.gle' in url or 'docs.google.com/forms' in url:
    browser.find_by_tag('input')[1].fill('YourName/RollNo');
    browser.find_by_class('.NPEfkd.RveJvd.snByac').click();
'''
#Comment out any one part of google forms above according to your condition

#Printing Status in terminal
if browser.is_text_present('Submitted') or browser.is_text_present('recorded') or browser.is_text_present('successfully'):
    print_success();

else:
    print ("Something went wrong");
    ss_path = browser.screenshot('{}splinter.png'.format(path,str(datetime.now())));
    print ("Screenshot taken:{}.png".format(ss_path));
browser.quit();

