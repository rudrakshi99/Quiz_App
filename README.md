# Quiz_App

The quiz application having MCQs related to various categories where the user can roll out from his previous question and can attempt only once.


## Technology Stack to be used:

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>  <img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/><img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/sqlite-0B96B2?style=for-the-badge&logo=sqlite&logoColor=white"/> 

- **Backend**: Django Rest Framework
- **IDE**: VS Code
- **Version Control**: Git and GitHub
- **Database**: Sqlite

### Backend Setup Instructions

- Fork and Clone the repo using
```
$ git clone https://github.com/nakul-19/Blog-Wall.git
```
- Change Branch to `backend` using 
```
$ git checkout backend
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
