#def search function
def personal_info(file):
#read entire output
    with open("./output.txt", "r") as personal_infos:
        entries = (personal_infos.readlines())
        for entry in entries:
            print(entry.strip())
    #use loop for searching
        #except print "file not found if name is not in txt file"
file = "./output.txt"
personal_info(file)