#Assignment #2 Password Cracker
#Michael Santoro 

#mcrypt 
#use a small english dictionary to crack the password
#Arguements --> 1. Shadow File  2. Username 
#Returns    --> 1. Password 

#if user does not exist print warning 
#if password is not in dictionary print that 

#################################################################
import pwd
import crypt 

##############################################
def checkDictionary(passwdHash, dictionary):
    salt = passwdHash[0:11]          #this is actually the salt and the encryption method id...
                                     #this allows the crypt functions to recognize the encryption method 
    file = open(dictionary, 'r')

    for word in file.readlines():
        word = word.strip('\n')       #parse wordlist

        wordHash = crypt.crypt(word, salt) #encrypt word and compare to the shadow file hash
        if (wordHash == passwdHash):
            print "Password: " + word + "\n"
            return

    print "Password is not in the dictionary.\n"
    return


#####################################33
def main():

    #accept and open shadow file
    shadowPath = raw_input("Please enter the path to your shadow file: \n ")
    try:
        shadow = open(shadowPath, 'r')
    except IOError:
        print("File could not be opened. ")
        return
    #print linux usernames 
    i = 1
    for p in pwd.getpwall():
        print "    ", p[0],
        if (i % 5 == 0):     #formatting
            print "\n"
        i = i + 1

    #accept and search for username
    uName = raw_input("\nPlease enter a username from the list of users: \n")

    for line in shadow.readlines():
        if ":" in line:    #shadow file is split by colons 
            tempU = line.split(":")[0]  #store to compare to user input 
            if (uName == tempU):
                passwdHash = line.split(":")[1].strip(" ") 
                print ("Username: " + uName + " has been found. Cracking Password...")
                checkDictionary(passwdHash, "/pythonCrack/wordlist/cracklib-small")   #this dictionary is hard coded so make sure the path will work when downloaded 
                return
    #if no user name matches 
    print("Username is invalid.")
    return
#start main function

if __name__ == '__main__' :
    main()

##############################################

