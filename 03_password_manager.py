from cryptography.fernet import Fernet

# function to generate key named key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() + master_pwd.encode()
fer = Fernet(key)
master_pwd = input("What is the master password?")

def add_pass():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view_pass():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw, fer.decrypt(passw.encode()))


while True:
    mode = input("Add or View passwords? (ADD/VIEW/QUIT)").lower()
    
    if mode == "view" or mode == "v":
        view_pass()
    elif mode == "add" or mode == "a":
        add_pass()
    elif mode == "quit" or mode == "q":
        break
    else:
        print("Invalid mode.")
        break