
"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example: Input: "tree", Output: "eert" or "eetr".

"
Goal: Apply the hash map + sorting pattern to a string/char context.
"""

# Iterate over string and store the counts of the values inside a hashmap.
# Check if using a Counter can work
# Sort the hashmap items based on the counts
# Iterate over the hashmap
# Add inner loop checking the value of count and put the item in the result
from typing import Counter

def sort_words(word):
    frequency = Counter(word)

    buckets = [[] for _ in range(len(word) + 1)]

    for key, value in frequency.items():
        buckets[value].append(key)

    result = []

    for n in range(len(buckets) - 1, 0, -1):
        for char in buckets[n]:
            result.append(char * n)

    final = "".join(result)
    return final
print(sort_words("tree"))

class SortCharacters:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''

    def sort_words(self):
        hash_map = Counter(self.word)

        sorted_hash = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)

        result = []

        for name, count in sorted_hash:
            for _ in range(count):
                result.append(name)
            # result.append(name * count)
        
        self.sorted_word = "".join(result)
            

# characterClass = SortCharacters('append')
# characterClass.sort_words()

# print(characterClass.sorted_word)
