#ask for full name, address, gender, hobbies, favorite color, favorite song, age, number
with open("./output.txt", "a") as personal_infos:
    while True:
            
        name = input("Name: ")
        gender = input("Gender: ")
        address = input("Address: ")
        fav_color = input("Favorite Color: ")
        fav_song = input("Favorite Song: ")
        age = int(input("Age: "))
        number = int(input("Contact Number: "))
#check for errors for input age and number
#ask if they want to put another entry/person
#write the personal infos in txt 