"""
find the max substring. ex: 'baca', all substrings: [b, ba, bac, baca, a, ac, aca, c, ca]
after sort, 
"""

def max_substring(s):
    if s is None or len(s) == 0:
        return ""
    max_str = ""
    for i in range(len(s)):
        for j in range(len(s)):
            #print("------")
            #print("i", i)
            #print("j", j)
            cur_str = s[i:j+1]
            #print("cur str: ", cur_str)
            #print("max str: ", max_str)
            if cur_str > max_str:
                max_str = cur_str
            #print("new max str: ", max_str)
    return max_str

test1_str = 'baca'
#print(max_substring(test1_str))


"""

    Calculates the minimum number of request code flips required to create
    non-overlapping, even-length segments of identical request codes.
    
    This solution achieves O(n) time complexity by processing the string
    in pairs, which is proven to be optimal for this specific problem.
    
    Args:
        requestSeq (str): Binary string of '0's and '1's
        
    Returns:
        int: Minimum number of bit flips required, or -1 if invalid input

"""
def minRequestFlips(requestSeq):
    if not requestSeq:
        return 0
    n = len(requestSeq)
    if n % 2 != 0:
        return -1
    total_flips = 0
    for i in range(0, n, +2):
        segment = requestSeq[i:i+2]
        #print(segment)
        flips_to_zeros = segment.count('1')
        flips_to_ones = segment.count('0')

        total_flips = min(flips_to_ones, flips_to_zeros)
    return total_flips
print(minRequestFlips("11010010"))