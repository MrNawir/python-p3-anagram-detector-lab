# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        matches = []
        target = sorted(self.word.lower())
        for candidate in candidates:
            if sorted(candidate.lower()) == target and candidate.lower() != self.word.lower():
                matches.append(candidate)
        return matches
