class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
          my_array = [0] * 26
          word_seen = {}
          for word in strs:
            for chara in word:
                position = ord(chara) - ord("a")
                my_array[position] += 1
            key_tuple = tuple(my_array)
            if key_tuple in word_seen:
                word_seen[key_tuple].append(word)
            else:
                word_seen[key_tuple] = [word]
            my_array = [0] * 26
          result = list(word_seen.values())
          return result
         
          