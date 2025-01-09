def grocery():
    print("looking for a Huge or convenient Asian supermarket with many options?" )
    answer = input("Y for yes and N for no: ").upper()
    
    if not (answer == "Y" or answer == "N"):
        print("Not a valid input. ")

    if answer == "N":
        print("Ok, Goodbye")
    
        
    elif answer == "Y":
      option = input("Convenient or Huge?").capitalize()
      if not (option == "Convenient" or option == "Huge"):
          print("Did not answer the question, Goodbye")

      if option == "Convenient":
          reccomend("Jmart")
      elif option == "Huge":
          reccomend("H Mart")     

    

def reccomend(store):
        print("You might like ", store)
    

      
grocery()
