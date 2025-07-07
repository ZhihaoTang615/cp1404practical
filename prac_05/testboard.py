# from operator import itemgetter
#
# name_and_number = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
# sorted_name_and_number = sorted(name_and_number.items(), key=itemgetter(1), reverse=True)
#
# max_length = max(len(name) for name in name_and_number)
#
# for name, value in sorted_name_and_number:
#     print(f"{name:{max_length}} = {value:{max_length}}")


# def count_words_length(words):
#     return {word: len(word) for word in words}
#
#
# colors = ["red", "blue", "white", "black"]
# color_lengths = count_words_length(colors)
# print(color_lengths)

things = {1, 10, 20, 1, 10}
things.add(20)
print(len(things))