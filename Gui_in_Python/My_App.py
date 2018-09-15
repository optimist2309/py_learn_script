#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 00:07:58 2018

@author: optimist2309
"""
import webbrowser
import tkinter

def glasdoor_launcher():
    chrome_path = '/usr/bin/google-chrome %s'
    url = 'https://www.glassdoor.co.in/Reviews/index.htm'
    webbrowser.get(chrome_path).open(url)
    
def udemy_launcher():
    chrome_path = '/usr/bin/google-chrome %s'
    url = 'https://www.udemy.com/'
    webbrowser.get(chrome_path).open(url)
    
def quora_launcher():
    chrome_path = '/usr/bin/google-chrome %s'
    url = 'https://www.quora.com/'
    webbrowser.get(chrome_path).open(url)
    
def gmail_launcher():
    chrome_path = '/usr/bin/google-chrome %s'
    url = 'https://mail.google.com'
    webbrowser.get(chrome_path).open(url)

def linkedin_launcher():
    chrome_path = '/usr/bin/google-chrome %s'
    url = 'https://www.linkedin.com'
    webbrowser.get(chrome_path).open(url)
    
def angel_co_launcher():
    chrome_path = '/usr/bin/google-chrome %s'
    url = 'https://angel.co/'
    webbrowser.get(chrome_path).open(url)


def github_launcher():
    chrome_path = '/usr/bin/google-chrome %s'
    url = 'https://github.com/optmist2309'
    webbrowser.get(chrome_path).open(url)

def geeks_for_geeks_launcher():
    chrome_path = '/usr/bin/google-chrome %s'
    url = 'https://www.geeksforgeeks.org/python-programming-language/'
    webbrowser.get(chrome_path).open(url)

gui_root = tkinter.Tk()
gui_root.title("Be Productive")
gui_root.minsize(400 ,200)

#glassdoor_icon = tkinter.PhotoImage(file="/home/optimist2309/Pictures/glassdoor-logo.png")
glassdoor_button = tkinter.Button(gui_root, text = "Glassdoor",command = glasdoor_launcher)
glassdoor_button.place(x = 20 , y = 30)

Udemy_button = tkinter.Button(gui_root,  text = "Udemy", command = udemy_launcher)
Udemy_button.place(x = 115 , y = 30)

Quora_button = tkinter.Button(gui_root, text = "Quora", command = quora_launcher)
Quora_button.place(x = 195 , y = 30)

Gmail_button = tkinter.Button(gui_root, text = "Gmail", command = gmail_launcher)
Gmail_button.place(x = 265 , y = 30)

Linkedin_button = tkinter.Button(gui_root, text = "Linkedin", command = linkedin_launcher)
Linkedin_button.place(x = 20 , y = 70)

Angle_co_button = tkinter.Button(gui_root, text = "AngelList", command = angel_co_launcher)
Angle_co_button.place(x = 110 , y = 70)

Github_button = tkinter.Button(gui_root, text = "Github", command = github_launcher)
Github_button.place(x = 200 , y = 70)

Geeks_for_geek_button = tkinter.Button(gui_root, text = "Python Tuts", command = geeks_for_geeks_launcher)
Geeks_for_geek_button.place(x = 280 , y = 70)

gui_root.mainloop()