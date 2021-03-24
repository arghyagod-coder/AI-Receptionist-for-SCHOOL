# This chatbot is appointed to solve issues of parents regarding the
# school and online sessions


# Importing Modules--

import datetime
import webbrowser
import smtplib


#------------------------------------------------------------------
    
# Setting Answer for Online Class Timings

def timings(cls, sec):
    
    # Classes between 2 and 5
    
    if cls<=5 and cls>=2:
        print('You must report to your online class at 7:25 AM and leave at 11:35 AM \n On days of Extra Classes (2 TIMES A WEEK) You have to leave at 12:35 PM after attending 5 Online Sessions. \n Classes take place every week Mon-Fri \n On days before exams, an extra revision class can be held every Saturday. \n Find out more on official DPS Website')
    
    # Classes between 5 and 10

    elif cls>5 and cls<=10:
        print('You must report to your online class at 8:00 AM and leave at 11:35 AM \n On days of Extra Classes (2 TIMES A WEEK) You have to leave at 1:35 PM after attending 5 Online Sessions. \n Classes take place every week Mon-Fri \n On days before exams, an extra revision class can be held every Saturday. \n Find out more on official DPS Website')
    
    # Science students
    
    elif cls>10 and cls<=12 and sec11 == 's':
        print('You must report to your online class at 8:00 AM and leave at 1:45 PM \n Classes take place every week Mon-Fri \n On days before exams, an extra revision class can be held every Saturday. \n Find out more on official DPS Website')
    
    # Commerce students
    
    elif cls>10 and cls<=12 and sec11 == 'c':
        print('You must report to your online class at 8:15 AM and leave at 1:20 PM \n Classes take place every week Mon-Fri \n On days before exams, an extra revision class can be held every Saturday. \n Find out more on official DPS Website')
    
    # Humanities students
    
    elif cls>10 and cls<=12 and sec11 == 'a':
        print('You must report to your online class at 8:15 AM and leave at 1:20 PM \n Classes take place every week Mon-Fri \n On days before exams, an extra revision class can be held every Saturday. \n Find out more on official DPS Website')
        
    # Redirection to Online Portal--
    
    prp = input('\n Visit webpage? (y/n): ')
    if  prp == 'y':
        
        # Open the school website
        
        webbrowser.open('https://www.dpskolkata.com/school-timings/')
        
    elif prp == 'n':
        pass
    
#---------------------------------------------------------
    
# Answer for Exam Dates
    
def DatesOfExam(cls, name):
    if cls<=5 and cls>=2:
        print(f'''{name}'s Exam Schedule for SESSION - 2021-22 :

PT- 1 -------------------------- May-June
PT- 2 -------------------------- August-September
PT- 3 -------------------------- November-December
Finals ------------------------- February-March

No study leave for classes below 5

Answer on sheets till class 4

Pen and Paper exams from class 5''')
    elif cls>5 and cls<=10:
        print(f'''{name}'s Exam Schedule for SESSION - 2021-22 :

Pre-Mid -------------------------- May-June
Half Yearly -------------------------- September
Post-Mid -------------------------- November-December
Annuals ------------------------- February-March
''')
    elif cls>10 and cls<=12:
        print(f'''{name}'s Exam Schedule for SESSION - 2021-22 :

UT-1 -------------------------- April-May
UT-2 --------------------------- May-June
Half Yearly -------------------- September
UT-1 --------------------------- November 
UT-2 --------------------------- December
Annuals ------------------------ February-March
''')
        
# Wishing without voice

def wishMeP():
    # Wishing Accurately
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning!')

    elif hour>=12 and hour<17:
        print("Good Afternoon! ")

    elif hour>=17 and hour<23:
        print("Good Evening! ")

    else:
        print("Good Night! ")

    print('''\n MY NAME IS EDU-CARTA.
Welcome to the query section of
DPS Ruby Park.
Please tell me how
may I help you? ''')
    
#-----------------------------------------
    
# Making a mail system

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('dpskolkatamail@gmail.com', 'school password')
#     server.sendmail(email, to, content)
#     server.close()

# This wont be used in this program as i cant reveal any Password and Accounts, but we can also make a mail system to clarify that the user is really accessing our bot (For extraSECURITY)

# Step 1: Making a Login System

