#-*- coding: UTF-8 -*-

from __main__ import *
from tasks.process_list import *
import random

# Set word list for language
input_list = input_list(language)

# Define test set to work with
print("\nYou can choose different options for testing.")
print("- Type 'all' to use the entire word list.")
print("- Type 'latest' to use the latest additions to the list.")
print("- Type 'errors' to use the words you got wrong the most.")
print("- Type 'rare' to use the least tested words in the list.")

choice = input("\nWhich dataset do you want to test? ")

word_list = (filter_list(choice, input_list))
random.shuffle(word_list)

os.system("clear")

if len(word_list) > 0:
	# Run test round for 25 items based on filtered list
	
	if len(word_list) < 25:
		test_range = len(word_list)
	else:
		test_range = 25
	
	item_counter = 0
	wrongs = 0
	corrects = 0
	wrong_list = []
	
	print("OK. Let's see how many words you remember.")
	print("You will have to translate {} words from {}." .format(test_range, language))
	
	while item_counter < test_range:
		for testitem in word_list:
			try_count = 1
			tested = False
			while tested == False:
				typed_word = input("\nWhat is the meaning of '{}'? " .format(testitem["word"]))
				if typed_word == testitem["target"]:
					corrects += 1
					testitem["correct_count"] = int(testitem["correct_count"]) +1
					tested = True
					print("\nThat is correct. Let's try the next one!\n")
				else:
					if try_count < 2:
						try_count += 1
						print("That is incorrect. Try again!")
					elif try_count == 2: 
						try_count += 1
						print("Here's a tip: %s" % (testitem["hint"]))
					elif try_count == 3: 
						wrong_list.append(testitem["target"])
						wrongs += 1
						testitem["wrong_count"] = int(testitem["wrong_count"]) +1
						tested = True
						print("No, the solution is: '%s'." %(testitem["target"]))
			testitem["test_count"] = int(testitem["test_count"]) +1
			item_counter +=1
			print("{} of {} items tested." .format(str(item_counter), test_range))
		if item_counter == len(word_list):
			print("\n-----")
			print("That's all. You have tested all words in the list.")
			print("Try adding some new words.")
			break

	# Print evaluation for test round
	print("\n-----")
	print("Here's your evaluation for the last run:")
	print("Correct items: {} of {}." .format(str(corrects), str(item_counter)))
	print("Wrong items: {} of {}." .format(str(wrongs), str(item_counter)))
	
	# Run extra recap round for words with errors
	if len(wrong_list) > 0:
		os.system("clear")
		print("\n-----")
		print("There were some words you didn't know. Let's recapitulate them.\n")
		recap_list = [item for item in word_list if item["word"] in wrong_list]
		recap_counter_counter = 0
	
		for capitem in recap_list:
			cap_count = 1
			typed_word = input("What is the meaning of '{}'? " .format(capitem["word"]))
			if typed_word == capitem["target"]:
				print("That is correct. Let's try the next one!")
			else:
				print("No, the solution is: '%s'." %(testitem["target"]))
	
	# Write modified list back to file
	output_list(word_list, language)
	
	print("\n-----")
	input("That's all for now. Hit enter to return to the main menu. ")
	os.system('clear')
elif len(word_list) == 0:
	print("\nThere are no words available for {} yet. You need to enter some first." .format(language))
	print("\n-----")
	input("That's all for now. Hit enter to return to the main menu. ")
	os.system('clear')