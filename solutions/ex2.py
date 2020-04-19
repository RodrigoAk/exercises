'''
Given a string, find the length of the longest substring without repeating
characters
'''


class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        self.length = 0
        self.max_length = 0
        self.sub_s = []
        for element in s:
            if element not in self.sub_s:
                self.sub_s.append(element)
                self.length += 1
            else:
                if(self.length > self.max_length):
                    self.max_length = self.length

                self.sub_s.append(element)
                self.length += 1

                for _ in range(len(self.sub_s)):
                    if(self.sub_s[0] != element):
                        self.sub_s.pop(0)
                        self.length -= 1
                    else:
                        self.sub_s.pop(0)
                        self.length -= 1
                        break

        return self.max_length


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
