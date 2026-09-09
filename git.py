# names=["John","Paul","George","Ringo"]
# m_name="marcus"
# names.append(m_name)
# age=13
# names.append(age)
# print(names[4])
# print(type(names[4]))

# A small Program which takes people name and neccesary credencials
# name=input("Enter Your Name: ")
# Age=input("Enter Your Age : ")
# School=input("Enter Your School: ")
# Program=input("Enter Your Program: ")
# Level=input("Enter Your Level: ")
# print(f"Your name is {name},your agew is {Age},you are a student of {School}, your program is {Program},and  you are in level {Level}")


users={
    "marcus" : "password1",
    "courage":"password2",
    "addae": "password3"
}
username=input("Enter Your username: ")
username=username.upper()
password=input("Enter Your Password: ")
password=password.upper()
if username in users and users[username]==password:
    print("Login Successful")
else:
    print("Invalid username or password")


