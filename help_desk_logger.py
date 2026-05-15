import datetime
print("Welcome to the IT Help Desk Logger")

user = input("Type your name: ")
issue = input("Describe your issue in one sentence: ")


timestamp = datetime.datetime.now().strftime("%m-%d-%y  %H:%M:%S")

print(timestamp)

with open(r"C:\Users\name\folderpath\ticket_log.txt", "w") as user_report:
    user_report.write(f"{timestamp}\n")
    user_report.write(f"client: {user}\n")
    user_report.write(issue)

print(f"Ticket has been established for {user}")
