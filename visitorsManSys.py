from visitorsManFunctions import Visitor , imageToText , loading_bar_animation , mainMenu 
import pickle
import getpass
from tabulate import tabulate


visitorList = []

try:
    with open("visitorslist.pkl", "rb") as fileName:
            visitorList = pickle.load(fileName)
except (FileNotFoundError, pickle.PickleError, Exception) as e:
    print(f"Error loading visitor list: {e}")

def theMainMenu():
    visitor = Visitor()
    imagePath = "id sample1.jpg"
    extractedText = imageToText(imagePath)
    
    print("------------The Virtual Receptionist-----------")
    
    visitor.set_visitorsName()
    visitor.set_visitorsEmail()
    visitor.set_userContact()
    visitor.set_purpose()
    visitor.set_dateVisit()
    visitor.set_timeArrive()
    visitor.set_visitee()
    visitor.set_idCardVerification(extractedText)
    visitor.set_departureTime()
    loading_bar_animation()

    print("\n")
    print(f"Welcome, {visitor.get_visitorsName().capitalize()}")

    visitorList.append(visitor)
    
    
    with open("visitorslist.pkl", "wb") as file:
            pickle.dump(visitorList, file)
            print("Successfully saved!")
          
def table():
    head = ["Visitor's Name","Email","Contact","Reason", "Date",
            "Arrival", "Departure", "Employee Visited", "ID Number"]
    

    visitorInfoList = []
    for visitor in visitorList:
        visitorInfo = [
            visitor.get_visitorsName(), visitor.get_visitorsEmail(), visitor.get_userContact(),
            visitor.get_purpose(), visitor.get_dateVisit(), visitor.get_timeArrive(),
            visitor.get_departureTime(), visitor.get_visitee(), visitor.get_idCardVerification()
        ]
        
        visitorInfoList.append(visitorInfo)
        
    print(tabulate(visitorInfoList, headers=head, tablefmt="grid"))
    
def status():
    option = mainMenu()
    
    if option == 1: 
        print("-----------------Login------------------")
        adminInfo = {}
        try:
            with open("loginDetails.pkl", "rb") as openfile:
                adminInfo = pickle.load(openfile)
        except (FileNotFoundError, pickle.PickleError, Exception) as e:
            print(f"Error loading login details: {e}")
        
        
        userName = input("Enter your username: ").lower().strip()
        password = getpass.getpass("Enter your password: ")
        
        maskPassword = '*' * len(password)
        print(maskPassword)
        
        if userName in adminInfo and adminInfo[userName] == password:
            print("Access Granted!")
            print("\n________Visitors Details________\n")
            table()
        else:
            print("Access Denied!")  
             
    elif option == 2:
        theMainMenu()
        
    elif option == 0:
        exit("Goodbye!")        
    
status()
