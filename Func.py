#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/12/30'


import os
import io
import sys
from time import sleep
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import configparser as ConfigParser


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
PATH = sys.path[0]


def default_setting():
    config = ConfigParser.ConfigParser()
    config.optionsxform = str
    config.read(PATH + '/config.cfg')
    if not config.has_section('DEFAULTSETTING'):
        config.add_section('DEFAULTSETTING')
    if not config.has_option('DEFAULTSETTING','index'):
        config.set('DEFAULTSETTING','index','1')
    config.write(open(PATH + '/config.cfg','w'))


def update_setting():
    config = ConfigParser.ConfigParser()
    config.optionsxform = str
    config.read(PATH + '/config.cfg')
    INDEX = config.getint('DEFAULTSETTING','index')
    INDEX += 1
    config.set('DEFAULTSETTING','index',str(INDEX))
    config.write(open(PATH + '/config.cfg','w'))
    return INDEX


def test():
    # update_setting()
    # print(INDEX)

    # _request = request.Request(SOURCE)
    # response = request.urlopen(_request)

    # print(response.read())
    pass


default_setting()
config = ConfigParser.ConfigParser()
config.read(PATH + '/config.cfg')
INDEX = config.getint('DEFAULTSETTING','index')
