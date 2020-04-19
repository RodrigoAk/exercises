class Solution:
  def isValid(self, s):
    self.sub_s = []
    for char in s:
        if(len(self.sub_s) == 0):
            self.sub_s.append(char)
        else:
            if(char == ')'):
                if(self.sub_s[-1] == '('):
                    self.sub_s.pop(-1)
                else:
                    return False
            elif(char == ']'):
                if(self.sub_s[-1] == '['):
                    self.sub_s.pop(-1)
                else:
                    return False
            elif(char == '}'):
                if(self.sub_s[-1] == '{'):
                    self.sub_s.pop(-1)
                else:
                    return False
            else:
                self.sub_s.append(char)
    if(len(self.sub_s) != 0):
        return False
    else:
        return True

                

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
