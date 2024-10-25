import json

"""
Ensure there is a file named 'french_list.txt' in the root directory of this script.
Example of 'french_list.txt' can be found here: https://www.freelang.com/dictionnaire/dic-francais.php#google_vignette
"""

with open("french_list.txt", "r", encoding="latin-1") as f:
    words = f.read().splitlines()

words_no_capital = [word for word in words if not word[0].isupper()]

with open("filtered_words.json", "w", encoding="utf-8") as f:
    json.dump(words_no_capital, f, ensure_ascii=False, indent=4)

print("Filtered words have been saved to 'filtered_words.json'.")
