from fabric.api import *
'''
OPS435 Assignment 2S - Fall 2020
Program: a2r_mlo16.py
Author: Mitchell Lo
The python code in this file a2s_mlo16.py is original work written by
Mitchell Lo. No code in this file is copied from any other source
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and violators
will be reported and appropriate action will be taken.
'''

env.hosts =['myvmlab.senecacollege.ca']
env.user = "student"
env.port = '7424'


def addUser(username):
    '''add a user with given user name to remote system'''
    command = 'useradd ' + username
    status = sudo(command)
    print(status)


def listUser():
    '''return a list of shell user on a remote system'''
    command = 'awk -F: \'/bash$/{print $1}\' /etc/passwd'
    status = run(command)
    l1 = []
    for i in status:
        l1.append(i)
    s = ''.join(l1)
    l2 = s.split()
    print(l2)


def listSysUser():
    '''return a list of system (non-shell) user'''
    command = 'awk -F: \'$7 !~ /bash$/{print $1}\' /etc/passwd'
    status = run(command)
    l1 = []
    for i in status:
        l1.append(i)
    s = ''.join(l1)
    l2 = s.split()
    print(l2)


def findUser(name):
    '''find user with a given user name'''
    command = 'getent passwd ' + name
    try:
        status = run(command)
        print('Found user '+ name + ' on the system.')
    except:
        print('User ' + name + ' is not on the system.')
