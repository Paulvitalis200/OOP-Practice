# Given a non-empty list of words, return the k most frequent elements. 
# If two words have the same frequency, the word with the lower alphabetical order should come first.
# Goal: Practice handling tie-breaking logic in your sorting.

from typing import List

words = ["Don", "Phil", "Sam", "Lawi", "Ken", "Cynthia", "Cynthia", "Don"]

# Create hash map
# Iterate over array and count each word and store it in the hashmap
# Sort hashmap
# If two words have same frequency, check how to sort alphabeticaly

class TopKElements:
    def __init__(self, items: List[str]):
        self.items = items
        self.hash_map = dict()

    def sort(self, k: int):
        for i in range(len(self.items)):
            if self.items[i] not in self.hash_map:
                self.hash_map[self.items[i]] = 1
            else:
                self.hash_map[self.items[i]] += 1

        sorted_words = sorted(self.hash_map.items(), key=lambda x: (-x[1], x[0]))

        return sorted_words[:k]

topK = TopKElements(words)
print(topK.sort(3))

