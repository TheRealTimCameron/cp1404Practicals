
# FIRST SECTION

file_name = open('name.txt', 'w')
name = str(input("What do they call you by? "))
print(name, file = file_name)
file_name.close()



file_name = open('name.txt', 'r')
first_line = file_name.readline()
print("Your name is {}".format(first_line))
file_name.close()








# SECOND SECTION

# file_name = open('numbers.txt', 'r')
# all_lines = file_name.readlines()
# first_line = int(all_lines[0].strip())
# second_line = int(all_lines[1].strip())
# total = first_line + second_line
# print(total)
# file_name.close()