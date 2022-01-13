# Quiz API

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technology](#technology)
4. [Backend Setup Instructions](#backend-setup-instructions)

## Introduction

The quiz application having MCQs related to various categories where the user can roll out from his previous question and can attempt only once.

## Features: 
1) Admin is able to create.
2) Authenticated Users can be attempt the quiz.
3) Each quiz is related to specific can have 1 or more questions and the question types can be MCQ (2-4 options) or open text.
4) A question will have text and optionally an image.
5) A user can be able to see the list of quizzes (live, past and upcoming).
6) A user can be able to attempt live quizzes (at max once) and can roll out from where they left.

## Technology:

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>  <img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/><img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/sqlite-0B96B2?style=for-the-badge&logo=sqlite&logoColor=white"/> 

- **Backend**: Django Rest Framework
- **IDE**: VS Code
- **API Testing & Documentation:** Swagger
- **Version Control**: Git and GitHub
- **Database**: Sqlite

### Backend Setup Instructions

- Fork and Clone the repo using
```
$ git clone https://github.com/rudrakshi99/Quiz_App.git
```
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip3 install -r requirements.txt
```
- Make migrations using
```
$ python3 manage.py makemigrations
```
- Migrate Database
```
$ python3 manage.py migrate
```
- Create a superuser
```
$ python3 manage.py createsuperuser
```
- Run server using
```
$ python3 manage.py runserver
``` 
