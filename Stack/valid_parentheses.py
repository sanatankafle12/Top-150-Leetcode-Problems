class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dictionary = {")":"(", "}":"{", "]":"["}

        stack_of_parentheses = []

        for i in s:
            if i in parentheses_dictionary.values():
                stack_of_parentheses.append(i)
            elif i in parentheses_dictionary.keys():
                if not stack_of_parentheses or parentheses_dictionary[i] != stack_of_parentheses.pop():
                    return False
                
        return True