# Python Web server Quickstarts
> Run a "Hello World" webserver in a selection of Python frameworks

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/python-webserver-quickstarts?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/python-webserver-quickstarts/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)

[![dependency - flask](https://img.shields.io/badge/dependency-flask-blue)](https://pypi.org/project/flask)
[![dependency - django](https://img.shields.io/badge/dependency-django-blue)](https://pypi.org/project/django)
[![dependency - cherrypy](https://img.shields.io/badge/dependency-cherrypy-blue)](https://pypi.org/project/cherrypy)
[![dependency - tornado](https://img.shields.io/badge/dependency-tornado-blue)](https://pypi.org/project/tornado)

The library badges above will take you to PyPi if you click them.

This project includes short scripts for basic web servers in various frameworks. These can be used as references for comparison or interest. They can also be run, after installing server-specific dependencies.


## Purpose

- Reference of how to setup a basic server to help with other projects.
- Run each locally as a demo.
- Optionally update it locally to see what changes, like adding an endpoint.


## Approaches

The idea is to cover a mixture of approaches.

- HTML templating
   - Use Jinja or similar templating engine to put data in HTML page and returned the finished result to the client.
   - Model View Controller for more complex project with a database.
- Backend and frontend.
   - Have an API endpoint of JSON data.
   - Setup a page with outline and no data.
   - Pull in the data from the API using JavaScript.


## Frameworks

The scripts in this repo mostly come from quickstart guides on the official docs or blog tutorials.

Whatever framework you choose, you can use it for your hobby or production app but you'll probably want to setup a load balanced like Nginx in front of it. The frameworks tend to recommend this in your docs.

You might also want to reduce resources by implementing caching one of these:

- Database queries (reduce load on database).
- Endpoint or page responses (reduce load on Python app).
- Nginx cache settings.
- Add AWs CloudFront with caching.

### Flask

- A micro-framework with this light and easy to extend with your own code or Flask extensions (separate libraries).
- Great for beginners.
- Build a backend API - handle and return requests typically using RESTful GET and POST endpoints and JSON data.
- Build a templating app.
    - Use a database on the backend and HTML on the frontend.
    - Use the Liquid / Jinja templating engine to read HTML templates and render them using loops and reusable "macros" (functions defined as Liquid).
- Handles connecting to a database like SQLite, MySQL or Postgres. For larger projects, you might want to install a package that you choose as your database ORM - like SQLAlchemy or SQLObject.

Links:

- Flask docs
   - [Homepage](https://flask.palletsprojects.com/en/master/) 
   - [Tutorals](https://flask.palletsprojects.com/en/master/tutorial/) in the Flask docs
   - [Define and Access the Database](https://flask.palletsprojects.com/en/master/tutorial/database/) tutorial on Flask docs.
       > The application will use a SQLite database to store users and posts. Python comes with built-in support for SQLite in the sqlite3 module.
- Tutorials
   - [Retrieving HTML From data using Flask](https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/) tutorial - return data as HTML with `render_template`.
   - [Flask - SQLite](https://www.tutorialspoint.com/flask/flask_sqlite.htm) tutorial on Tutorials Point.
   - [Tutorials point](https://www.tutorialspoint.com/flask/) - including guides for routing, templates, sessions, static files, redirects and more.
- [flask-json](https://flask-json.readthedocs.io/en/latest/) library's docs.
- Flask RESTful library.
   - [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/) docs.
   - [Tutorial: Building a RESTful API with Flask](https://kite.com/blog/python/flask-restful-api-tutorial/)

### Django

- An opinionated framework that is built to handle a database, templating, admin view and auth without installing further libraries yourself.
- Django is not powerful but complex so not beginner-friendly.
- Additional Django libraries are available as replacements to handle things like GraphQL or ecommerce.

Links:

- [Home - djangoproject.com](https://djangoproject.com)
- [Getting started](https://www.djangoproject.com/start/) official guide
- [Django Hello World](https://pythonprogramminglanguage.com/django-hello-world/) guide. This was used to create the app in this project.
- [Starting a Django project](https://realpython.com/django-setup/#create-an-app)
- [Django REST](https://www.django-rest-framework.org/tutorial/quickstart/) tutorial
- [Hello World App](https://djangoforbeginners.com/hello-world/) on Django For Beginners site
- [Run Django without a database](http://www.librador.com/2011/05/23/How-to-run-Django-tests-without-a-database/)

### CherryPy

Not as famous as Flask, but it is similar and from some research it is supposed to be faster too.

Links:

- [Home - cherrypy.org](https://cherrypy.org/)
- [Tutorials](https://docs.cherrypy.org/en/latest/tutorials.html#)
- [Configure](https://docs.cherrypy.org/en/latest/config.html)

### Tornado

Links:

- [Home - tornadoweb.org](https://www.tornadoweb.org/en/stable/index.html#) including quickstart.


## Requirements

- Python >= 3.6


## Installation

Note: This instructions to install and run for a Linux and macOS environments.


Follow this guide to install/update Python and install project dependencies in a new virtual environment using [requirements.txt](/requirements.txt) file.

- [Setup A Python3 Virtual Environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).


## Run

### Start

```bash
$ cd webservers
```

Run a server using one of the commands below. Note that most of the files are executable so do not need as `python` command preceding them.

- No framework
    ```bash
    $ ./no_framework_hello_world.py
    ```
- Flask
    ```bash
    $ # Recommended way.
    $ FLASK_APP=flask_hello_world.py flask run
    $ # This also works:
    $ python flask_hello_world.py
    ```
- Django
    ```bash
    $ cd django_hello_world
    $ python manage.py runserver 5000
    $ # For help on available commands:
    $ python manage.py help
    ```
- CherryPy
    ```bash
    $ cd cherrypy_hello_world
    $ hello_world/main.py

    $ multiple_endpoints/main.py
    ```
- Tornado
    ```bash
    $ ./tornado_hello_world.py
    ```

Press <kbd>CTRL</kbd>+<kbd>C</kbd> when you want to stop the server.

### View

View the hello world response in the browser.

- http://localhost:5000/

For Django, you also get an admin view.

- http://localhost:5000/admin/


## Resources

See also this site which includes tutorials for Python webserver frameworks - [fullstackpython.com/web-frameworks.html](https://www.fullstackpython.com/web-frameworks.html).


There instructions were followed to create the base Django project initially, before customizing it. Run these to get a fresh app setup.

```bash
$ pip install django

$ django-admin startproject hello_app
$ cd hello_app
$ python manage.py startapp hello
```


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
