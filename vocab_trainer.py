#-*- coding: UTF-8 -*-

import re
import os
import csv
import time
import sys
import runpy

from tasks.process_list import choose_language

# Choose language to work with
os.system('clear')
print("-----")
print("Welcome to the vocabulary trainer!")
print("-----\n")

language = choose_language()

print("Language is set to {}." .format(language))

stop = False

while stop == False:
	# Choose a function for the language
	print("\n-----")
	print("Main menu")
	print("-----")
	print("\nThis program has seven basic functions.")
	print("- Type 'enter' to enter new words to the list.")
	print("- Type 'edit' to edit words in the list.")
	print("- Type 'test' to train your vocabulary.")
	print("- Type 'backwards' to train your vocabulary backwards.")
	print("- Type 'stats' to print your test statistics.")
	print("- Type 'reset' to reset your test_counts.")
	print("- Type 'switch' to switch the working language.")
	print("\nType 'quit' to exit the program.")

	choice = input("\nWhat do you want to do? ")

	if choice == "enter":
		os.system('clear')
		runpy.run_path("tasks/enter_words.py")
	elif choice == "edit":
		os.system('clear')
		runpy.run_path("tasks/edit_words.py")
	elif choice == "test":
		os.system('clear')
		runpy.run_path("tasks/test_words.py")
	elif choice == "backwards":
		os.system('clear')
		runpy.run_path("tasks/test_backwards.py")
	elif choice == "stats":
		os.system('clear')
		runpy.run_path("tasks/test_stats.py")
	elif choice == "reset":
		os.system('clear')
		runpy.run_path("tasks/reset_counters.py")
	elif choice == "switch":
		os.system('clear')
		language = choose_language()
	elif choice == "quit":
		os.system('clear')
		print("\nOK then, let's call it a day. Bye!\n")
		print("| Vocabulary Trainer v0.4 | Concept & code: Christoph Purschke | Luxembourg 2020 |")
		time.sleep(3)
		os.system('clear')
		stop = True
	else:
		os.system('clear')
		print("\nThis is not an option. Plus, you don't read instructions. Try again.")