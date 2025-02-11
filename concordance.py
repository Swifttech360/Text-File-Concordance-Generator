"""
Author: Miles Butler

Publish Date: 2/11/25

Overview:
This Python program opens a test file within the program's working directory based on a user input.
Then, the program displays a list of every word within the file's text, along with each word's number of occurrences.
"""

while True:
    seenText = []
    fileSelection = input('Please select a local text file:  ')
    if "." not in fileSelection:
        print('\nInvalid Input.\n'
              "Be sure to include the file's add in all inputs (i.e., .txt, .rtf, .md).")
        continue
    try:
        text = open(fileSelection, 'r').read()
    except FileNotFoundError:
        print('File Not Found\n'
              "This file could not be found this program's working directory.\n"
              "Please try again.\n")
        continue
    print('\nFile Text:\n'
          '' + text)

    #remove all punctuation from text for text identification accuracy
    text = text.replace('.', '').replace('?', '').replace \
        ('!', '').replace(',', '').replace \
        ('-', ' ').replace(';', '')

    splitText = text.split()
    #print(f'\nSplit Text:\n{splitText}')

    for i, currentWord in enumerate(splitText):
        if currentWord not in seenText:
            seenText.append(currentWord)
    sortedSeenText = sorted(seenText, key=lambda x: x.upper())
    #print('\nSorted text instances:\n'+ str(sortedSeenText))
    print()
    print(f'{fileSelection} Word Frequency:')
    for currentWord in sortedSeenText:
        print(f"{currentWord}: {splitText.count(currentWord)}")
    print()
