#Django-Vagrant

This is a Vagrant Ubuntu instance to help you get started with the
[Django](https://www.djangoproject.com/) framework. It's been configured to
work in conjunction with the [fabfile](https://github.com/ryankanno/django-skeleton/blob/master/fabfile.py)
from [django-skeleton](http://github.com/ryankanno/django-skeleton/).  By
cloning this repository, you'll quickly have a playground environment to play
around with the Django framework.


##Features 

Ubuntu 12.04 LTS

[Puppet](http://puppetlabs.com) provisioned:

* nginx
* uwsgi
* mysql 
* git
* hg
* virtualenv


##Install

* `git clone http://github.com/ryankanno/django-vagrant`
* `git submodule update --init`
* `vagrant up`
* `vagrant provision` (to reset password using libshadow)

To actually dig into the weeds of the box, run the following:

* `vagrant ssh`

##Details

* creates a user (django/django)
