#Story Generator

import random
from time import sleep

main_character = input("Main character: ")
friend_name = input("Friend's name: ")
action = input("Action you want to perform now (e.g. listening, climbing, singing) : ")
adjective = input("Adjective: ")
adjective2 = input("Second adjective: ")

word1 = ['answer', 'notes', 'book']
word2 = ['seals', 'writers comments', 'music production', 'another scary funeral', 'searching your cat']
word3 = ['rock', 'pop', 'electronic', 'country', 'classical', 'techno']
word4 = ['loved', 'not added', 'generated', 'hated']

sentence = ['Today while watching News and', 'action', ',', 'main_character', 'asked', 'friend_name', 'about', 'word1', 'and about',
            'word2', '. He/She', 'word4', 'it and posted his/her', 'word3', 'article. Then he/she wrote his/her own', 'adjective', 'word1', ', but',
            'friend_name', 'noticed', 'adjective2', 'word1', 'about', 'word2','.']

for item in sentence: #item is the item of the list
    if item == "action":
        sentence[sentence.index(item)] = action #index ---> list[index] = value
    elif item == "main_character":
        sentence[sentence.index(item)] = main_character
    elif item == "friend_name":
        sentence[sentence.index(item)] = friend_name
    elif item == "adjective":
        sentence[sentence.index(item)] = adjective
    elif item == "adjective2":
        sentence[sentence.index(item)] = adjective2
    elif item == "word1":
        sentence[sentence.index(item)] = random.choice(word1)
    elif item == "word2":
        sentence[sentence.index(item)] = random.choice(word2)
    elif item == "word3":
        sentence[sentence.index(item)] = random.choice(word3)
    elif item == "word4":
        sentence[sentence.index(item)] = random.choice(word4)
    else:
        continue

story = " ".join(item for item in sentence)
print("\nStory is generating...\n ")
sleep(3)
print(story)
