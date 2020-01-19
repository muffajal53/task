# Intial Setup

Create a virtual environment and install requirements

	Creating virtual enviornment for python 3.6
	- virtualenv .env -p python3.6
	
	Activate the created environment (i.e .env)
	- source .env/bin/activate
	
	Install all the required dependencies from the requirement.txt file
	- pip install -r requirement.txt

If you want to see that result in GUI then you have to install tkinter for it.
	- sudo apt-get install python3.6-tk

Check all the dependencies successfully installed -
	- pip freeze


# Task Details

1. Create Chess Board Image Using Numpy/Pandas/matplotlib.
	For this task, Please Run the chess.py file.
	- python chess.py

2. Write Alogirithm and Pseduo code for iterative sequence Problem.
	For this task, Please Run the sequence.py file.
	- python sequence.py

	and for Pseduo, please see it.
	- Pseudocode_sequence.txt

3. Create Django Application for Movie information storage.
	
	please Go to the movie_management
	- cd movie_management

	- pip install -r requirement.txt

	Note:- If you want to setup new database then run below command for creating tables.
		- python manage.py makemigrations
		- python manage.py migrate

	Please run below commnd for starting the django server
	- python manage.py runserver

