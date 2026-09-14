# numbers = [1, 2, 3, 4, 5]
# new_numbers =[]

# def transform_numbers(numbers):
#     for number in numbers:
#         new_numbers.append(number + 5)
#     return new_numbers
# print("The transformed numbers are:", transform_numbers(numbers))
# print("The original numbers are:", numbers)

# val = map(transform_numbers, numbers)

# numbers = [1, 2, 3, 4, 5]
# print("The original numbers are:", numbers)
# val = map(lambda x: x + 5, numbers)
# print("The transformed numbers using map and lambda are:", list(val))


# numbers = [1, 2, 3, 4, 5]
# def filter_numbers(numbers):

#  val = filter(lambda numbers: numbers % 2 == 0, numbers)
# print("The filtered even numbers using filter and lambda are:"   )
# print("The original numbers are:", numbers)              

class animal:

    def __init__(self,name,sound):
        self.name = name
        self.sound = sound 
    def speak(self):
        print(self.sound) 