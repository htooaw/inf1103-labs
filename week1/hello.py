print("==============================")
print("welcome here")
print("my first post")
print("==============================")


username = "cool creator"
bio = "Fun blogger"
followers = 1000

print("Username:", username)
print("Bio:", bio) 
print("Followers:", followers)

followers = 100

followers += 50
print("Day1:",followers)

followers += 20
print("Day2:", followers)

followers -= 10
print("Day3:", followers)

username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Category: ")

print("\nInstagram Profile")
print("==============================")
print("Username:", username)
print("Age:", age)
print("Category:", category)

if age>40 and category =="fun":
    print("You are old what is fun for you??")