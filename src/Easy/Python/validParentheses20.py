class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        i = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                brackets.append(s[i])
            else:
                if not brackets:
                    return False
                top = brackets.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False
        return len(brackets)==0
