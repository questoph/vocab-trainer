# Vocabulary trainer

This is a demonstration project developed in the context of the class "Computing culture. An introduction to Python programming for the humanities". It is built as a combination of scripts written in Python 3.7. The program can be used to enter, edit, and train words in different languages. For now, it runs completely in your shell.

## Functions

- **Enter:** Add new words with translations and example phrases
- **Edit:** Change and delete existing entries in the word list
- **Test:** Train 25 words translating to the target language
- **Test backwards:** Test 25 words translating from the target language
- **Stats:** Display and reset your test statistics 
- **Languages:** Manage word list for different languages

The test modes offer different possibilities for testing:

- Use the entire word list
- Use the latest additions to the list
- Use the words you got wrong the most
- Use the least tested words in the list

## Use

To use the vocabulary trainer, clone the repo, enter the main directory, and run the following command in your shell:

``pip install -r requirements.txt``

The following external libraries will be installed: *glob*, *prettytable*.

After the installation, simply run the following command in your shell:

``python vocab_trainer.py``

## To do

I am currently thinking about additional fields for the word list that could be useful for training and documentation of words. Plus, I might try and add a simple GUI.
