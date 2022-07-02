print("""Welcome!
Enter a number between 1 and 1000

""")

user = int(input("Enter a number: "))

# code to check for even or odd number
if (user >= 1 and user <= 1000):
    if (user % 2 == 0):
        print("{:d} is an even number".format(user))
    else:
        print("{:d} is an odd number".format(user))
else:
    print("Ooops! Enter a number between 1 and 1000")