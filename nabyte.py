#!/usr/bin/python
# -*- coding: utf-8 -*-
import mechanize
import random
import sys
import os
def clear():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")
clear()
def logo():
    print ('''
   ▄   ██   ███ ▀▄    ▄   ▄▄▄▄▀ ▄███▄   
    █  █ █  █  █  █  █ ▀▀▀ █    █▀   ▀  
██   █ █▄▄█ █ ▀ ▄  ▀█      █    ██▄▄    
█ █  █ █  █ █  ▄▀  █      █     █▄   ▄▀ 
█  █ █    █ ███  ▄▀      ▀      ▀███▀   
█   ██   █   Anonymous File Hosting                           
        ▀    IRC: irc.nabyte.com                           
''')
logo()
def instr():
    print ('''nabyte.py <file> <opt hist key>''')
try:
    filename = str(sys.argv[1])
    try:
        hist_key = str(sys.argv[2])
        hist = True
    except:
        hist = False
except:
    instr()
    exit(0)
def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
    return random.choice(uastrings)
br = mechanize.Browser()
br.addheaders = [('User-agent', GET_UA())]
br.set_handle_robots(False)
br.set_handle_redirect(mechanize.HTTPRedirectHandler)
if hist == True:
    br.addheaders = [('Cookie','rez='+hist_key)]
br.open("https://nabyte.com")
br.select_form(nr=0)
br.form.add_file(open(filename), 'text/plain', filename)
print ('Uploading...\n\n')
req = br.submit()
clear()
logo()
for link in br.links():
    if str(filename) in str(link):
        pr = str(link)
        if hist == True:
            print ('Uploaded to -> '+hist_key)
        print ('Size: '+str(os.path.getsize(str(filename)))+' Bytes')
        print ("URL: 'https://nabyte.com/"+ pr.replace("Link(base_url=u'https://nabyte.com/u', url=u'", '').replace("', text=u'",'  ').replace("',  ",'').replace("tag=u'a', attrs=[(u'style', u'color:lime'), (u'href', u'upload/", '\nFilename: ').replace("')])",''))
    else:
        pass
