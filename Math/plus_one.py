class Solution:
    def plusOne(self, digits):
        num_str =''
        for i in digits:
            num_str+=str(i)
        
        string_list = list(str(int(num_str)+1))    
        return ([int(x) for x in string_list])