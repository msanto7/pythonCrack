#Assignment #2 Password Cracker

#mcrypt 
#use a small english dictionary to crack the password
#Arguements --> 1. Shadow File  2. Username 
#Returns    --> 1. Password 

#if user does not exist print warning 
#if password is not in dictionary print that 

#################################################################
import pwd, grp
import crypt 

#Reqeuest Username

#print("Users: \n")
#print()
#for p in pwd.getpwall():
#    print p[0], grp.getgrgid(p[3])[0]


def checkDictionary(passwdHash, dictionary):
    salt = passwdHash[0:11]
    file = open(dictionary, 'r')
    for word in file.readlines():
        word = word.strip('\n')
        wordHash = crypt.crypt(word, salt)
        if (wordHash == passwdHash):
            print "[+] Found Password: " + word + "\n"
            return

    print "Password is not in the dictionary.\n"
    return


def main():
    shadow = open("/etc/shadow", 'r')
    uName = raw_input("\nPlease enter a username from the list of users: \n")
    print(uName)

    for line in shadow.readlines():
        if ":" in line:
            uName = line.split(":")[0]
            passwdHash = line.split(":")[1].strip(" ") 
            print ("Username  " + uName + " is being processed")
            checkDictionary(passwdHash, "/msanto7/cracklib-small")

if __name__ == '__main__' :
    main()


#Use shadow file to find check if this user name exists

#if username does not exist print and exit

#if the username exists run the dictionary and compare hashes to the one from shadow

      #if a match is found print the password 
#print("The Password is: " )

      #else if (no match)
#print("Password not in Dictioanry. ")



                                                                      
