import random #random module

print("Whats up, its Tyrones password generator") #introductory message

Length = int(input("Password Length?: ")) #gets input from the user
Characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()" #random characters
Password = "".join(random.sample(Characters, Length)) #takes the information held in characters variable and information held in length variable and makes a random password
print(Password) #prints the password
print("Thank you for using the program")