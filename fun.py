import os

while True:
    try:
        count = int(input("Enter a number: "))
        if count <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

i = 0
hi = input("Are you sure? [Yes] or [No]: ").strip()

if hi.lower() == "yes":
    while i < count:
        os.system("explorer.exe")
        i += 1
else:
    # If not 'yes', do nothing or handle accordingly
    pass
