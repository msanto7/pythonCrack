#Assignment #2 Password Cracker
#Michael Santoro 

#mcrypt 
#use a small english dictionary to crack the password
#Arguements --> 1. Shadow File  2. Username 
#Returns    --> 1. Password 

#if user does not exist print warning 
#if password is not in dictionary print that 

#################################################################
import pwd, grp
import crypt 


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


def main():

    #accept and open shadow file
    shadowPath = raw_input("Please enter the path to your shadow file: \n ")
    try:
        shadow = open(shadowPath, 'r')
    except IOError:
        print("File could not be opened. ")
        return

    #accept and search for username
    uName = raw_input("\nPlease enter a username from the list of users: \n")

    for line in shadow.readlines():
        if ":" in line:
            tempU = line.split(":")[0]
            if (uName == tempU):
                passwdHash = line.split(":")[1].strip(" ") 
                print ("Username: " + uName + " has been found. Cracking Password...")
                checkDictionary(passwdHash, "/msanto7/cracklib-small")   #this dictionary is hard coded so make sure the path will work when downloaded 
                return


    print("Password not in dictionary")
    return
#start main function

if __name__ == '__main__' :
    main()


#Use shadow file to find check if this user name exists

#if username does not exist print and exit

#if the username exists run the dictionary and compare hashes to the one from shadow

      #if a match is found print the password 
#print("The Password is: " )

      #else if (no match)
#print("Password not in Dictioanry. ")



                                                                      
