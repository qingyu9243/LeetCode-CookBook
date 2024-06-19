from collections import defaultdict, Counter
# 631. Design Excel Sum Formula
class Excel:

    def __init__(self, height: int, width: str):
        self.height = height 
        self.width = self.convertCol(width) + 1
        self.matrix =[[0]*self.width for i in range(self.height)]
        self.matrix_sum = defaultdict(Counter) # (row, col) : {'row_x, col_x': count, 'row_y, col_y': count}

    def set(self, row: int, column: str, val: int) -> None:
        n_row = row-1
        n_col = self.convertCol(column)
        self.matrix[n_row][n_col] = val
        if (n_row, n_col) in self.matrix_sum:
            del self.matrix_sum[(n_row, n_col)]

    def get(self, row: int, column: str) -> int:
        n_row = row-1
        n_col = self.convertCol(column)
        val = 0
        if (n_row, n_col) in self.matrix_sum:
            for cell, cnt in self.matrix_sum[(n_row, n_col)].items():
                val += self.get(cell[0]+1, chr(cell[1]+65)) * cnt
            self.matrix[n_row][n_col] = val
        #print(n_row, n_col, self.matrix[n_row][n_col])
        return self.matrix[n_row][n_col]

    def sum(self, row: int, column: str, numbers) -> int:
        sum_ = 0
        key_row = row - 1
        key_col = self.convertCol(column)

        if (key_row, key_col) in self.matrix_sum:
            del self.matrix_sum[(key_row, key_col)]
        for num in numbers:
            n_list = num.split(":")
            if len(n_list) == 1:
                n_row = int(n_list[0][1:])-1
                n_col = self.convertCol(n_list[0][0])
                sum_ += self.get(n_row+1, chr(n_col+65))
                self.matrix_sum[(key_row,key_col)][(n_row, n_col)] += 1
            else:
                n_row_s = int(n_list[0][1:])-1
                n_col_s = self.convertCol(n_list[0][0])
                n_row_e = int(n_list[1][1:])-1
                n_col_e = self.convertCol(n_list[1][0])
                for n_row in range(n_row_s, n_row_e+1):
                    for n_col in range(n_col_s, n_col_e+1):
                        sum_ += self.get(n_row+1, chr(n_col+65))
                        self.matrix_sum[(key_row,key_col)][(n_row, n_col)] += 1 
        #print(self.matrix)
        #print(self.matrix_sum)
        self.matrix[key_row][key_col] = sum_
        return sum_

    def convertCol(self, column):
        return ord(column)-ord("A")

"""

// Design and implement an in-memory key value data store. 
This data store should be able to support some basic operations such as Get, Set and Delete for string keys and values.

// I would like to see test cases as well as implementation code. You can assume that the input operations are always valid, 
but the key to operate on may be non-existent.

// We won' t worry about concurrent access to the database. You can handle errors however you think is best. 
Let' s start with the data structure of this key value store.

// Implement methods for Get, Set and Delete.

// Add support for transactions - Begin, Commit and Rollback.
// A transaction is created with the Begin command and creates a context for the other operations to happen.
// Until the active transaction is committed using the Commit command, those operations do not persist.
// The Rollback command throws away any changes made by those operations in the context of the active transaction.
// Commit() and ``Rollback()`` will only happen when inside a transaction, and they both end the transaction.
// Note: We won't worry about concurrency for this part of the question.
"""
class KeyValueStore:
    def __init__(self) -> None:
        pass
    def get(self, key):
        pass
    def set(self, key, value):
        pass
    def delete(self, key):
        pass