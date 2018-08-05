                                                  DJANGO-BLOG


A Blogging WebApplication made using Django Web Framework and Python:-

App Features:

1)User Registration,Login,Change and Reset Password.

2)Create, Read, Update and Delete posts (Update and Delete feature only for post author).

3)Users can comment on the post.

4)Chat Room for users.

5)Admin Dashboard.

6)User Profile page.


Major Package Versions:

1)Python = 3.5.3

2)Django = 1.11.4

3)redis==2.10.6 

(whole list provided in requirements.txt)


App Requirements:


1.pip install -r requirements.txt

or use virtual environment(ven):  source ven/bin/activate


2.To run redis server:  sudo docker run -p 6379:6379 -d redis:2.8

(redis server allows asynchronous communication)


3.To run development server: python manage.py runserver


(after running virtual environment)
