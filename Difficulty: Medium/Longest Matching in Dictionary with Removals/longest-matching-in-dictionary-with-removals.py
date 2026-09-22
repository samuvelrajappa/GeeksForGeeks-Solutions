from collections import defaultdict

class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # Group words by their first character
        waiting = defaultdict(list)
        for word in d:
            if word:
                waiting[word[0]].append((word, 0))

        best_word = ""

        # Advance pointers as we scan s once
        for char in s:
            if char in waiting:
                current_words = waiting[char]
                del waiting[char]

                for word, i in current_words:
                    if i + 1 == len(word):
                        # Word is fully matched; update best result
                        if len(word) > len(best_word) or (len(word) == len(best_word) and word < best_word):
                            best_word = word
                    else:
                        # Move word to the bucket for its next required character
                        waiting[word[i + 1]].append((word, i + 1))

        return best_word
