Python Crack - Michael Santoro 
---------------------------------------
--> This is a python script for cracking linux user passwords using the shadow file and a dictionary attack.

GETTING STARTED
---------------------------------------- 
-Begin by cloning this repository into the root directory and installing the necessary dependencies below.
  Any linux distrobution is recommened.
    
    Linux Command: sudo su
    Linux Command: cd /
    Linux Command: git clone https://github.com/msanto7/pythonCrack.git
    Linux Command: cd /pythonCrack/python
 
----------------------------------------

DEPENDENCIES 
-----------------------------------------
-This program will require the host system to have any version of [Python](https://www.python.org/) installed. 
    
    Linux Command: sudo apt-get install python

    Linux Command: python --version       -->used to check if python is installed 

-Linux is the ideal operating system for this program based on the use of the /etc/shadow file, 
 however it can be executed on a Windows or Mac operating system that has python and a path to 
 a local path to a linux shadow file. I will provide the commands for setup and execution based
 on an assumption of a linux host. 

-----------------------------------------

RUN THE APPLICATION
----------------------------------------
-To execute the program, we will need to run the assignmen2.py file in the python folder. 
-Open a linux command prompt and use the, cd and ls commands to have the working directory 
 be the python folder in this cloned project.

    Linux Command: cd /pythonCrack/python
 
-Use the command below to run the program 

    Linux Command: python assignment2.py

-The program will prompt for 2 parameters, first the path to your shadow file. By default
 for a linux system you can enter the path "/etc/shadow", however if on another operating
 you will have to have a copied shadow file and the appropriate path. For the username choose
 any of the listed linux users.

-After pressing enter, the program will begin to search the shadow file and our dictionary that 
 is provided. If the password is in our dictionary file...it will be printed to the console when 
 found. Otherwise you will be notified that the password does not exist in our english dictionary. 

---------------------------------------

TESTING
----------------------------------------
-To test the functionality of this program add a new user...and manipulate their password. 

  Create new user
    Linux Command: adduser <enterusername>

-If you set the password to an english word you will find that the password cracker 
 successfully finds the password

Note: use passwords that start with the letter "a" to expediate testing time. 
