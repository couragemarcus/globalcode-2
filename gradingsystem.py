#  Grading system 
print("="*12)
print("   Welcome to Your Grading System ")
print("="*12)
Score=int(input("Enter Your Score: "))

if Score >=80:
    print("Your Grade is A1")
elif Score >=70:
    print("Your Grade is B+")
elif Score >=80:
    print("Your Grade is B")
elif Score >=70:
    print("Your Grade is C+")
if Score >=60:
    print("Your Grade is C")
if Score >=50:
    print("Your Grade is D")
else:
    print("invalid input")