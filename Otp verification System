import os
import math
import random
import smtplib
import requests


global s

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("noreplyotpofficer@gmail.com", "jaizeswbkqmjgzrd")


def opt():

    global msg,OTP

    digits="0123456789"
    OTP=""
    for i in range(4):
        OTP+=digits[math.floor(random.random()*10)]

    otp = "Your OTP for  verification is " + OTP 

    print(otp)
    msg= otp

    print("Enter '1' for E-mail Verification")
    print("Enter '2' for mobile Verification")

    e=str(input('Enter your Preference'))

    if  e == '1' or e == 'ONE' or e =='one' :

        mail()


    elif e== '2' or e == 'TWO' or e == 'two' :
        
        text()


    else:
        print('Plese enter a valid input')
        opt()





def text():
    
    my_phone_number =(input("Enter your Mobile number"))




    if len(my_phone_number) == 10 :
        my_phone_number = my_phone_number
          

    elif len(my_phone_number) == 13 :
        
        my_phone_number = my_phone_number[3:]
         
        

    else:
        print("Wrong Mobile Number Try again")
        text()




    url = "https://www.fast2sms.com/dev/bulk"


    querystring = {"authorization":"shHJAb3XLQGD9IPVwxuh70DqVxKuQbJtRXOmQw5ZKY2uvTCHs02yGi6kMoM1",
                   "sender_id":"FSTSMS",
                   "message":msg,
                   "language":"english",
                   "route":"p",
                   "numbers":my_phone_number}


    headers={
        'cache-control': "no-cache"
    }
    

    response=requests.request("GET", url, headers=headers, params=querystring)
    

    print("verification code sent Sucessfully")



    while True:
        a = input("Enter Your OTP >>: ")
        if a == OTP:
            print("Verified")
                      
            break
        
        else:
            print("Your OTP Is Incorrect")
            continue






def mail() :
        
    emailid = input("Enter your email: ")
    

    if '@' in emailid and '.com' in emailid:
        s.sendmail('&&&&&&&&&&&',emailid,msg)
        

    else:
        print('Wrong Email Entered Try again')
        mail()
        
    print("verification code sent Sucessfully")

    while True:
        a = input("Enter Your OTP >>: ")
        if a == OTP:
            print("Verified")
            s.sendmail('&&&&&&&&&&&',emailid,'Thank You for Verification')
            break

        else:
            print("Your OTP Is Incorrect")
            continue









opt()

    
