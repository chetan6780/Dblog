# GoCardless sample application

## Pre-setup
Create a new folder anywhere on your system
open terminal in this new folder

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/chetan6780/Django-blog.git
$ cd Django-blog
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ .\env\Scripts\activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
The blog application should be running on `http://127.0.0.1:8000/`