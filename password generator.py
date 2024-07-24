import random
import string

def main():
    print("PASSWORD GENERATOR")
    while True:
        try:
            lenght=int(input("Enter the desired lenght of your password: "))
            if lenght>0:
                break
            else:
                print("Your desired password length should be getter than zero")
                continue
        except ValueError:
            print("Enter a valid integer for password length")
    while True:
        ty=input("Enter the type of password you need complex:(yes/no)")
        if ty in ["yes",'y']:
            ty=True
            break
        elif ty in ["no",'n']:
            ty = False
            break
        else:
            print("invalid input print yes or no")
    password=generate_password(lenght,ty)
    print(f"Password generaterd: {password}")
def generate_password(length,ty):
    if ty==True:
        characters=string.ascii_letters+string.digits+string.punctuation
    else:
        characters=string.ascii_letters+string.digits
    password=''.join(random.choice(characters)for _ in range(length))
    return password



if __name__ == "__main__":
    main()

