# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


file2 = open("/Users/MrAvarice/PycharmProjects/Mail Merge Project Start/input/Names/invited_names.txt")
names = file2.readlines()

print(names)
for name in names:
    with open("/Users/MrAvarice/PycharmProjects/Mail Merge Project Start/input/Letters/starting_letter.txt", mode='r') as f:
        ff = f.read(12)
        ff3 = ff.replace('Dear [name],', f"Dear {name}")
        # print(ff)
        ff2 = f"{ff3} {f.read()}\n"
        with open("/Users/MrAvarice/PycharmProjects/Mail Merge Project Start/Output/ReadyToSend/example.txt", mode="a") as files:
            contents = files.write(ff2)
            print(contents)



# f = open("/Users/MrAvarice/PycharmProjects/Mail Merge Project Start/input/Letters/starting_letter.txt")
# ff = f.read()
# ff[0] = "Dear Randy,\n"
# ff.remove('\n')
#
# print(ff)

# with open("/Users/MrAvarice/PycharmProjects/Mail Merge Project Start/input/Names/invited_names.txt") as file2:
#     name_contents = file2.readlines()
#
# print(name_contents[0])
#

# for name in name_contents:
#     ff[0] = f"Dear {name}"
#     with open("/Users/MrAvarice/PycharmProjects/Mail Merge Project Start/Output/ReadyToSend/example.txt", 'a') as file3:
#         file3.write(f"{f}\n")
#         print(contents)
#     print(ff[0])
#
# with open("/Users/MrAvarice/PycharmProjects/Mail Merge Project Start/Output/ReadyToSend/example.txt") as file4:
#     print(file4.read())
# my_list = [1, 2, 3, 4, 5]
