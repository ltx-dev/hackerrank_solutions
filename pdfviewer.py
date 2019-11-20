#
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# Make it shorter
#
user_input = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7".split(' ')
letter_list = list(map(chr, range(97,123))) # keys
letter_heights = [int(char) for char in user_input ] # values

letter_dictionary = dict(zip(letter_list, letter_heights))

word = "abc"
highest = 0

for char in word:
	if letter_dictionary[char] > highest:
		highest = letter_dictionary[char]

answer = len(word) * highest
print(answer)