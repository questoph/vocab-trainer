#-*- coding: UTF-8 -*-

from __main__ import *
from tasks.process_list import *

from prettytable import PrettyTable

# Set word list for language
word_list = input_list(language)

edit_list = sorted(word_list, key=lambda x: x['word'].lower(), reverse=False)
chunk_list = [edit_list[i:i + 20] for i in range(0, len(edit_list), 20)]

print("Welcome to the dictionary editor.")

stop = 0
words_to_update = []
words_to_delete = []

while stop < len(chunk_list):
	for sublist in chunk_list:
		stop +=1
		done = False
		while done == False:
			plist = PrettyTable()
			plist.field_names = ["id", "word", "translation", "hint"]
			plist.align["word"], plist.align["translation"], plist.align["hint"] = "l", "l", "l"
			for entry in sublist:
				plist.add_row([entry["id"], entry["word"], entry["target"], entry["hint"]])
			print("\nEnter the id to edit the respective entry.")
			print("Hit enter to continue scrolling through the list.")
			print("Type 'quit' to exit the editor.\n")
			print(plist)
			print("\n-----")
			word = input("Which word do you want to edit?: ")
			if word == "":
				done = True
				os.system('clear')
			elif word == "quit":
				os.system('clear')
				break
			else:
				os.system('clear')
				for el in sublist:
					if el["id"] == word:
						pos = sublist.index(el)
					else: 
						pass
				print(plist.get_string(start=int(pos), end=int(pos)+1))
				print("\nEnter the new text or hit enter to skip the column.")
				print("Type 'del word' to delete the entry from the list.\n" )
				for ent in sublist:
					if ent["id"] == word:
						ed_entry = ent 
				w_edit = input("Type the new word: ")
				if w_edit == "":
					pass
				elif w_edit == "del word":
					words_to_delete.append(ed_entry)
					sublist.remove(ed_entry)
					continue
					os.system("clear")
				else: 
					ed_entry["word"] = w_edit
				t_edit = input("Type the new translation: ")
				if t_edit == "":
					pass
				else: 
					ed_entry["target"] = t_edit
				h_edit = input("Type the new hint: ")
				if h_edit == "":
					pass
				else: 
					ed_entry["hint"] = h_edit
				words_to_update.append(ed_entry)
			os.system('clear')

print("\n-----")
print("Editing finished.")
input("Hit enter to return save changes and to the main menu.")

if len(words_to_update) == 0 and len(words_to_delete) == 0:
	pass
else:
	for item in word_list:
		for entry in words_to_delete:
			if entry["id"] == item["id"]:
				word_list.remove(item)
		for entry in words_to_update:
			if entry["id"] == item["id"]:
				update_pos = word_list.index(item)
				word_list.remove(item)
				word_list.insert(update_pos, item)
	output_list(word_list, language)

os.system('clear')