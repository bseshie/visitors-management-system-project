# Visitors Management System

This is a python- based application designed to manage visitor information. It ultilizes image recognition techniques to extract visitor id numbers from identification cards, for security reasons. This system is user friendly and allows quick and easy input of visitor details.

## Features

Image recognition: the systems employs OCR(Optical Character Recognition) techniques to extract text data from identification cards.
Visitor information management: captures visitor details
User interaction: provides an interactive menu for selecting the reason of the visit.
Data storage: stores visitor information in a binary using the pickle module for future refernce 

## Prerequisites 
- Python 3.x
- PIL library for image processing: 'pip install pillow'
- Pytesseract library for OCR: 'pip install pytesseract'
-Tesseract-OCR: Tesseract Installation Guide

### Files and Modules
- VisitorsManFunctions.py: Contains the Visitor class and various functions for      visitor information processing.
- visitorsManSys.py: The main script that interacts with the user and utilizes functions from other modules.

### Acknowledgments
Special thanks to the developers of Tesseract-OCR, Pillow, and pytesseract for their invaluable contributions to open-source software. This project is built upon their work.

### Note

-This application is designed for educational purposes and may require further enhancements for production-level usage.

- Ensure proper handling of sensitive information, especially email credentials, and follow security best practices.

- For detailed instructions on Tesseract-OCR installation and configuration, refer to the official Tesseract Wiki.
