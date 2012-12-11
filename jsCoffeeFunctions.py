#!/usr/bin/python
# Filename: jsCoffeeFunctions.py

import re
from subprocess import PIPE
from subprocess import Popen

def coffee2js(string):
    string = prepareCoffee(string)
    p = Popen(['coffee', "-ecb", string], stdin = PIPE, stdout = PIPE, stderr = PIPE)
    stdout, stderr = p.communicate()
    stdout = removeComments(stdout)
    return stdout, stderr

def prepareCoffee(string):
    string = re.sub("[A-z\d]+ = undefined", '', string)
    string = removeComments(string)
    string = string.strip(" \t\n\r")
    return string

def prepareJs(string):
    string = removeComments(string)
    string = re.sub("var [A-z\d\,\s]+\n", '', string)
    string = re.sub("\n[\S\d\, ]+ = void 0;", '', string)
    string = string.strip(" \t\n\r")
    return string

def js2coffee(string):
    p = Popen(['js2coffee', '-X'], stdin = PIPE, stdout = PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(prepareJs(string))
    return stdout, stderr 

def removeComments(string):
    return re.sub("//[\S\d\. ]+\n", '', string)