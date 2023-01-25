
def isValid(s):
        stack = []       
        mapping = {'(':')','[':']','{':'}'}
        for char in s:
            if char in mapping.keys():
                stack.append(mapping[char])
            elif not stack or stack[-1]!=char:
                print('stack not',stack[-1]!=char)

                return False
            else:
                stack.pop()
        return len(stack)==0
s = "(}"
isValid(s)        