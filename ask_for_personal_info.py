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
                number = int(input("Contact Number: 09"))
                break
            
            except: 
                print("Please input valid numbers")
#ask if they want to put another entry/person
#write the personal infos in txt 