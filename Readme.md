⚠️Warning: It shouldn't be taken as a tool which will work in all conditions but it is almost a complete framework providing you required things at once. You might have to edit/add/delete one or more lines in `#Browser Interactions` part in `attendance.py` according to your forms in most cases. It is not going to help you in marking proxies and shouldn't be misunderstood that way. Make sure to change your name or rollno. in `attendance.py` in the same order it is on form at the place of `YourName/Rollno.`. 

# Online Attendance Automation tool

### Installation
Step 1 : Download the repository  
```
git clone https://github.com/Amit0617/online-attendance
```
Step 2 : Move into the directory  
```
cd online-attendance
```
Step 3 : Setup the required environment  
If you have pip installed  
```
make -s gecko setup 
```
OR If you are not sure about it  
```
make -s gecko pip setup
```
Step 4 : Make sure your environment is ready
```
make -s verify_setup
```
This should output like this :
```
===> Checking pip...
(1/2) VERSION=21.3.1
(2/2) LOCATION=/home/amit/.local/lib/python3.10/site-packages/pip
===> Checking geckodriver...
(1/1) TYPE=executable
===> Checking if geckodriver is on path
geckodriver --> /home/amit/Downloads/geckodriver
```
You are ready to automate attendance marking!

### Usage
Step 1 : Make sure to make it executable(this step is one time only)
```
chmod u+x attendance.py
```
(Assuming you are inside the cloned directory i.e., `online-attendance`)  

Step 2 :
```
./attendance.py [link of your attendance] OPTIONS
```
And you are done.

##### Examples:
```
./attendance.py https://www.surveyheart.com/form/60a103fc03dbe251fdca08b0
```
If you want it to happen in background(headless):
```
./attendance.py [link] -b
```
Maybe you would like it to save a screenshot of final status if something went wrong in headless mode:
```
./attendance.py [link] -b -s ~/Pictures/
```
Check help:
```
./attendance.py -h
```
### Uninstall
Step 1 : Clean setup environment
(Assuming you are in cloned directory i.e., `online-attendance`)  
```
make clean
```
Step 2 : Clean cloned directory
```
cd .. ; rm -rf online-attendance
```
<hr></hr>

###### TODO:
[] To make attendance.py suggest help on wildcards  
[] To update usage with several supported flags  
[] Add more examples for different usecases.  

