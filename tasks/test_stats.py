#-*- coding: UTF-8 -*-

from __main__ import *
from tasks.process_list import *
from operator import itemgetter

word_list = input_list(language)

if len(word_list) > 0:
	runs_total = max([int(item['test_count']) for item in word_list])
	correct_answers = sum([int(item['correct_count']) for item in word_list])
	wrong_answers = sum([int(item['wrong_count']) for item in word_list])
	top_correct = sorted(word_list, key=itemgetter('correct_count'), reverse=True)
	top10_correct = ', '.join(map(str, [item["word"] for item in top_correct[:10]]))
	top_wrong = sorted(word_list, key=itemgetter('wrong_count'), reverse=True)
	top10_wrong = ', '.join(map(str, [item["word"] for item in top_wrong[:10]]))
	
	if runs_total > 0:
		print("Here is your test statistics for {}." .format(language))
		print("\n-----")
		print("Number of words in list: {}" .format(len(word_list)))
		print("- Number of test runs total:{}" .format(runs_total))
		print("- Number of correct answers: {}" .format(correct_answers))
		print("- Number of wrong answers: {}" .format(wrong_answers))
		print("\n-----")
		print("- Top 10 correct words: {}" .format(top10_correct))
		print("- Top 10 wrong words: {}" .format(top10_wrong))
		print("\n-----")
		input("That's all for now. Hit enter to return to the main menu. ")
		os.system('clear')
	elif runs_total == 0:
		print("There are no stats available for {} yet. You need to train some words first." .format(language))
		print("\n-----")
		input("That's all for now. Hit enter to return to the main menu. ")
		os.system('clear')
elif len(word_list) == 0:
	print("There are no words available for {} yet. You need to enter some first." .format(language))
	print("\n-----")
	input("That's all for now. Hit enter to return to the main menu. ")
	os.system('clear')