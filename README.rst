
This is SQL version modified of Project Enferno (use NoSQL)

Change from Enferno:
-------------------
* Move database from MongoEngine to Flask-SqlAlchemy
* Integrate base Front-end use Bootstrap, Navigation Responsive, already for run production your website.


=========================

Tutorials from Enferno
-------------

* First steps: create your first website with Enferno : https://medium.com/project-enferno/moonwalking-with-project-enferno-402937628745
* Customize your website : https://medium.com/project-enferno/moonwalking-with-project-enferno-part-2-9a23d39af55a
* Create a simple blog in 5 minutes: https://medium.com/project-enferno/create-a-simple-blog-in-5-min-using-project-enferno-be359ae77788?source=1
* Create a comic website with Enferno in 7 min: https://medium.com/project-enferno/create-a-comic-website-in-7-min-using-project-enferno-6c838c1e2742?source=1
* How to use background tasks and Mail in Enferno : https://medium.com/project-enferno/create-your-first-minion-with-project-enferno-f7884aa95443?source=1
* Deploy your Enferno project on Ubuntu in a minute: https://medium.com/project-enferno/tip-deploy-enferno-framework-on-ubuntu-with-a-single-command-cc1a596ec3f7
* How to deploy Enferno on Heroku: https://medium.com/project-enferno/deploy-your-enferno-website-on-heroku-for-free-810326f0aaa
* YOOO: a url shortener built with Enferno: https://medium.com/project-enferno/introducing-yooo-a-url-shortener-api-based-on-enferno-framework-823bdc2afa05?source=1


Prerequisites
-------------

* MySql
* Redis (optional for cache)
* Python Imaging (jpeg/png) support if you would like to work with images
* Node.js and npm (optional for front-end stuff)

Quickstart
----------
::

    $ git clone https://github.com/loctv/flask-server-starter.git
    
    $ cd flask-server-starter
    
    $ virtualenv env
    
    $ source env/bin/activate 
    
    $ pip install -r requirements.txt

    $ npm install

After that, you should create your admin user, run the following command:
::

    $ ./manage.py install

and follow the instructions, this will create your first user and first admin role.


Edit the settings.py and change the settings to suit your needs, sepcifically you can change Flask security settings, security keys, Mongodb settings,and Flask mail.

to run the system, you can use a management command:
::

    $ ./manage.py server

    and

    $ gulp
    

Features
--------
- Flask based
- Fully working user registration and authentication + user roles via Flask security and Flask Principal
- Memory caching via Redis/Memcached and Flask cache
- Simple admin backend via Flask Admin
- Command line scripting via Flask Script (will be replaced by "click" in the next release)
- Automatic assets bundling, minification and sass support via gulp
- MySQL and SqlAlchemy ORM
- Background tasks via Celery
- Email integration via Flask Mail
- Best practices by utilizing Flask blueprints and development/production configuration


Inspiration & Credits
---------------------

- `Cookiecutter Flask <https://github.com/sloria/cookiecutter-flask>`_
- `Flask Security <https://pythonhosted.org/Flask-Security/>`_
- `Flask-SqlAlchemy <http://flask-sqlalchemy.pocoo.org/2.1/>`_
- `Flask WTF <https://flask-wtf.readthedocs.org/en/latest/>`_
- `Flask Admin <https://github.com/mrjoes/flask-admin/>`_
- `Celery Task Queue <http://www.celeryproject.org/>`_
- `Redis <http://redis.io/>`_
- `Flask Mail <https://pythonhosted.org/flask-mail/>`_
- `Flask Documentation <http://flask.pocoo.org/docs/>`_
- `Celery Task Queue <http://www.celeryproject.org/>`_


License
-------

MIT licensed.

