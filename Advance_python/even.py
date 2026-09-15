num= [1,56,234,87,4,76,24,69,90,135]

def is_even(num):
    print("The original numbers are:", num)
    value = filter(lambda num: num % 2 == 0, num)
    print("The even numbers are:", list(value))

is_even(num)

def is_odd(num):
    print("The original numbers are:", num)
    value = filter(lambda num:num % 2 != 0, num)
    print("The odd numbers are:", list(value))

is_odd(num)