def login(x, y):
    # Making few global variables
    
    global email, passw
    
    # Fixed School Code (to be given by school)
    grpcode = 'ARD6672'
    
    # Defining Variables
    email = x
    passw = y
    
    # Checking validity of mail:
    
    mail_ext = ('gmail.com' or 'hotmail.com' or 'outlook.com' or 'yahoo.com' or 'aim.com' or 'yandex.com' or 'zohomail.com' or 'tutanota.com' or 'tutanota.de' or 'tutamail.com' or 'tuta.io' or 'keemail.me' or 'icloud.com')
    
    if mail_ext in email:
        pass
    else:
        print('Invalid Email. Did you forget to put the extension? No business mail accounts allowed')
        exit()
        
    #Checking Validity of School iD
        
    if passw == grpcode:
        pass
    else:
        print('Invalid ID. Access denied !!')
        exit()
        

    
#--------------------------------------------------------------------------
    

# Starting MAIN program

if __name__ == "__main__":

# Setting the Login System
    
    
    print('''Before we talk,
I need to clarify that
it's you. Login to your account: \n''')
    mail = input('Your Email ID: ')
    UID = input('\n School ID provided by School: ')
    login(mail, UID)
    wishMeP()
    
    # Prompt Details of Student
    
    cls = int(input('Class: '))
    name = input('Name: ')
    sec = input('Section: ')
    
    if cls > 10:
        sec11 = input('Science (s), Arts(a) or Commerce(c)? ')
    
#     content = '{name} has entered to the DPS Reception- EduCarta using your ID and Passcode. If it wasnt you, you may report to the school via mail to dpskolkata.rpk@gmail.com'
#     to = mail
#     sendEmail(to, content)

# Repeat Loop
    
    while True:
        # Input
        
        query = input('\nType your message... \n')
        
        # Timings-
        
        if 'timings' in query:
            # Online or Offline?
            
            # Online-
            mode = input('Online or Offline? ')
            if mode == 'online' or 'Online' or 'ONLINE':
                timings(cls, sec)
                
            # Offline-
            elif mode == 'offline' or 'Offline' or 'OFFLINE':
                webbrowser.open('https://drive.google.com/file/d/19xvo5NUAN9ts1FTWageaDlhR8DbV3eFz/view?usp=sharing')
            
        # Exam Dates-
            
        elif 'examination dates' in query or 'exam dates' in query or 'exam schedule' in query:
            DatesOfExam(cls, name)
            
        # Syllabus-
         
        elif 'syllabus' in query:
            webbrowser.open(f'https://www.dpskolkata.com/academics/syllabus/syllabus-class-{cls}/')
            print(f'\n Did Not Open? \n \n Paste this link in your browser: \n\n https://www.dpskolkata.com/academics/syllabus/syllabus-class-{cls}/')
            
        # Mode of examination
        
        elif 'mode of examination' in query or 'exam mode' in query or 'online or offline exam' in query or 'offline or online exam' in query:
            print('\n Exams will be held online through our school exam portal, dpskolkata.net/exam')
            prp = input('\n Visit webpage? (y/n): ')
            if  prp == 'y':
                webbrowser.open('https://www.dpskolkata.net/exam/')
                
            elif prp == 'n':
                pass
            
        # Exit / Bye
            
        elif ('exit' or 'bye' or 'gtg' or 'goodbye') in query:
            print('Hope I could help you')
            exit()
            
        # Contact Info
        
        elif 'contact' in query:
            print('''Contact Us at:

High School
254 Shanti Pally, RB Connector,
Kolkata 700 107
Telephone: +91 33 71300258, +91 33 71300265
Fax: +91 33 2441 5301

Existing students send mail to : info@dpskolkata.com
fees related queries, send mail to : fees@dpskolkata.com \n\n''')
            
        else:
            print('''\n\nSorry, I couldn't get you, and I heartily apologize for that. There may be some technical dfficulties on our side.

Was it something unrelated to the school? Then I would like to mention that I was made to solve doubts regarding DPS Ruby Park School.

OR

Try using some of these keywords-

offline class timings

syllabus

exam mode

regular timings

exam dates

contact 

OR

Search your doubts in https://www.dpskolkata.com/

''')
            
# THE END------------------------------------------
        
        
    


