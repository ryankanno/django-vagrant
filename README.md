#Django-Vagrant

This is a Vagrant instance to help you get started with the
[Django](https://www.djangoproject.com/) framework. It's been configured to
work in conjunction with the [fabfile](https://github.com/ryankanno/django-skeleton/blob/master/fabfile.py)
from [django-skeleton](http://github.com/ryankanno/django-skeleton/).  By
cloning this repository, you'll quickly have a playground environment to play
around with the Django framework.


##Features 

* puppet provisioned
* nginx
* uwsgi
* git
* virtualenv


##Install

* `git clone http://github.com/ryankanno/django-vagrant`
* `vagrant init`
* `vagrant up`
* `vagrant provision`

To actually dig into the weeds of the box, run the following:

* `vagrant ssh`
