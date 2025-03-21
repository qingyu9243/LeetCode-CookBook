from typing import List
def process_strings(string_array):
    """
    Process an array of strings with the following rules:
    - If string length is odd, reverse the string
    - If string length is even, convert to lowercase
    
    Args:
        string_array (list): List of strings to process
        
    Returns:
        list: Processed list of strings
    """
    result = []
    
    for s in string_array:
        if len(s) % 2 == 1:  # Odd length
            result.append(s[::-1])
        else:  # Even length
            result.append(s.lower())
            
    return result

# Example usage for string processing
test_strings = ["Hello", "World", "Python", "Programming", "Test"]
processed_strings = process_strings(test_strings)
print("Original strings:", test_strings)
print("Processed strings:", processed_strings)
#################################################################################

def reduce_to_single_digit(num):
    while num > 9:
        digit_sum = 0
        temp = num
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        num = digit_sum
    return num

def process_number_array(numbers):
    """
    Process an array of numbers:
    1. Reduce each number to a single digit
    2. Find the most frequent digit in the resulting array
    
    Args:
        numbers (list): List of numbers to process
        
    Returns:
        tuple: (most_frequent_digit, frequency, single_digits)
    """
    # Reduce each number to a single digit
    single_digits = [reduce_to_single_digit(num) for num in numbers]
    
    # Count frequency of each digit
    digit_counts = {}
    for digit in single_digits:
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1
    
    # Find the most frequent digit
    most_frequent = None
    max_count = 0
    
    for digit, count in digit_counts.items():
        if count > max_count:
            max_count = count
            most_frequent = digit
    
    return most_frequent, max_count, single_digits

test_numbers = [38, 27, 156, 82, 19, 734, 251, 9, 463]
most_frequent, frequency, single_digits = process_number_array(test_numbers)
print("\nOriginal numbers:", test_numbers)
print("Reduced to single digits:", single_digits)
print(f"Most frequent digit: {most_frequent}, appears {frequency} times")

#################################################################################
def rotate_matrix_around_diagonal(matrix, rotations):
    """
    Rotate a matrix around its main diagonal, keeping diagonal elements fixed.
    
    Args:
        matrix: A square matrix (2D list)
        rotations: Number of 90-degree clockwise rotations
    
    Returns:
        Rotated matrix
    """
    n = len(matrix)
    # Create a deep copy of the original matrix
    result = [row[:] for row in matrix]
    
    # Normalize rotations (4 rotations = 360 degrees = same as original)
    rotations = rotations % 4
    
    # If no rotation needed or complete 360-degree rotation
    if rotations == 0:
        return result
    
    # Apply rotations
    for _ in range(rotations):
        # Create a new matrix for this rotation
        new_matrix = [row[:] for row in result]
        
        # Perform one 90-degree clockwise rotation
        for i in range(n):
            for j in range(n):
                # Skip diagonal elements (where i == j)
                if i == j:
                    continue
                
                # For rotation around the main diagonal:
                # (i,j) -> (j,i) in a transposition
                # But we need to handle proper orientation based on quadrants
                new_matrix[j][i] = result[i][j]
                
        # Update the result for the next rotation
        result = new_matrix
    
    return result

def print_matrix(matrix):
    """Print a matrix in a readable format"""
    for row in matrix:
        print(" ".join(str(x) for x in row))
    print()

# Example usage
test_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Original matrix:")
print_matrix(test_matrix)

rotated_once = rotate_matrix_around_diagonal(test_matrix, 1)
print("After 1 rotation:")
print_matrix(rotated_once)

rotated_twice = rotate_matrix_around_diagonal(test_matrix, 2)
print("After 2 rotations:")
print_matrix(rotated_twice)

#################################################################################

def find_one_digit_different_pairs(numbers):
    """
    Find all pairs of numbers where exactly one digit differs.
    
    Args:
        numbers: List of integers
    
    Returns:
        List of pairs (tuples) where digits differ in exactly one position
    """
    result = []
    n = len(numbers)
    
    # Convert all numbers to strings for easier digit comparison
    str_numbers = [str(num) for num in numbers]
    
    # Check each pair of numbers
    for i in range(n):
        for j in range(i + 1, n):
            num1 = str_numbers[i]
            num2 = str_numbers[j]
            
            # If numbers have different lengths, they can't be a valid pair
            if len(num1) != len(num2):
                continue
            
            # Count differences in digits
            diff_count = 0
            for k in range(len(num1)):
                if num1[k] != num2[k]:
                    diff_count += 1
                
                # Early termination if more than one difference found
                if diff_count > 1:
                    break
            
            # If exactly one digit differs, add to result
            if diff_count == 1:
                result.append((numbers[i], numbers[j]))
    
    return result

# Example usage
test_numbers = [12, 13, 45, 42, 121, 151, 999, 899, 1, 9, 7]
pairs = find_one_digit_different_pairs(test_numbers)

#print("Numbers:", test_numbers)
#print("Pairs with exactly one digit difference:")
#for pair in pairs:
#    print(f"{pair[0]} and {pair[1]}")

# count house segments after queries
def count_segments_after_queries(houses, queries):
    """
    计算每次房屋被摧毁后的连续区段数量。
    
    参数：
        houses: 房屋位置列表
        queries: 按顺序摧毁的房屋位置列表
        
    返回：
        每次查询后的区段数量列表
    """
    house_set = set(houses)
    result = []

    segments= count_segments(house_set)

    for house in queries:
        print("aa")
        if house in house_set:
            left_exists = house - 1 in house_set
            right_exists = house + 1 in house_set
            if left_exists and right_exists:
                segments += 1
            elif not left_exists and not right_exists:
                segments -= 1
            house_set.remove(house)
        result.append(segments)
    return result

def count_segments(h_set): # count the segments from a set.
    if not h_set:
        return 0
    houses = sorted(h_set)
    count = 1
    for i in range(1, len(houses)):
        if houses[i] > houses[i-1] + 1: # not continous
            count += 1
    return count
houses = [1, 2, 3,  7, 8, 10, 11]
queries = [2, 10, 8]
#print(count_segments_after_queries(houses, queries))    

#################################################################################
# leetcode 2043 Simple bank transaction
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.accounts_count = len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.valid_account(account1) and self.valid_account(account2):
            if self.withdraw(account1, money):
                self.deposit(account2, money)
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.valid_account(account):
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.valid_account(account) and self.balance[account-1] >= money:
            self.balance[account-1] -= money
            return True
        return False

    def valid_account(self, account) -> bool:
        if account  >= 1 and account <= self.accounts_count:
            return True
        return False
    
# leetcode 3161 Block placement queries
    









