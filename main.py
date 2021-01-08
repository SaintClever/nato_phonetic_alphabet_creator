import pandas as pd


data = pd.read_csv('assets/nato_phonetic_alphabet.csv')
# print(data)

nato = {row['letter']:row['code'] for (index,row) in data.iterrows()}
# print(nato)

user_word = input('\nPlease enter a word: ').upper()

nato_output = [nato[letter] for letter in user_word if letter in nato.keys()]
print(f'\n{nato_output}\n')