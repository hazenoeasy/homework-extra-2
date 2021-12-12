# coding: utf-8
from binascii import hexlify
from hashlib import sha256
from tqdm import tqdm

def main():
  # read password file
  f = open("password.txt")
  raw_password = f.read()
  # split password_hash and salt
  salt, password  = parse_salt_and_password(raw_password)
  #rainbow book
  with open("rockyou.txt",encoding='utf-8') as f:
      # loading tab
      for line in tqdm(f.readlines()):
        ans = line.strip()
        #  generate salted hash
        generate_password = hash_pword(salt,ans)

        # compare two hash code 
        if(generate_password == password):
          print(ans)
          return

def hash_pword(salt, pword):
    assert(salt is not None and pword is not None)
    hasher = sha256()
    hasher.update(salt.encode('utf-8'))
    hasher.update(pword.encode('utf-8'))
    return hasher.hexdigest()

def parse_salt_and_password(user):
    return user.split('$')

if __name__ == '__main__':
    main()