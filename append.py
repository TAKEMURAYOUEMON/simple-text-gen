from random import choice

results = []

with open("first_array.txt", "r") as file_first_array:
	first_array = (file_first_array.read()).split("\n")

with open("second_array.txt", "r") as file_second_array:
	second_array = (file_second_array.read()).split("\n")

enter_space = input("Enter the space?(y or n): ")
if enter_space == "y":
	enter_space = " "
elif enter_space == "n":
	enter_space = ""

for _ in range(10000):
	results.append(choice(first_array) + enter_space + choice(second_array) + "\n") 

result_filtered = list(set(results))

with open("RESULT.txt", "w") as result_file:
	for result in result_filtered:
		result_file.write(result)

