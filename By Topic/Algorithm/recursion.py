# 273	Integer to English Words	30.6%	Hard
"""
Convert a non-negative integer num to its English words representation.
"""
def integerToEnglish(num):
    to_19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    thousand = 'Thousand Million Billion'.split()

    def word(n, idx=0):
        if n == 0:
            return []
        if n < 20:
            return [to_19[n-1]]
        if n < 100:
            return [tens[n//10-2]] + word()
        if n < 1000:
            return [thousand[n//100-1]] + ['Hundred'] + word(n%100)
        p, reminder = n//1000, n%1000
        space = [thousand[idx]] if p%1000 != 0 else []
        return word(p, idx+1) + space + word(reminder)
    return ' '.join(word(num)) or 'Zero'

# 50	Pow(x, n)	34.8%	Medium

# 21	Merge Two Sorted Lists	64.3%	Easy	
# 231	Power of Two	47.8%	Easy	
# 224	Basic Calculator	43.4%	Hard	
# 206	Reverse Linked List	76.5%	Easy	
# 394	Decode String 59.2%	Medium	
# 143	Reorder List 58.7%	Medium	
# 772	Basic Calculator III 50.6%	Hard	
# 234	Palindrome Linked List	53.2%	Easy	
# 509	Fibonacci Number	71.0%	Easy	
# 10	Regular Expression Matching