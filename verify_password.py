password="tokyoghoul"

def verify_password(password1):
    if(password==password1):
        print("Matched Password")
    else:
        print("Wrong Password")
password1= input("Enter the password:")
verify_password(password1)