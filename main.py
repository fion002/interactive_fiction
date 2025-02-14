input('Enter your name:')

print('Hello,{name}!')

##Start interactive friction

while True:
    print("""you are in a room with a table not a chair.
          
          OPTIONS:
          1.Look under the table
          2.Sit down
          """)
    
    choice = input("what do you do")

    if choice == "1":
        print("You find a key under the table.")
        break
    elif choice == "2":
        print("You sit down and relax.")
        break
    else:
        print("Invalid choice.\n")