# Intial Setup


Creating virtual enviornment, activating and installing all the required dependencies for the first 2 tasks(i.e Chess Board and iterative sequence Problem )
	
	virtualenv .env -p python3.6
	
	source .env/bin/activate
	
	pip install -r requirement.txt
	
Note:- For the first 2 tasks, do make the use of root  'requirement.txt'  file.

Check all the dependencies successfully installed -
	
	pip freeze


# Task Details

1. Create Chess Board Image Using Numpy/Pandas/matplotlib. 
For this task, Please run chess.py file.
	
	python chess.py
	

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

