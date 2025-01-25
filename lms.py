#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from termcolor import colored
import sys

def main():    
    try:
        welcome_msg()
        user_input()
        lms_management()
        
    except ZeroDivisionError:
        print("You cant divide by Zero:, Try again")
    except ValueError:    
        print("You cant divide by invalid value ,Try again with Valid")
    except Exception as e:
        print("Some Unknown Error, Try Again", e)
    else: # if no error
        print("Successfully Completed the task")
    finally:  # finally show
        print("Program Developed by:Gopal")

def welcome_msg():
     welcome_msg ="Welcome to IIT Guwahati Central Library"
     print(colored(welcome_msg, 'green', attrs=['bold']))
     #print(welcome_msg)    

def user_input_generic():                      
    user_name = "admin"
    password = "password123"
    u = input("Enter Username to Login:")
    p = input("Enter Password:")
    if u == user_name and p == password:
        print("Thenk You for Providing Correct Username and Password")
    else:
        print("please provide valid Username or Password")             
    
def lms_management():
    print("\nWelcome to IITG Library Management Services")
    print("How can I help you!!")
    print("Plese choose the below available services and select the appropriate option \n ")
    avail_services()
    option = input("\nEnter Option:")
    if (option == "1"):
        print("1")
        book_avail()                             # To show all Books available including issued and not issued
        lms_management()
    elif (option == "2"):
        print("2")
        view_issued_books()                      #To show issued books, assigned to the users 
        lms_management()
    elif (option == "3"):
        print("3")
        view_not_issued_books()                   #To shows not issued books, that is available only books.
        lms_management()
    elif (option == "4"):
        print("4")
        book_name = input("\nEnter Book name:")
        auth_book = input("\nEnter Book Author:")
        book_add(book_name,auth_book)             #To add new Books to the Library 
        lms_management()
    elif (option == "5"):
        print("5")
        book_name = input("\nEnter Book name:")
        auth_book = input("\nEnter Book Author:")
        asgn_book = input("\nEnter Assignee :")
        issue_book(book_name,auth_book,asgn_book) #Assign a book to a user
        lms_management()
    elif (option == "6"):
        print("6")
        print("Enter Book name and Author to return")
        book_name = input("Enter Book name:")
        auth_book = input("Enter Book Author:")
        return_book(book_name,auth_book)
        lms_management()                      # Return a book back to Library
    elif (option == "7"):
        print("7")
        exit_program()
    else:
        option_check(option)                      #user Option Check 
        
def option_check(opt_num):
    options = (1,2,3,4,5,6,7)
    if(opt_num not in options):
        print("Wrong Option, please try again\n\n")
        lms_management()
def avail_services():
    services = ["Total Available Books", "View Issued Books","View Not Issued Books", "Add a Book","Issue a Book","Return a Book", "Exit"]
    for i, item in enumerate(services):        
        print (i+1, item)
        
def book_avail():
    print("Below are the list of books available\n")
    book_store()   

def view_issued_books():
    #print("Below are the list of books Issued\n")
    issued_books()
    #book_store()   

def view_not_issued_books():
    print("Below are the list of books Not Issued\n")
    not_issued_books()
    #book_store()  
def book_add(name,author):
    update_master_library(name,author)    
    
def issue_book(name,author,asgn_book):
    check_book_issue(name,author,asgn_book)  
    
def return_book(name,author):
    ret_book(name,author)        
    
def exit_program():
    print("Exiting The Services! Thank You")
    exit()

#Fuction to check book status in master library before assigning
def check_book_issue(name,author,asine):
    if name in master_store:
            #master_store[name] = {}
            if(author in master_store[name]["Author_name"]):
                if(master_store[name]["Assigned_To"] == ""):
                    master_store[name]["Assigned_To"]= asine
                    print("Book Name: ",name,"with Author ", author, "has been assigned to ",asine, "succesfully\n")
                    #book_store()
                else:
                    print("Book",name,"with",author,"already Assigned to",master_store[name]["Assigned_To"])
            else:
                print("Author:",author,"Incorrect")
                print("No Book found with name:",name,"and Author:",author)
                if(master_store[name]["Assigned_To"] == ""):
                    print("Book:",name,"with Author:",master_store[name]["Author_name"], "is available")
                    option = input("Do you want to proceed ? \n Press Y/y or N/n") 
                    if(option == "Y" or option == "y"):
                        master_store[name]["Assigned_To"]= asine
                        print("Book Name: ",name,"with Author ", author, "has been assigned to ",asine, "succesfully\n")
                        #book_store()
                    elif (option == "N" or option == "n"):
                        print("Please select the Options\n")
                        lms_management()
                #else:
                    #print("Book Name: ",master_store[name],"with Author ", master_store[name]["Author_name"], "is already assigned to ",master_store[name]["Assigned_To"])                
    else:
        print("Book",name,"not found, Please provide correct Book Name\n")

