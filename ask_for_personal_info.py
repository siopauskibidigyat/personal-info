#ask for full name, address, gender, hobbies, favorite color, favorite song, age, number
with open("./output.txt", "a") as personal_infos:
    while True:
            
        name = input("Name: ")
        gender = input("Gender: ")
        address = input("Address: ")
        fav_color = input("Favorite Color: ")
        fav_song = input("Favorite Song: ")
#check for errors for input age and number        
        while True:
            try:
                age = int(input("Age: "))

                while True:

                    number = input("Contact Number: 09")
                    if len(number) == 9 and number.isdigit:
                        number = f"09{number}"
                        break
                    else:
                        print("Number should only contain 11 digits")
                break
            
            except: 
                print("Please input valid numbers")
#write the personal infos in txt first dahil isa lang nase-save pag maraming entry ;(
        personal_infos.write(f"Name: {name}\n")
        personal_infos.write(f"Gender: {gender}\n")
        personal_infos.write(f"Address: {address}\n")
        personal_infos.write(f"Favorite Color: {fav_color}\n")
        personal_infos.write(f"Favorite Song: {fav_song}\n")
        personal_infos.write(f"Age: {age}\n")
        personal_infos.write(f"Contact Number: {number}\n")
        personal_infos.write("\n")

#ask if they want to put another entry/person
        another_input = input("Do you want to put another entry?(yes or no): ")
        if another_input != "yes":
            print("Your Personal Information Has Been Successfully Saved")
            break