# Webserver Quickstarts - Python
> Run a "Hello World" webserver in a choice of Python frameworks

This project includes short scripts for basic webservers in various frameworks. These can be used as references for comparison or interest. They can also be run, after installing dependencies.


## Frameworks

The scripts in this repo mostly come from quickstart guides on the official docs or blog tutorials. See links below.

- CherryPy
    * [Home](https://cherrypy.org/)
    * [Tutorials](https://docs.cherrypy.org/en/latest/tutorials.html#)
    * [Configure](https://docs.cherrypy.org/en/latest/config.html)
- Tornado
    - [Home and quickstart](https://www.tornadoweb.org/en/stable/index.html#)
- Flask
    * [Home](https://www.fullstackpython.com/flask.html)
    * [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/) guide
    * [Tutorial: Building a RESTful API with Flask](https://kite.com/blog/python/flask-restful-api-tutorial/)
- Django
    * [Getting started](https://www.djangoproject.com/start/) official guide
    * [Django Hello World](https://pythonprogramminglanguage.com/django-hello-world/) guide, without using a database
    * [Starting a Django project](https://realpython.com/django-setup/#create-an-app)
    * [Django REST](https://www.django-rest-framework.org/tutorial/quickstart/) tutorial
    * [Hello World App](https://djangoforbeginners.com/hello-world/) on Django For Beginners site
    * [Run Django without a database](http://www.librador.com/2011/05/23/How-to-run-Django-tests-without-a-database/)


## Installation

Note: This instructions to install and run for a Linux and Mac environments.


Required:
- Python 3.6+

Follow this guide to install/update Python and install project dependencies - [Setup A Python3 Virtual Environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).


To setup your Django project:

```bash
$ django-admin startproject TARGET_DIRECTORY
```

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
    $ python manage.py startapp hello
    ```

Press CTRL+C when you want to stop the server.


### View

Open http://localhost:5000/ in the browser.
