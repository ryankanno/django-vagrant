#!/usr/bin/env python
# coding: utf-8
import os
import sys
import subprocess
from subprocess import Popen

from jinja2 import Environment, PackageLoader
from subprocess import Popen
env = Environment(loader=PackageLoader('ixxy', 'templates'))


FILES = (
    'passwords.py',
    'settings_local.py',
)

def mysql(command):
    return Popen('echo "{command}" | mysql -u root'.format(command=command),
        shell=True)


def generate(path, project_path):
    print(u'Generating {}'.format(path))
    template = env.get_template(path)
    data = template.render(project=project)
    with open(os.path.join(project_path, 'myproject', path), 'w') as f:
        f.write(data)


def main(project, project_path):
    print "VIRTUALENV IS HERE", os.environ.get('VIRTUAL_ENV')
    python = os.path.join(os.environ.get('VIRTUAL_ENV', '/usr'), 'bin', 'python')
    print python
    print("Initialising local files for {}".format(project))
    for path in FILES:
        generate(path, project_path)
    print('Deleting old database...')
    db_create = mysql('DROP DATABASE {}'.format(project))
    print('Creating database...')
    db_create = mysql('CREATE DATABASE {}  CHARACTER SET utf8'.format(project))
    db_create.wait()
    print('Syncing DB...')
    syncdb = Popen([
            python,
            '{project_path}/myproject/manage.py'.format(project_path=project_path),
            'syncdb',
            '--noinput',
        ],
        stdout=subprocess.PIPE, stdin=subprocess.PIPE,)
    syncdb.wait()
    print('Migrating fixtures...')
    migrate = Popen([
            python,
            '{project_path}/myproject/manage.py'.format(project_path=project_path),
            'migrate',
        ],
        stdout=subprocess.PIPE, stdin=subprocess.PIPE,)
    migrate.wait()
    print('Initialising CMS...')
    initcms = Popen([
            python,
            '{project_path}/myproject/manage.py'.format(project_path=project_path),
            'init_cms',
        ],
        stdout=subprocess.PIPE, stdin=subprocess.PIPE,)
    initcms.wait()

    print('Your username is be "admin" and password is "admin".')



if __name__ == '__main__':

    project_path = os.getcwd()
    project = project_path.split('/')[-1]

    main(project, project_path)