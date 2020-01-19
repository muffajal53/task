# Intial Setup


Creating virtual enviornment, activating and installing all the required dependencies for the first 2 tasks(i.e Chess Board and iterative sequence Problem )
	
	virtualenv .env -p python3.6
	
	source .env/bin/activate
	
	pip install -r requirement.txt
	
Note:- For the first 2 tasks, do make the use of root  'requirement.txt'  file.

Check all the dependencies successfully installed -
	
	pip freeze


# Task Details

Task 1 :- Create Chess Board Image Using Numpy/Pandas/matplotlib. 
For this task, Please run chess.py file.
	
	
	python chess.py

Output:- Chess.png
	
Task 2 :- Write Alogirithm and Pseduo code for iterative sequence Problem.
For this task, Please Run the sequence.py file.

	python sequence.py

Output :- 
	
	Please insert the number for iterative sequence :- 15
	15
	46
	23
	70
	35
	106
	53
	160
	80
	40
	20
	10
	5
	16
	8
	4
	2
	1

and for Pseduo, please see it.
	
	Pseudocode_sequence.txt

Task 3:- Create Django Application for Movie Information Storage.
Creating virtual enviornment and activating for Django application 
	
	virtualenv .movie -p python3.6
	
	source .movie/bin/activate
	
Navigate to movie_management folder

	cd movie_management

Install Dependencies

	pip install -r requirement.txt
	
Databse Creation

	python manage.py makemigrations
	python manage.py migrate
	
starting the django server
	
	python manage.py runserver