#Function to update the master library in case of add Books
def update_master_library(name,author):
    tmp_dict = {"Author_name":author, "Assigned_To":""}
    if (name not in master_store):
            master_store[name] = {}
            master_store[name]["Author_name"]= author
            master_store[name]["Assigned_To"]= ""
            print("New Book:",name,"Author_name: ",author, "Added Successfully\n Please check the Book List\n")
            #book_store()
    elif (name in master_store):
            if(author not in master_store[name]["Author_name"]):
                #master_store[name] = {}
                master_store[name]["Author_name"].append(author)
                master_store[name]["Assigned_To"]= ""
                print("New Book:",name,"Author_name: ",author, "Added Successfully\n Please check the Book List\n")
                #book_store()          
        
            else:
                if(author in master_store[name]["Author_name"]):
                    print("Book",name,"with",author,"Exists")

#Function to show books not issued in master library
def not_issued_books():
        books=[]
        for i,j  in master_store.items():
        #print("\nBook Name:", i)    
        #for key in j:
            if(j["Assigned_To"] == ""):
                #print(key + ':', j[key])
                print(i," :not assigned to User")
                books.append(i)
        print(books)

#Function to issue a book and update master library
def issued_books():
        books=[]
        for i,j  in master_store.items():
        #print("\nBook Name:", i)    
        #for key in j:
            if(j["Assigned_To"] != ""):
                #print(key + ':', j[key])
                print(i," Book is assigned to User", j["Assigned_To"])
                books.append(i)
        if(len(books) == 0):
            print("No Books Assigned\n")
        else:
            print(books)

#Function to return book and update the master library
def ret_book(name,author):
    if name in master_store:            
            if(author in master_store[name]["Author_name"]):
                if(master_store[name]["Assigned_To"] != ""):
                    master_store[name]["Assigned_To"] = ""
                    print("New Book:",name,"with Author_name: ",author, "Successfully Returned")
                    #book_store()
                else:
                    print("Printing",master_store[name]["Author_name"])
                    print("Records show  that Book:",name,"with Author:",author,"is Not assigned, can not returned. please check and return correct book")
            else:
                print("Book:",name,"with Author:",author,"doesnt exists in Book Store, can not returned. please check and return correct book")
                
    else:
        print("Book Name:",name,"doesnt exists in Book Store, are you sure this is correct Book Name.")

#Print the Book list
def book_store():    
    #print(type(dict))
    for i,j  in master_store.items():
        print("\nBook Name:", i)    
        for key in j:
            print(key + ':', j[key])   

#dictionary to store the Books in library -master library
master_store = {
                "Book1":{"Author_name":["Author1"], "Assigned_To":""},
                "Book2":{"Author_name":["Author2"], "Assigned_To":""}, 
                "Book3":{"Author_name":["Author3"], "Assigned_To":""},
                "Book4":{"Author_name":["Author4"], "Assigned_To":""}, 
                "Book5":{"Author_name":["Author5"], "Assigned_To":""}
               }

def user_input():
    print(colored("Login to Continue",'green', attrs=['bold']))
    print(colored("Press Q to quit Library Services",'green', attrs=['bold']))
    user = input("Username")
    if(user == "Q" or user == "q"):
        exit_program()    
    check(user)
    password = input("Password")
    if(password == "Q" or password == "q"):
        exit_program()
    check(password) 
    check_credentials(user,password)
    
def check(data):
    #print(type(data))    
    d = data.find(" ")
    #print(d) 
    if(d >= 0 ):
        print("Username or password has spaces, pls correct and reenter")
        user_input()

#function to store passwords in a dictionary
def read_credentials_dict(): 
    new_contents=[]
    dict={}
    dict["gopal"]="password"
    dict["user1"]="password1"
    dict["user2"]="password2"
    dict["user3"]="password3"
    dict["user4"]="password4"
    for i,j in dict.items():
        cont =[]
        cont.append(i)
        cont.append(j)
        new_contents.append(cont)    
    return(new_contents)

#function to store passwords in a dictionary
def read_credentials_file():
    new_contents=[]
    with open("login.txt", "r") as file:
        contents = file.readlines()
        for line in contents:
            fields = line.split(",")
            fields[1] = fields[1].rstrip()
            new_contents.append(fields)
    return(new_contents)

#function to validate usename and passwords
def check_credentials(user,password):           
    readlogins = read_credentials_dict()
    #print(readlogins)
    logged_in = False
    for line in readlogins:
        #print("line read:",line)
        if line[0] == user and logged_in == False:
            if line[1] == password:
                logged_in = True
        if logged_in == True:
            print(colored("Logged in successfully",'green', attrs=['bold']))
            logged_in = True
            break
    if(logged_in == False):
        print(colored("Username and Password are incorrect",'red', attrs=['bold']))
        user_input()      


#main()


# In[ ]:


6


# In[ ]:




