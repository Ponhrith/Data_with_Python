queue = []

print("[a] Add a person into the line")
print("[b] Remove the front person")
print("[c] View the front person")
print("[d] Exit Program")
option = input("Enter your option: ")

isExit = False

while isExit == False:
    if option == 'a':
        name = input("Enter a name: ")
        queue.append(name)
    elif option == 'b':
        if queue == []:
            if queue == []:
                print("The list is empty. ")
            else:
                queue.pop(0)
    elif option == 'c':
        if queue == []:
            print("The list is empty")
        else: print(queue[0])
    elif option == 'd':
        print("You are exiting the program.")
    else:
        print("You have enter an invalid option.")

    print("[a] Add a person into the line")
    print("[b] Remove the front person")
    print("[c] View the front person")
    print("[d] Exit Program")
    option = input("Enter your option: ")
