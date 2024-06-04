#!/usr/bin/python 
# To Do List Manager for OSX 
# 
# Casey IT LLC
# 4-4-11


from __future__ import with_statement
import sys
import os
import fileinput



os.system('clear')

print ("##############          TO DO LIST       ############")
print ("##############                           ############")

def showlist():
        os.system('clear')
        print ("############  Current To Do List  ######")
        print ("########################################")
    
        get_list = open('todo.txt')
	entire_list = get_list.readlines()
	for i in range (len(entire_list)):
		print i, entire_list[i]
        get_list.close()
        print ("########################################")
        print ("########################################")

def appendlist():
	 print ("#######################################")
         print ("#######################################")

	 
	 addtolist = str( raw_input("Enter new item:  \n"))
         thelist = open('todo.txt', 'a')
         thelist.write(str(addtolist))
	 thelist.write(str('\n'))
         thelist.close()	 
	 showlist()


def deleteitem():
	showlist()
	
	with open("todo.txt") as f:
            lines = f.readlines()
            if len(lines) == 0:  
                return  
	prompt = "Enter number to delete , or '0' to abort: "
	while True:
            input = raw_input(prompt)
            try:
                input = int(input, 10)
            except ValueError:
                print "Invalid input."
            else:
                if 0 <= input <= len(lines):
                    break
                print "Input out of range."
	if input == 0:
              return
        
	lines[input] = "" 

        with open("todo.txt", "w") as f:
            f.writelines(lines)

	showlist()

while True:

	askme = raw_input("\nDo you want to:\n(S)ee list\n(A)ppend list\n(D)elte from list\n(Q)Quit?\n")
	print str('\n')

	if askme == "S":
		showlist()
	elif askme == "A":
		appendlist()
	elif askme == "D":
		deleteitem()

	elif askme == "Q":
		sys.exit()
	else: 
		print ("Try again?")
	
print ("#######################################")
print ("#######################################")



