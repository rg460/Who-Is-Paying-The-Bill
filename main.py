import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
# Plan
# Generate a random number index between 0 and the length of the list
random_index = random.randrange(len(names))
# Get an element from a list based on that index
random_name = names[random_index]
# ouput the random name of the person paying the bill 
print(f"{random_name} is going to buy the meal ")
  

