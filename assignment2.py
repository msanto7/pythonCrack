#Assignment #2 Password Cracker

#mcrypt 
#use a small english dictionary to crack the password
#Arguements --> 1. Shadow File  2. Username 
#Returns    --> 1. Password 

#if user does not exist print warning 
#if password is not in dictionary print that 

#################################################################

#Reqeuest Username

input("\nPlease enter a username: \n")

#Use shadow file to find check if this user name exists

#if username does not exist print and exit

#if the username exists run the dictionary and compare hashes to the one from shadow

      #if a match is found print the password 
print("The Password is: " )

      #else if (no match)
print("Password not in Dictioanry. ")



