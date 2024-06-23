from collections import defaultdict, Counter
from typing import List
# 631. Design Excel Sum Formula [hard]
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
https://leetcode.com/discuss/interview-question/3928848/rippling-phone-screen-sr-software-engineer-us-rejected
https://leetcode.com/discuss/interview-question/279913/key-value-store-with-transaction



// Design and implement an in-memory key value data store. 
This data store should be able to support some basic operations such as Get, Set and Delete for string keys and values.

// I would like to see test cases as well as implementation code. You can assume that the input operations are always valid, 
but the key to operate on may be non-existent.

// We won' t worry about concurrent access to the database. You can handle errors however you think is best. 
Let' s start with the data structure of this key value store.

Pharse 1 
// Implement methods for Get, Set and Delete.

Pharse 2
// Add support for transactions - Begin, Commit and Rollback.
// A transaction is created with the Begin command and creates a context for the other operations to happen.
// Until the active transaction is committed using the Commit command, those operations do not persist.
// The Rollback command throws away any changes made by those operations in the context of the active transaction.
// Commit() and ``Rollback()`` will only happen when inside a transaction, and they both end the transaction.
// Note: We won't worry about concurrency for this part of the question.

Pharse 3
/// Support nested transactions. Begin() multiple times and close out the transactions by either rollback or commit.
"""
class KeyValueStore:
    def __init__(self) -> None:
        self.store = {}
        self.transactions = []

    def get(self, key):
        for transaction in self.transactions[::-1]:
            if key in transaction:
                return transaction[key]
        else:
            return self.store[key]

    def set(self, key, value):
        if self.transactions:
            self.transactions[-1][key] = value
        else:
            self.store[key] = value

    def delete(self, key):
        if self.transactions:
            self.transactions[-1][key] = None
        else:
            del self.store[key]

    def begin(self,):
        self.transactions.append({})

    def commit(self,):
        if self.transactions:
            cur = self.transactions.pop()
            for k, v in cur.items():
                if v is None:
                    #print(k, v)
                    del self.store[k]
                else:
                    self.store[k] = v

    def rollback(self,):
        if self.transactions:
            self.transactions.pop()

# phase 1, basic functions
s = KeyValueStore()
s.set('1', 'a')
s.set('2', 'b')
s.delete('2')
s.get('1')
s.set('2', 'c')
s.set('3', 'm')
#s.get('2')
s.set('1', 3)
print(s.store)

# phase 2, support commit and rollback
s.begin()
s.set('1', 5)
s.delete('3')
s.rollback()
print(s.store)
s.begin()
s.set('2', 8)
print('1 is', s.get('1'))
s.delete('3')
s.commit()
print(s.store)


# phase 3, support nested transactions
s.begin()
s.set('1', 6)
"""
https://www.1point3acres.com/bbs/thread-1071111-1-1.html
    https://www.1point3acres.com/bbs/thread-1045548-1-1.html
"""


## Design Google News
