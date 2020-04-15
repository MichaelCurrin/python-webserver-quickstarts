# Python Webserver Quickstarts
> Run a "Hello World" webserver in a selection of Python frameworks

This project includes short scripts for basic webservers in various frameworks. These can be used as references for comparison or interest. They can also be run, after installing server-specific dependencies.


## Purpose

- Reference of how to setup a basic server to help with other projects.
- Run each locally as a demo.
- Optionally update it locally to see what changes, like adding an endpoint.


### Approaches

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


### Flask

* A micro-framework with this light and easy to extend with your own code or Flask extensions (separate libraries).
* Great for beginners.

Links:

* [Docs](https://flask.palletsprojects.com/en/master/)
* [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/) guide
* [Tutorial: Building a RESTful API with Flask](https://kite.com/blog/python/flask-restful-api-tutorial/)


### Django

* An opinionated framework that is built to handle a database, templating, admin view and auth. Much heavier than Flask so not 

Links:

* [Home - djangoproject.com](https://djangoproject.com)
* [Getting started](https://www.djangoproject.com/start/) official guide
* [Django Hello World](https://pythonprogramminglanguage.com/django-hello-world/) guide. This was used to create the app in this project.
* [Starting a Django project](https://realpython.com/django-setup/#create-an-app)
* [Django REST](https://www.django-rest-framework.org/tutorial/quickstart/) tutorial
* [Hello World App](https://djangoforbeginners.com/hello-world/) on Django For Beginners site
* [Run Django without a database](http://www.librador.com/2011/05/23/How-to-run-Django-tests-without-a-database/)


### CherryPy

Not as famous as Flask but it is similar and from some research it is supposed to be faster too.

Links:

* [Home - cherrypy.org](https://cherrypy.org/)
* [Tutorials](https://docs.cherrypy.org/en/latest/tutorials.html#)
* [Configure](https://docs.cherrypy.org/en/latest/config.html)


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
- CherryPy
    ```bash
    $ ./cherrypy_hello_world.py
    ```
- Tornado
    ```bash
    $ ./tornado_hello_world.py
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
    $ django_hello_world
    $ python manage.py runserver 5000
    $ # For help on available commands:
    $ python manage.py help
    ```

Press CTRL+C when you want to stop the server.


### View

View the hello world response in the browser.

- http://localhost:5000/


For Django, you also get an admin view.

- http://localhost:5000/admin/


## Resources


See also this site which includes tutorials for Python webserver frameworks - [fullstackpython.com/web-frameworks.html](https://www.fullstackpython.com/web-frameworks.html).



There are the instructions which were followed to create the base Django project initially, before customizing it. So this can be used for 

```bash
$ django-admin startproject <TARGET_DIRECTORY>
$ d <TARGET_DIRECTORY>
$ python manage.py startapp hello
```
