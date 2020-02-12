#-*- coding: UTF-8 -*-

from __main__ import *
from operator import itemgetter
import csv
import glob

# Function to define the input list for testing
def input_list(language):
	input_list = []
	with open("languages/{}.csv" .format(language), "r") as input_csv:
		rowdata = csv.DictReader(input_csv, delimiter=';')
		for row in rowdata:
			input_list.append(row)
	return input_list

# Function to filter the word list based on different criteria
def filter_list(choice, inputlist):
	if choice == "all":
		filter_list = inputlist
		return filter_list
	elif choice == "latest":
		id_filter = sorted(inputlist, key=itemgetter('id'), reverse=True)
		filter_list = id_filter[:25]
		return filter_list
	elif choice == "errors":
		wrong_filter = sorted(inputlist, key=itemgetter('wrong_count'), reverse=True)
		filter_list = wrong_filter[:25]
		return filter_list
	elif choice == "rare":
		test_filter = sorted(inputlist, ey=itemgetter('test_count'), reverse=False)
		filter_list = test_filter[:25]
		return filter_list

# Function to write the modified word list back to file
def output_list(output, language):
	with open("languages/{}.csv" .format(language), 'w') as output_csv:
		if len(output) > 0:
			keys = output[0].keys()
		else: 
			keys = ["id", "word", "target", "hint", "date_entered", "test_count", "correct_count","wrong_count"]
		dict_writer = csv.DictWriter(output_csv, keys, delimiter=';')
		dict_writer.writeheader()
		dict_writer.writerows(output)

# Add new language list
def new_list (name):
	with open("languages/{}.csv" .format(name), 'w') as new_csv:
		keys = ["id", "word", "target", "hint", "date_entered", "test_count", "correct_count","wrong_count"]
		dict_writer = csv.DictWriter(new_csv, keys, delimiter=';')
		dict_writer.writeheader()
		return new_csv

# Switch language for testing
def choose_language():
	# Look up languages
	langsearch = glob.glob("languages/*.csv")
	langlist = [re.search(r"/([^']*).csv", item).group(1) for item in langsearch]
	
	print("\nWhat language do you want work on today?")
	print("\nThese languages are already in the database: {}" .format(', '.join(map(str, langlist))))
	
	lang_choice = False
	while lang_choice == False:
		language = input("\nType the name of the language to start. ")
		if language in langlist:
			os.system('clear')
			lang_choice = True
		else:
			print("\nThis language does not exist yet.")
			new = input("Type 'yes' to add it as new language and 'no' to retry. ")
			if new == "yes":
				new_list(language)
				os.system('clear')
				lang_choice = True
			elif new == "no":
				continue
			else:
				print("Not a valid option. Please retry.")
	return language