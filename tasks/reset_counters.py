#-*- coding: UTF-8 -*-

from __main__ import *
from tasks.process_list import *

# Set list of words for language
word_list = input_list(language)


print("- Type 'all' to reset all counters.")
print("- Type 'test' to reset the counter for the number of tests.")
print("- Type 'eval' to reset the counters for correct/wrong answers.")
print("Hit 'enter' to return to the main menu. ")

# Choose counters to reset
stop = False

while stop != True:
	call = input("\nWhat do you want to reset? ")
	for item in word_list:
		if call == "all":
			item["test_count"] = int(0)
			item["correct_count"] = int(0)
			item["wrong_count"] = int(0)
			stop = True
		elif call == "test":
			item["test_count"] = int(0)
			stop = True
		elif call == "eval":
			item["correct_count"] = int(0)
			item["wrong_count"] = int(0)
			stop = True
		elif call == "":
			stop = True

# Write modified list back to file
output_list(word_list, language)

print("\n-----")
print("Done! Now you have a fresh start for testing {}." .format(language))
input("Hit enter to return to the main menu. ")
os.system('clear')