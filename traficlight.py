
# Conditions in python

# Trafic Light Program
# Taking inputs from the user
light=input("Enter the light color: ")
light=light.upper()

if light=="RED" :
    print("STOP")
elif light=="YELLOW":
    print("READY")
elif light=="GREEN":
    print("GO")
else:
    print("Invalid light color")
