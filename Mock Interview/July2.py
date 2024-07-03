# (ADD 3 4)
# (ADD (ADD 3 4) (MULT 4 6))
def parseExpression(s):
    stack = []
    num = ""
    operation = ""

    for char in s:
        if char == "(":
            continue
        elif char.isalpha():
            operation += char
        elif char.isdigit():
            num += char
        elif char == " ":
            if num:
                stack.append(int(num))
                num = ""
            if operation:
                stack.append(operation)
                operation = ""
        elif char == ")":
            #print(stack)
            tmp = 0
            n2 = stack.pop()
            n1 = stack.pop()
            op = stack.pop()
            if op == "ADD":
                tmp = n1 + n2
            if op == "MULT":
                tmp = n1 * n2
            stack.append(tmp)
    #print(stack)
    return stack[0]
#print(parseExpression("( ADD 3 4 )"))
#print(parseExpression("( ADD 13 4 )"))
#print(parseExpression("(ADD ( ADD 3 4 ) ( MULT 3 4 ) )"))
#print(parseExpression("( MULT 3 4 )"))
#print(parseExpression("(ADD ( ADD ( MULT 1 2 ) 4 ) ( MULT 3 4 ) )"))
"""

"""
dic_one = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
dic_less_20 = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

dic_tens = {
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fitfy",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def integerToEnglish(num):
    result = ""
    ten = num // 10
    rest = num % 10
    if ten:
        result += dic_one[ten]
    return