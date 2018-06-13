import time
import os 
import urllib.request
import webbrowser
X='''
Press 1: to check current date and time 
Press 2: to create a file
Press 3: to create a directory
Press 4: to search something on google
Press 5: logout your system
Press 6: reboot your OS 
Press 7: to check internet connection 
Press 8: to login whatsapp on browser
Press 9: to check all connected IP address in your browswer
'''

print (X)

choice=input("enter your choice")

if choice=='1':
       print ("showing current date and time")
       print (time.ctime())
if choice=='2':
       	print("creating a file")
       	f=open("example1.txt","x") # will show error if file named already exist
        f=open("example2.txt","w") #will create a file if exist
if choice=='3':
       print("creating a folder")
       path='/home/riddhi/folder18'
       os.makedirs(psth,exist_ok=True)
if choice=='4':
        print("to search something on google") 
        msg=input("type to search")
        webbrowser.open_new_tab('http://www.google.com/search?q='+msg)
if choice=='5':
        print("logging out your system")
        os.system('gname-session-quit')
if choice=='6':
        print("shutdown your system")
        time.sleep(2)
        os.system("poweroff")
if choice=='7':
       print("checking internet connection")
       url="http://www.google.com"
       urllib.request.urlopen(url)
       status="connected"
       print(status)
    
if choice=='8':
        print("logging in your whatsapp account")
        webbrowser.open_new_tab("http://www.whatsapp.com")
       
if choice=='9':
        print("all connecting IP address is showing")
        
else
       print("wrong choice")




       
       




