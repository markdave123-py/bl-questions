# Given a dictionary of words and an input string without spaces, write a method that returns a string with spaces inserted correctly.

# Example:

# Input:  "bloombergisfun"
# Dict:   ["bloom", "bloomberg", "is", "fun"]
# Output: "bloomberg is fun"

class Solution:
    def insertSpaces(self, s: str, wordDict: list[str]) -> str:
        
        def dfs(i):
            if i == len(s):
                return []           

            for word in wordDict:
                L = len(word)
                if s[i:i+L] == word:
                    sub = dfs(i + L)
                    if sub is not None:
                        return [word] + sub   

            return None  

        words = dfs(0)
        return " ".join(words) if words is not None else ""

    def insertSpaces(self, s: str, wordDict: list[str]) -> str:
        memo = {}  # maps index - list of words if success, or None if dead end

        def dfs(i):
            if i in memo:
                return memo[i]

            # Reached end of string - valid segmentation
            if i == len(s):
                return []

            for word in wordDict:
                L = len(word)

                if s[i:i+L] == word:
                    sub = dfs(i + L)
                    if sub is not None:           # success continuation
                        memo[i] = [word] + sub    # store in memo
                        return memo[i]

            memo[i] = None  # mark this index as unsplittable
            return None

        words = dfs(0)
        return " ".join(words) if words else ""
