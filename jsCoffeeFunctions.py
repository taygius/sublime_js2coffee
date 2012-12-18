#!/usr/bin/python
# Filename: jsCoffeeFunctions.py

import re
from subprocess import PIPE, Popen

def coffee2js(string):
    p = Popen(['coffee', "-ecb", prepareCoffee(string)], stdin = PIPE, stdout = PIPE, stderr = PIPE)
    stdout, stderr = p.communicate()
    stdout = removeComments(stdout)
    return stdout, stderr

def prepareCoffee(string):
    string = re.sub("[A-z\d]+ = undefined", '', string)
    return removeComments(string).strip(" \t\n\r")

def prepareJs(string):
    string = removeComments(string)
    return re.sub("\n[\S\d\, ]+ = void 0;", '', string).strip(" \t\n\r")

def prepareJsBefore(string):
    return re.sub("(var[\w\s\,]+\;)(?:\b|\n|$)", '', prepareJs(string))

def js2coffee(string):
    p = Popen(['js2coffee', '-X'], stdin = PIPE, stdout = PIPE, stderr=PIPE)
    return p.communicate(prepareJsBefore(string))

def removeComments(string):
    return re.sub("//[\S\d\. ]+\n", '', string)