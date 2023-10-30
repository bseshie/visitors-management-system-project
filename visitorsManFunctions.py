import re
import datetime
from PIL import Image
import pytesseract

class Visitor:
    def __init__(self):
        self.__visitorsName = None
        self.__email = None
        self.__contact = None
        self.__reason = None
        self.__date = None
        self.__arrival = None
        self.__departure = None
        self.__visitee = None
        self.__idNumber = None
        
    def set_visitorsName(self):
        while True:
            name = input("Name: ")
            visName = name.capitalize().replace(" ", "")
            if visName.isalpha():
                self.__visitorsName = visName
                break
            else:
                print("Name should include only letters! ")

    def set_visitorsEmail(self):
        while True:
            userEmail = input("Email: ")
            regex = re.compile(r'[\w]+@[A-Za-z]+\.[A-Za-z]{2,}')
            if re.fullmatch(regex , userEmail):
                self.__email = userEmail
                break
            else:
                print("Invalid email format")
        
    def set_userContact(self):
        while True:
            try:
                contact = input("Contact Number: ")  
                if contact.isdigit() and len(contact) == 10 and contact[0] == '0':
                    self.__contact = contact
                    break
                else:
                    print("Invalid contact number format")
            except ValueError:
                print("Invalid number!")                
    
    def set_purpose(self):
        self.__reason = purpose()
        
        
    def set_dateVisit(self):
        current = datetime.datetime.now()
        date = current.strftime("%d/%m/%y")
        self.__date = date
        print(date)
        
    def set_timeArrive(self):
        current = datetime.datetime.now()
        time = current.strftime("%I:%M %p") 
        self.__arrival = time
        print("Time of arrival:", time)
        
    def set_departureTime(self):
        self.__departure = timeDepart()
        
    def set_visitee(self):
        self.__visitee = employee()

    def set_idCardVerification(self,extractedText):
        pattern = r'[A-Za-z]{2} \d{9}'  
        # Find all occurrences of the pattern in the extracted text
        matches = re.findall(pattern,extractedText)
        for match in matches:
            if match[0] == 'A':
                self.__idNumber = match
                print(f"ID number is {match}") 
                break
    
    def get_visitorsName(self):
        return self.__visitorsName
    
    def get_visitorsEmail(self):
        return self.__email 
                
    def get_userContact(self):
        return self.__contact
    
    def get_purpose(self):
        return self.__reason
    
    def get_dateVisit(self):
        return self.__date

    def get_timeArrive(self):
            return self.__arrival   
    
    def get_departureTime(self):
        return self.__departure
    
    def get_visitee(self):
        return self.__visitee
        
    def get_idCardVerification(self):
        return self.__idNumber
                
        
#functions or methods outside of the class      
def menu():
        print("______Purpose of Visit______")
        print("1. Delivering or Collecting Items \n 2. Special Education Services \n 3. Job Shadowing \n 4. Event or Program \n 5. Appointment or Meeting \n 6. Other")    

        while True: 
            try: 
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Invalid input. Choice should be from 1-6")
            except ValueError:
                print("Invalid input. Choice should be from 1-6")

    
    
def purpose():
    choice = menu()
    
    if choice == 1:
        return "Delivering or Collecting Items"
    elif choice == 2:
        return "Special Education Services"
    elif choice == 3:
        return "Job Shadowing"
    elif choice == 4:
        return "Event or Program"
    elif choice == 5:
        return "Appointment or Meeting"
    elif choice == 6:  
        while True:
            reason = input("Purpose of visit: ").lower().replace(" ", "")
            if reason.isalpha():
                return reason
            else:
                print("Reason should include only letters! ")
        
def timeDepart():
    while True:
        current = datetime.datetime.now()
        try:
            print("Time of departure: ")
            timeHr = int(input("Hour(24-hour format): "))
            timeMin = int(input("Minute: "))
            userTime = f"{timeHr:02d}:{timeMin:02d} {current.strftime('%p')}"
            print(userTime)
        except (ValueError, Exception):
            print("Please enter a valid number")
        else:
            if 1 <= timeHr <= 24 and 0 <= timeMin < 60:
                if (current.hour < timeHr) or (current.hour == timeHr and current.minute < timeMin):
                    print("Valid departure time")
                    return userTime
                else:
                    print("Invalid departure time")
            else:
                print("Invalid time")
    

def employee():
    employeeList = {
        'A': 'John Doe', 'B' : 'Susan Meyers' , 'C' : 'Emma Taylor' , 'D' : 'James Coleman' ,
        'E':'Mark Dan' , 'F' : 'Elon Musk' , 'G' : 'Aliko Dangote' , 'H' : 'Kevin Okyere'
}

    while True:
        nameVisitee = input("Who are you visiting?: ")
        if nameVisitee.replace(" ","").isalpha():
            for name in employeeList.values():
                if nameVisitee.replace(" ","").lower() == name.replace(" ", "").lower():
                    print(f"You are visiting: {name}")
                    return name
            print("Employee / person not found! ")
        else:
            print("Employee name should include only letters")
    
    
def imageToText(imagePath):
    try:
        # Open the image using Pillow (PIL)
        with Image.open(imagePath) as img:
            # Perform OCR on the image
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        return str(e)
    
    
# def emailOrContact():
#         choice = input("Email or contact? (e/c): ").lower()
        
#         if choice == "e":
#             return Visitor.get_visitorsEmail()
#         elif choice == "c":
#             return Visitor.get_userContact()
#         else:
#             print("Invalid choice. Please enter 'e' for email or 'c' for contact.")
#             return Visitor.get_emailOrContact()    
                
