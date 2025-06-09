name = input("Enter your name: ")
in_file = open("name.txt", "w")
in_file.write(name)
in_file.close()



in_file = open("name.txt", "r")
name_from_file = in_file.readline()
in_file.close()
print(f"Hi {name_from_file}")


with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
    print(first_number + second_number)

total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line)


print(total)