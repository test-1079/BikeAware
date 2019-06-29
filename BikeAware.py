#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os
import subprocess
import time

from termcolor import colored

from pyfiglet import Figlet
f = Figlet(font='slant')

sel = 0
run = 1

con = lite.connect('BikeAware.db')
cur = con.cursor()

while run == 1:
    os.system("clear")
    while sel == 0:
	print("")
	print colored(f.renderText("Bike Aware"), 'green')
	print("")
	print colored("A Spatially Intelligent Cycling Safety Program", 'cyan')
	print colored("Type a selection (i.e. 1,2,3)", 'cyan')
	print("")
        sel = input ("1. Enter Bike ID & Track Name\n2. View Participants\n3. Delete Record\n")
	print("")

    while sel == 1:
    
		MyOut10 = subprocess.Popen(["rm", "-rf", "ba"], 
           	stdout=subprocess.PIPE, 
           	stderr=subprocess.STDOUT)
		stdout,stderr = MyOut10.communicate()
		
		MyOut11 = subprocess.Popen(["rm", "-rf", "BikeAware.db"], 
           	stdout=subprocess.PIPE, 
           	stderr=subprocess.STDOUT)
		stdout,stderr = MyOut11.communicate()
		
		MyOut1 = subprocess.Popen(["git", "clone", "https://github.com/test-1079/ba.git"], 
           	stdout=subprocess.PIPE, 
           	stderr=subprocess.STDOUT)
		stdout,stderr = MyOut1.communicate()
		
		MyOut3 = subprocess.Popen(["mv", "ba/BikeAware.db", "BikeAware.db"], 
           	stdout=subprocess.PIPE, 
           	stderr=subprocess.STDOUT)
		stdout,stderr = MyOut3.communicate()
		
        	os.system("clear")
        	ssid = input("Type the SSID name of you wifi hotspot...\n")
    		time.sleep(3)
    		track = input("Type in Track Name...\n")
        	params = (ssid, track)	
        	cur.execute("INSERT INTO BikeAware VALUES (NULL, ?, ?, CURRENT_TIMESTAMP)", params)

        	with con:
            		sql2 = '''SELECT Count(*) FROM BikeAware'''
            		cur.execute(sql2)
            	rows = cur.fetchall()
            	for row in rows:
                	text = row
                	str(text)
                	row[2:1]
        		print text
		
        		MyOut4 = subprocess.Popen(["mv", "BikeAware.db", "ba/BikeAware.db"], 
           		stdout=subprocess.PIPE, 
           		stderr=subprocess.STDOUT)
			stdout,stderr = MyOut4.communicate()
		 
        		MyOut2 = subprocess.Popen(["git", "push", "-f", "origin", "master"], 
           		stdout=subprocess.PIPE, 
           		stderr=subprocess.STDOUT)
			stdout,stderr = MyOut2.communicate()
		
			print stdout         

		print("")
		print colored(f.renderText("Bike Aware"), 'green')
		print("")
		print colored("A Spatially Intelligent Cycling Safety Program", 'cyan')
		print colored("Type a selection (i.e. 1,2,3)", 'cyan')
		print("")
        	sel = input ("1. Enter Bike ID & Track Name\n2. View Participants\n3. Delete Record\n")
		print("")

    while sel == 2:
    
		MyOut5 = subprocess.Popen(["git", "clone", "https://github.com/test-1079/ba.git"], 
			stdout=subprocess.PIPE, 
			stderr=subprocess.STDOUT)
		stdout,stderr = MyOut5.communicate()
			
		MyOut6 = subprocess.Popen(["mv", "ba/BikeAware.db", "BikeAware.db"], 
			stdout=subprocess.PIPE, 
			stderr=subprocess.STDOUT)
		stdout,stderr = MyOut6.communicate()
        
    		with con:
    		    """sql1 = '''SELECT * FROM BikeAware WHERE date > datetime(current_timestamp,'localtime', 'start of day', 'weekday 6', '-7 day')'''"""
    		    sql1 = '''SELECT * FROM BikeAware ORDER BY id DESC LIMIT 7'''
    		    cur.execute(sql1)
    		    rows = cur.fetchall()
    		    for row in rows:
    		        print row
    		    print len(rows)
   			
   		print("")
		print colored(f.renderText("Bike Aware"), 'green')
		print("")
		print colored("A Spatially Intelligent Cycling Safety Program", 'cyan')
		print colored("Type a selection (i.e. 1,2,3)", 'cyan')
		print("")
    		sel = input ("1. Enter Bike ID & Track Name\n2. View Participants\n3. Delete Record\n")
		print("")

    while sel == 3:
    
   		MyOut7 = subprocess.Popen(["git", "clone", "https://github.com/test-1079/ba.git"], 
    		stdout=subprocess.PIPE, 
    		stderr=subprocess.STDOUT)
		stdout,stderr = MyOut7.communicate()
			
		MyOut8 = subprocess.Popen(["mv", "ba/BikeAware.db", "BikeAware.db"], 
    		stdout=subprocess.PIPE, 
    		stderr=subprocess.STDOUT)
		stdout,stderr = MyOut8.communicate()
    
        	os.system("clear")
        	enterdelete = input("Enter record id number to delete...\n")
        	cur.execute("DELETE FROM BikeAware WHERE id='%s'" % enterdelete)
        	con.commit
        	os.system("clear")
    		
		print("")
		print colored(f.renderText("Bike Aware"), 'green')
		print("")
		print colored("A Spatially Intelligent Cycling Safety Program", 'cyan')
		print colored("Type a selection (i.e. 1,2,3)", 'cyan')
		print("")
		sel = input ("1. Enter Bike ID & Track Name\n2. View Participants\n3. Delete Record\n")
		print("")
