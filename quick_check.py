import subprocess
import datetime

#Quick System Checker 

time = datetime.datetime.now().strftime("%m-%d-%y at %H:%M:%S")

print("Hey There! \U0001F44B Let's run a quick system check!")

while True:
    print("\n Which would you like to run?")
    print("1 - Ping Google")
    print("2 - Show IP config")
    print("3 - Exit")

    choice = input ("Choose a number(1,2,3): ")

    if choice == "1":
        print("pinging google...\n")
        c1 = subprocess.run(["ping","8.8.8.8"], capture_output = True, text = True)
        print(f"Ping completed \U0001F600 on {time}  ")
        print(c1.stdout)
        print("Ping completed Successfully")
        break

    elif choice == "2":
        print ("\n Showing IP config...\n")
        c1 = subprocess.run(["ipconfig"], capture_output = True, text = True)
        print(c1.stdout)
        break

    elif choice == "3":
        print("Goodbye \U0001F641")
        break

    else:
        print("Wrong input! Try again \U0001F61F")
        
