# your class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [word for word in word_list if self.is_anagram(word)]

    def is_anagram(self, other_word):
        other_word = other_word.lower()
        return sorted(self.word) == sorted(other_word)

    def get_sorted_word(self):
        return ''.join(sorted(self.word))

    def is_valid_word(self):
        # Add custom validation logic for a valid word
        return len(self.word) > 1

# Example usage:
word1 = Anagram("listen")
word2 = "silent"
word3 = "hello"
word_list = ["enlist", "inlets", "hit", "stink", "tones", "silent"]

print(f"Is '{word1.word}' a valid word? {word1.is_valid_word()}")
print(f"Is '{word2}' an anagram of '{word1.word}'? {word1.is_anagram(word2)}")
print(f"Sorted word for '{word1.word}': {word1.get_sorted_word()}")
print(f"Matching anagrams for '{word1.word}' in the list: {word1.match(word_list)}")
code goes here!
