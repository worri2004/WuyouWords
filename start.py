import random
import csv

def load_word_file():
	word_list = []
	with open('words.csv', 'r') as csvfile:
		content = csv.reader(csvfile)
		for i in content:
			word_list.append(tuple(i))
	return word_list

# a = load_word_file()
# print(a)

def examination():
	word_list = load_word_file()
	examination_quantity = 100
	if len(word_list) < examination_quantity:
		examination_quantity = len(word_list)
	for english_word, chinese_word in random.sample(word_list, examination_quantity):
		print('\n')
		print(chinese_word)
		answer = input('请拼写出这个单词的英文?(请用小写，大写算错)   ')
		if answer == english_word:
			print('你答对了！')
		else:
			append_word(english_word, chinese_word)
			print('你错了，正确的答案是：', english_word)

def append_word(english_word, chinese_word):
	with open('words.csv', 'a', newline = '') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([english_word, chinese_word])


if __name__ == '__main__':
	examination()
