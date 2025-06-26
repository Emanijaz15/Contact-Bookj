def file(Name,Phone):
    with open("contacts.txt","a") as f:
        f.write(f"{Name},{Phone}\n")
while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Exit")
    user=int(input("Choose: "))
    if (user==1):
        Name=input("Name: ")
        Phone=input("Phone: ")
        file(Name,Phone)
    elif (user==2):
        with open("contacts.txt", "r") as f:
            next(f)    #to ignore the first line as it is empty
            for line in f:
                Name, Phone = line.strip().split(",")
                print(f"Name: {Name}, Phone: {Phone}")
    elif (user==3):
        break
    else:
        print("Invalid input.")
        
