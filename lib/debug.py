#!/usr/bin/env python3

from anagram import Anagram

if __name__ == '__main__':
    word1 = Anagram("listen")
    word2 = "silent"
    word3 = "hello"
    word_list = ["enlist", "inlets", "hit", "stink", "tones", "silent"]

    print(f"Is '{word1.word}' a valid word? {word1.is_valid_word()}")
    print(f"Is '{word2}' an anagram of '{word1.word}'? {word1.is_anagram(word2)}")
    print(f"Sorted word for '{word1.word}': {word1.get_sorted_word()}")
    print(f"Matching anagrams for '{word1.word}' in the list: {word1.match(word_list)}")

    # Start debugging session with ipdb
    import ipdb; ipdb.set_trace()

