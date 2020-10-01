#E-mail Slicer

email = input("What is your email address? ").strip() #the strip() method removes characters from both left and right based on the argument (a string
# specifying the set of characters to be removed)

user_name = email[:email.index("@")]

domain_name = email[email.index("@") + 1:]

output = "Your username is '{}' and your domain name is '{}.'".format(user_name, domain_name) #the format() method formats the specified value(s) and
# insert them inside the string's placeholder

print(output)