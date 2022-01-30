Make sure `pip` is installed :
```
python3 -m pip --version
```
If not installed(`ensurepip` module comes builtin with python) :
```
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```
If installing `pip` first time then console should have thrown a warning something like `pip is installed on 'path/where/it/is/installed' which is not on your PATH` and second command given above would not have worked. Then
```
export PATH=path/where/it/is/installed:$PATH
```
will add `pip` to your PATH.  
Get the files for it
```
git clone https://github.com/amit0617/online-attendance; cd online-attendance
```
Create a venv(helps in better management of different dependencies)
```
python3 -m venv Attendance
```
Now a directory with name `Attendance` should be created in your working directory.
To activate that `venv`:
```
source Attendance/bin/activate
```
Install `splinter` in it 
```
pip3 install splinter
```
Install `selenium` in it.
```
pip3 install selenium
```
Also make sure `firefox` and `geckodriver` is in PATH. Type `firefox` in your terminal if it launches then it is in PATH(which remains generally). But `geckodriver` would not be doing anything(if it is not preconfigured by you before).
So first download latest geckodriver(*.tar.gz) from github [releases](https://github.com/mozilla/geckodriver/releases) section according to your OS. Extract geckodriver executable from it and add it to PATH.
So we will just link our geckodriver executable path to a path which is already in PATH(This line sounds really funny, this would make sense if you understand that PATH is environment variable which you can see using `echo $PATH` where `:` is delimiter). For example we have `/usr/bin` generally already in PATH.
```
sudo ln -s -T /home/user/Downloads/geckodriver /usr/bin/geckodriver
```
Assuming `/home/user/Downloads/geckodriver` is where you extracted your geckodriver. Also make sure you can execute your geckodriver by `./path/to/geckodriver` for example `./home/user/Downloads/geckodriver`. It should say something like `Listening on 127.0.0.1:4444`
Check if it was successful, using : 
```
file /usr/bin/geckodriver
```
It should echo something like `/usr/bin/geckodriver: symbolic link to /home/user/Downloads/geckodriver`.

