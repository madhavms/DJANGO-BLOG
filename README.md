                                                  DJANGO-BLOG

A Blog Project has been implemented with user authentiction and facility to create posts and other CRUD features(CRUD:Create Read Update Delete) and make comments.

A Chat feature using channels is also provided as a separate project with redirects to and from the Blog.

Requirements:
BLOG_PROJECT:

1.pip install -r blog_requirements.txt            

or use virtual environment:  source ven/bin/activate

2.To run development server: python manage.py runserver

CHAT_PROJECT:

1.pip install -r chat_requirements.txt            

or use virtual environment:  source env/bin/activate

2.To run redis server:       sudo docker run -p 6379:6379 -d redis:2.8

(redis server allows asynchronous communication)

3.To run development server:  python manage.py runserver 5000 

