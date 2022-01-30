setup:
#ifneq (,$(findstring p, $(MAKEFLAGS)))
#endif
	curl -fsSL -o ~/Downloads/geckodriver-v0.30.0-linux64.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
	tar -xzvf ~/Downloads/geckodriver-v0.30.0-linux64.tar.gz -C ~/Downloads/
	sudo ln -s -T ~/Downloads/geckodriver /usr/bin/geckodriver

#ifneq (,$(findstring v, $(MAKEFLAGS)))
	PWD=$(shell pwd)
	export ATTENDANCE = ${PWD}/Attendance
	python3 -m venv Attendance
	source Attendance/bin/activate; \
	pip3 install splinter; \
	pip3 install selenium
#endif
pip:
	python3 -m ensurepip --upgrade
	python3 -m pip install --upgrade pip

verify_setup: check_pip verify_gecko

start:
	source ${ATTENDANCE}/bin/activate

check_pip:
	echo "===> Checking pip..."
	echo "(1/2) VERSION=$(shell python3 -m pip --version | cut -d ' ' -f2)"
	echo "(2/2) LOCATION=$(shell python3 -m pip --version | cut -d ' ' -f4)"

verify_gecko:
	echo "===> Checking geckodriver..."
	echo "(1/1) TYPE=$(shell file ~/Downloads/geckodriver | cut -d ' ' -f6 | tr -d ,)"
	echo "===> Checking if geckodriver is on path"
	echo "geckodriver --> $(shell file /usr/bin/geckodriver | cut -d ' ' -f5)"

clean:
	-rm -rf $(ATTENDANCE)
