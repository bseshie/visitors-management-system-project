import re
import datetime
from PIL import Image
import pytesseract
import sys
import time


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
                self.__visitorsName = name
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
        #print("Date: ",date)
        
    def set_timeArrive(self):
        current = datetime.datetime.now()
        time = current.strftime("%I:%M %p") 
        self.__arrival = time
        #print("Time of arrival:", time)
        
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
                #print(f"ID number is {match}") 
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
            reason = input("Purpose of visit: ")
            purposeVisit = reason.lower().replace(" ", "").replace("'" , "").replace("," , "").replace("." , "")
            if purposeVisit.isalpha():
                return reason
            else:
                print("Reason should include only letters! ")
        
def timeDepart():
    while True:
        current = datetime.datetime.now()
        try:
            print("Time of departure: ")
            timeHr = int(input("Hour(in 24 hour format): "))
            timeMin = int(input("Minute: "))
            userTime = f"{timeHr:02d}:{timeMin:02d}"
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
    'employee 1': {
        'name': 'John Doe',
        'job_title': 'Software developer',
        'department': 'Technology',
        'gender': 'Male',
        'email': 'johndoe@gmail.com'
    },
    'employee 2': {
        'name': 'Susan Meyers',
        'job_title': 'Systems engineer',
        'department': 'Technology',
        'gender': 'Female',
        'email': 'susanmey2@gmail.com'
    },
    'employee 3': {
        'name': 'Emma Taylor',
        'job_title': 'Marketing Manager',
        'department': 'Marketing',
        'gender': 'Female',
        'email': 'tayemma@gmail.com'
    },
    'employee 4': {
        'name': 'James Coleman',
        'job_title': 'Chief Operating Officer',
        'department': 'Management',
        'gender': 'Male',
        'email': 'jcoleman1@gmail.com'
    },
    'employee 5': {
        'name': 'Mark Dan',
        'job_title': 'Auditor',
        'department': 'Finance',
        'gender': 'Male',
        'email': 'markdan@gmail.com'
    },
    'employee 6': {
        'name': 'Elon Musk',
        'job_title': 'Finance Manager',
        'department': 'Finance',
        'gender': 'Male',
        'email': 'the_elonmusk@gmail.com'
    },
    'employee 7': {
        'name': 'Aliko Dangote',
        'job_title': 'Chief Financial Officer',
        'department': 'Finance',
        'gender': 'Male',
        'email': 'chief_alikodangote@gmail.com'
    },
    'employee 8': {
        'name': 'Kevin Okyere',
        'job_title': 'Senior sales executive',
        'department': 'Sales',
        'gender': 'Male',
        'email': 'kevinokyere1@gmail.com'
    },
    'employee 9': {
        'name': 'Belinda Seshie',
        'job_title': 'Chief Executive Officer',
        'department': 'Management',
        'gender': 'Female',
        'email': 'thebelseshie@gmail.com'
    },
    'employee 10': {
        'name': 'Danielle Spencer',
        'job_title': 'Human Resource Manager',
        'department': 'Human Resource',
        'gender': 'Female',
        'email': 'daniellespencer3@gmail.com'
    },
    'employee 11': {
        'name': 'Emma Taylor',
        'job_title': 'Cloud engineer',
        'department': 'Technology',
        'gender': 'Male',
        'email': 'emmatay12@gmail.com'
    },
    'employee 12': {
        'name': 'James Coleman',
        'job_title': 'Data Scientist',
        'department': 'Technology',
        'gender': 'Male',
        'email': 'jcole254@gmail.com'
    }
}
    
    infoList = []
    while True:
        nameVisitee = input("Who are you visiting?: ")
        
        if nameVisitee.replace(" ","").isalpha():
            found = False
            for employeeInfo in employeeList.values():
                if nameVisitee.replace(" ","").lower() in employeeInfo['name'].replace(" ","").lower():
                    infoList.append(employeeInfo)
                    found = True

            if not found:
                print("Employee not found!")
            elif len(infoList) == 1:
                print(infoList)
                print(f"You are visiting {infoList[0]['name']}.")
                return infoList[0]['name']
                #break
            else:
                print("Multiple employees found: ")
                for idx, employee in enumerate(infoList, start=1):
                    print(f"{idx}.{employee['name']} ,{employee['job_title']}, {employee['department']}, {employee['gender']}, {employee['email']}")
                    
                try:
                    choice = int(input("Please enter the number corresponding to the employee you are visiting: "))
                    if 1 <= choice <= len(infoList):
                        selectedEmployee = infoList[choice - 1]['name']
                        print(f"You selected option {choice}")
                        return selectedEmployee
                        #break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
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
    
    
def mainMenu():
    print("Welcome!")
    print("========Administrator or Visitor?========")
    print("1. Administrator \n2. Visitor / Guest \n0. Exit")    

    while True: 
        try: 
            option = int(input("Enter your choice: "))
            if 0 <= option <= 2:
                return option
            else:
                print("Invalid input. Choice should be from 1-2")
        except ValueError:
            print("Invalid input. Choice should be from 1-2")
            

def loading_bar_animation():
    total_progress = 100  # Total progress value (e.g., 100%)
    bar_width = 50  # Width of the loading bar in characters

    for progress in range(total_progress + 1):
        completed_width = bar_width * progress // total_progress

        sys.stdout.write("\r[")
        for i in range(bar_width):
            if i < completed_width:
                sys.stdout.write("=")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("] {}%".format(progress))
        sys.stdout.flush()

        # Add a small delay to control the speed of the animation
        time.sleep(0.05)

    print()  # Move to the next line after the loading bar is complete
    
    