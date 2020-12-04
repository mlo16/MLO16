from fabric.api import *
'''
OPS435 Assignment 2S - Fall 2020
Program: a2s_mlo16.py
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
    list1 = []
    for i in status:
        list1.append(i)
    s = ''.join(list1)
    list2 = s.split()
    print(list2)


def listSysUser():
    '''return a list of system (non-shell) user'''
    command = 'awk -F: \'$7 !~ /bash$/{print $1}\' /etc/passwd'
    status = run(command)
    list1 = []
    for i in status:
        list1.append(i)
    s = ''.join(list1)
    list2 = s.split()
    print(list2)


def findUser(username):
    '''find user with a given user name'''
    command = 'getent passwd ' + username
    try:
        status = run(command)
        print('Found user '+ username + ' on the system.')
    except:
        print('User ' + username + ' is not on the system.')
