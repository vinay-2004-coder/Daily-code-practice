from tkinter.font import names
import art
print(art.logo)


import game_data
import random

data=game_data.data
a=data[random.randint(0,len(data)-1)]

compare_name_a=a["name"]
compare_follower_a=a["follower_count"]
compare_description_a=a["description"]
compare_country_a=a["country"]

b=data[random.randint(0,len(data)-1)]

compare_name_b=b["name"]
compare_follower_b=b["follower_count"]
compare_description_b=b["description"]
compare_country_b=b["country"]

print(f"Compare A: {compare_name_a}, a {compare_description_a}, from {compare_country_a}")

print(f"Compare B: {compare_name_b}, a {compare_description_b}, from {compare_country_b}")

user_input=input("Who has more followers? Type 'A' or 'B' ")

if(compare_follower_a > compare_follower_b):
    print("A is greatest")
elif(compare_follower_b > compare_follower_a):
    print("B is greatest")