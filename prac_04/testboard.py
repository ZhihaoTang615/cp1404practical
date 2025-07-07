# # names = ["Ada","Alan","Bill","John"]
# #
# # print(",".join(names))
# # name_to_remove = input("who do you want to remove?").strip()
# # while name_to_remove != "":
# #     try:
# #         names.remove(name_to_remove)
# #         print(f"{name_to_remove} was removed")
# #     except ValueError:
# #         print(f"Error: '{name_to_remove}' is not in the list.")
# #     print(names)
# #     name_to_remove = input("who do you want to remove?")
# #
# # print("good try")
# #
#
# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
# def get_numbers():
#     text = input("Enter numbers separated by spaces: ")
#     numbers = text.split(',')
#     return numbers
#
# def square_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = float(numbers[i]) ** 2
# # numbers = [float(numbers[i])] ** 2 for in range(len(numbers))]
#
# def display_numbers(numbers):
#     print("..".join([str(number) for number in sorted(numbers)]))
#
# main()




# from operator import itemgetter
# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
# max_length = max(len(name[0]) for name in data)
# print(max_length)
#
# data.sort(key=itemgetter(1), reverse=True)
#
# for name, score in data:
#     print(f"{name:{max_length}} = {score:{max_length}}")


# words = ["aye", "bee", "sea", "bee"]
# words.remove("bee")
# print(words.pop(0))
# print(words)

#
# things = list("one two three")
# print("{}-{}".format(*things))


print("*".join([len(word) for word in "one*two*three".split('*')]))
