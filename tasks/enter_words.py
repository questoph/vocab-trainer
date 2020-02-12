#-*- coding: UTF-8 -*-

from __main__ import *
from tasks.process_list import *
import datetime

# Set word list for language
word_list = input_list(language)

# Set ID for entry counting
if len(word_list) == 0:
	last_id = 0
else:
	last_id = max([item['id'] for item in word_list])

# Collect all words in list to check for double entries
list_of_words = [ent["word"] for ent in word_list]

print("\n-----")
print("You can add as many new words as you want.")
print("To stop entering mode type 'quit' instead of hitting enter.\n")

# Add a new item to the word_list
stop = False

while stop == False:
	new_item = {}
	new_item["word"] = input("\nWhat is the new word? ")

	if new_item["word"] in list_of_words:
		print("\nThis item is already in your list, see?\n")
		double_entry = [item for item in word_list if new_item["word"] in item["word"]]
		print("Word: {}" .format(double_entry[0]["word"]))
		print("Translation: {}" .format(double_entry[0]["target"]))
		print("Hint: {}" .format(double_entry[0]["hint"]))
		print("\nIf you want to change this entry, enter the 'edit' mode in the main menu.\n")
		continue
	else:
		new_item["target"] = input("What is the new translation? ")
		new_item["hint"] = input("What is the new hint? ")
		new_item["id"] = int(last_id) + 1
		new_item["date_entered"] = datetime.date.today()
		new_item["test_count"] = int(0)
		new_item["correct_count"] = int(0)
		new_item["wrong_count"] = int(0)
		word_list.append(new_item)
		last_id = int(last_id) +1
	
	stop_trigger = input("Another one? Just hit enter. ")
	if stop_trigger == "quit":
		stop = True

# Write modified list back to file
output_list(word_list, language)

print("\n-----")
input("Well, that's all for now. Hit enter to return to the main menu. ")
os.system('clear')