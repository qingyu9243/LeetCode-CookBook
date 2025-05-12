## OA ##
from collections import defaultdict
# bank system
class BankSystem:
    def __init__(self) -> None:
        self.accounts = {} # {accountId: balance}
        self.transactions = {} # {accountId: total amounts}
        self.pending_transfers = {}
        self.transfer_counter = 1

    def createAccount(self, timestamp, accountId):
        if accountId in self.accounts:
            return "false"
        self.accounts[accountId] = 0
        self.transactions[accountId] = 0
        return "true"
    
    def deposit(self, timestamp, accountId, amount):
        if accountId not in self.accounts:
            return ""
        self.accounts[accountId] += amount
        self.transactions[accountId] += amount
        return str(self.accounts[accountId])    

    def pay(self, timestamp, accountId, amount):
        if accountId not in self.accounts:
            return ""
        if self.accounts[accountId] < amount:
            return ""
        self.accounts[accountId] -= amount
        self.transactions[accountId] += amount
        return str(self.accounts[accountId])

    def top_activity(self, timestamp, n):
        n_int = int(n)
        sorted_accounts = sorted(self.transactions.items(), key=lambda x:(-x[-1], x[0]))
        result_accounts = sorted_accounts[:n_int] if len(sorted_accounts) >= n else sorted_accounts
        result = ", ".join([f"{acct}({trans})"] for acct, trans in result_accounts)
        return result
    
    def transfer(self, timestamp, sourceAccountId, targetAccountId, amount):
        ts_int = int(timestamp)
        amt_int = int(amount)

        if sourceAccountId == targetAccountId:
            return ""
        if sourceAccountId not in self.accounts or targetAccountId not in self.accounts:
            return ""
        if self.accounts[sourceAccountId] < amount:
            return ""
        # withhold money
        self.accounts[sourceAccountId] -= amount
        # create transfer id
        transfer_id = f"transfer{self.transfer_counter}"
        self.transfer_counter += 1
        # expire time
        expiration_time = ts_int + 24*60*60*60*1000
        self.pending_transfers[transfer_id]= {
            "sourceAccountId": sourceAccountId,
            "targetAccountId": targetAccountId,
            "amount": amt_int,
            "timestamp": ts_int,
            "expiration_time": expiration_time,
            "status": "pending"
        }
        return transfer_id

    def accept_transfer(self, timestamp, accountId, transferId):
        pass


import heapq
# cloud storage system
class CloudStorage:
    def __init__(self) -> None:
        # main storage for file, {name: size}
        self.files = {}
        # user storage, {user_id: {capacity: int, remaining: int, files: {}}
        self.users = {"admin": {"capacity": float('inf'), "remaining": float('inf'), "files":{}}}

    # level 1: file manipulation
    def add_file(self, name, size): # -> bool
        if name in self.files:
            return False
        self.files[name] = size
        return True

    def get_file_size(self, name): # -> int/None
        if name in self.files:
            return self.files[name]
        return None

    def delete_file(self, name): # -> int(size)/None
        if name in self.files:
            size = self.files[name]
            del self.files[name]
            return size
        return None

    # level 2: retrieve file statistics with prefix
    def get_n_largest_heap(self, prefix, n):
        n_largest = []
        l = len(prefix)
        for name, size in self.files.items():
            if prefix == name[:l]:
                if len(n_largest) < n:
                    heapq.heappush(n_largest, (-size, name))
                else:
                    head = n_largest[0]
                    if head[0] < size:
                        heapq.heappop(n_largest)
                        heapq.heappush(n_largest, (-size, name))
        result = []
        for size, name in n_largest:
            result.append(name)
        return result
    
    def get_n_largest(self, prefix, n):
        matching_files = []
        for name, size in self.files.items():
            if name.startswith(prefix):
                matching_files.append((-size, name))
        # sort and return :n
        matching_files.sort(key=lambda x:(x[0], x[1]))
        return [name for _, name in matching_files[:n]]
    
    # level 3: queries from diff users. (all users share common file system, but each user has capacity limit)
    def add_user(self, user_id, capacity): # bool
        if user_id in self.users:
            return False
        self.users[user_id] = {"capacity": capacity, "remaining": capacity, "files":{}}
        return True
    
    def add_file_by(self, user_id, name, size): # int(remaining capacity)/None
        # check user if exist
        if user_id not in self.users:
            return None
        # check capacity
        remaining = self.users[user_id]["remaining"]
        if size > remaining:
            return None
        # add file
        self.users[user_id]["files"][name] = size
        self.users[user_id]["remaining"] -= size
        return self.users[user_id]["remaining"]

    # level 4: allow user to backup their files
    def backup_user():
        pass

cloudStorage = CloudStorage()
cloudStorage.add_file("file1", 5)
cloudStorage.add_file("file2", 20)
cloudStorage.add_file("file3.mov", 9)
print(cloudStorage.get_n_largest("file", 2))

# key value store



# course registration system




# text editor





# 281. Zigzag iterator

# 588. design in-memory file system

# 2043. simple bank system

# 68. test justification

# 1166. design file system

# 2325. decode the message

# 1801. number of orders in the backlog

# 2369. check if there is a valid partition for the arrary

# 981. time based key-value store

# 3043. find the length of the longest common prefix

# 399. evaluate division