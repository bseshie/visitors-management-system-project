from visitorsManFunctions import Visitor , imageToText

imagePath = "id sample1.jpg"
extractedText = imageToText(imagePath)
visitor = Visitor()
print("------------The Virtual Receptionist-----------")
visitor.set_visitorsName()
visitor.set_visitorsEmail()
visitor.set_userContact()
visitor.set_purpose()
visitor.set_dateVisit()
visitor.set_timeArrive()
visitor.set_departureTime()
visitor.set_visitee()
visitor.set_idCardVerification(extractedText)

print("\n________Visitor's Details________")
print("Visitor's Name:", visitor.get_visitorsName())
print("Email: ", visitor.get_visitorsEmail())
print("Contact Number: (+233)", visitor.get_userContact())
print("Purpose of Visit:", visitor.get_purpose())
print("Date of Visit:", visitor.get_dateVisit())
print("Arrival Time:", visitor.get_timeArrive())
print("Departure Time:", visitor.get_departureTime())
print("Person Visited:", visitor.get_visitee())
print("ID Number:", visitor.get_idCardVerification())

