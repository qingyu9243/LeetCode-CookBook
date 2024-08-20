"""
Implement a database to store transactions that has following functions:
set(k, v)
get(k)
unset(k)
----------------------------------------------------------------------
begin()
rollback()
commit()

"""
from collections import defaultdict
class database:
    def __init__(self):
        self.data = defaultdict(str)
        self.tmp_data = defaultdict(str) # record the changes after begin
        self.to_delete = set() # record the keys that need to del in self.data
        self.begin_flag = False

    def begin(self):
        self.begin_flag = True

    def rollback(self):
        self.tmp_data = defaultdict(str)
        self.to_delete = set()

    def commit(self):
        self.begin_flag = False
        for d in self.to_delete:
            del self.data[d]
        for k, v in self.tmp_data.items():
            self.data[k] = v
        self.tmp_data = defaultdict(str)
        self.to_delete = set()

    def set(self, k, v):
        if self.begin_flag:
            self.tmp_data[k] = v
        else:
            self.data[k] = v
    
    def unset(self, k):
        if self.begin_flag:
            if k in self.tmp_data:
                del self.tmp_data[k]
            else:
                self.to_delete.add(k)
        else:
            del self.data[k]
    
    def get(self, k):
        if self.begin_flag:
            if k in self.tmp_data:
                return self.tmp_data[k]
        if k not in self.data:
            print("no such key exist.", k)
        return self.data[k]

db = database()
db.set("apple", "kkkk")
print(db.get("apple")) # -> kkkk
db.unset("apple")
print(db.get("apple")) # -> no such key exist, apple
print(db.get("banana")) # -> no such key exist, banana
db.set("pear", "pppp")
## -------- ##
db.begin()
db.set("pear", "pppp2")
db.set("pear", "pppp3")
db.set("apple", "kkkk2")
print(db.get("apple")) # -> "kkkk2"
print(db.get("pear")) # -> "pppp3"
db.rollback()
print(db.get("apple")) # -> None
print(db.get("pear")) # -> "pppp"
db.commit()
## -------- ##
print(db.get("apple")) # -> None
print(db.get("pear")) # -> "pppp"
print(db.data)