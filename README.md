# Clean python installation 

List python libraries installed already

    $ pip3 freeze

Install virtual environment for python

    $ pip3 install virtualenv

Call virtual environnement and create a folder 'venv' with a fresh python installation

    $ virtualenv venv --python=python3

Enter virtual environment

    $ source venv/bin/activate

Check the virtual environment version

    (venv) $ python --version
    Python 3.8.3

Quit virtual environment

    (venv) $ deactivate

Check the version outside the virtual environment

    $ python --version
    Python 2.7.16

Go back on venv and install the Flask-RESTful library

    $ source venv/bin/activate
    (venv) $ pip install Flask-RESTful
    Collecting Flask-RESTful
    Downloading Flask_RESTful-0.3.8-py2.py3-none-any.whl (25 kB)
    Collecting six>=1.3.0
    Using cached six-1.15.0-py2.py3-none-any.whl (10 kB)
    Collecting aniso8601>=0.82
    Downloading aniso8601-8.0.0-py2.py3-none-any.whl (43 kB)
        |████████████████████████████████| 43 kB 1.5 MB/s
    Collecting Flask>=0.8
    Using cached Flask-1.1.2-py2.py3-none-any.whl (94 kB)
    Collecting pytz
    Using cached pytz-2020.1-py2.py3-none-any.whl (510 kB)
    Collecting Jinja2>=2.10.1
    Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
    Collecting click>=5.1
    Using cached click-7.1.2-py2.py3-none-any.whl (82 kB)
    Collecting itsdangerous>=0.24
    Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
    Collecting Werkzeug>=0.15
    Using cached Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
    Collecting MarkupSafe>=0.23
    Using cached MarkupSafe-1.1.1-cp38-cp38-macosx_10_9_x86_64.whl (16 kB)
    Installing collected packages: six, aniso8601, MarkupSafe, Jinja2, click, itsdangerous, Werkzeug, Flask, pytz, Flask-RESTful
    Successfully installed Flask-1.1.2 Flask-RESTful-0.3.8 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 aniso8601-8.0.0 click-7.1.2 itsdangerous-1.1.0 pytz-2020.1 six-1.15.0

List the libraries installed

    (venv) $ pip freeze
    aniso8601==8.0.0
    click==7.1.2
    Flask==1.1.2
    Flask-RESTful==0.3.8
    itsdangerous==1.1.0
    Jinja2==2.11.2
    MarkupSafe==1.1.1
    pytz==2020.1
    six==1.15.0
    Werkzeug==1.0.1

Initialize repository on code dir

    $ cd code
    $ git init
    $ touch .gitignore 
        > .DS_Store
        > __pycache__
        > *.pyc
    $ git status
    $ git add .
    $ git commit -m "First commit, basics python-flask rest API with stores, items and user authentication"

Create repo on github

git@github.com:fbrcode/py-flask-rest-api.git