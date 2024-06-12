"""
Interview Challenge: Implementing a SnapshotMap

Background: You're tasked with implementing a SnapshotMap data structure 
that extends a regular map with snapshot capabilities. This data structure 
should allow users to take snapshots of the map's state and retrieve values 
from these snapshots later.

A regular map has the following interface methods:
- get(k) -> v or KeyError
- put(k, v)
- delete(k)

We wish to augment this with two more methods:
- take_snapshot() -> snap_id
- get(k, snap_id) -> v or KeyError

Your Task:

Implement the SnapshotMap class with the following methods:
- put(k, v): Insert or update the value for a key.
- get(k, snap_id=None): Retrieve the value of a key at the current state or 
at a given snapshot.
- take_snapshot(): Take a historical snapshot of the current state and return a snapshot ID.
- delete(k): Delete a key from the map and reflect this in SUBSEQUENT snapshots. (Optional, if time permits)

Your implementation must adhere to these hard constraints:
- Values unchanged across snapshots should not be duplicated.
- All operations should be sub-linear in the size of the map.
- Assume the map will handle up to ~1 million keys, with ~10 snapshots, and 1% of 
the keys changing in each snapshot.

Testing Your Implementation
- To ensure your implementation meets the requirements, use the provided tests. 
This includes various scenarios to check the functionality and performance of 
your SnapshotMap.

Please review the test cases before starting the problem.
"""

import time
import random

"""
map = {key: {id:value, id:value}}
"""
from collections import defaultdict
class SnapshotMap:
    def __init__(self):
        # First, initialize your chosen data structure
        self.map = {} # {k: {s_id:value}, {s_id: valuex}}
        self.current_snap_id = 1

    def take_snapshot(self):
        # Second, create a snapshot of the current state
        self.current_snap_id += 1
        return self.current_snap_id

        # Third, we'll need to cover the basics
    def put(self, k, v):
    #     # Insert or update the value for a key
        if k not in self.map:
            self.map[k] = defaultdict(list)
            self.map[k].append()

    def get(self, k, snap_id=None):
    #     # Retrieve the value for a key - if snap_id is given, grab it from there
        

    # Now run the Phase 1 tests, and if you have time, begin the Phase 2 key deletion
    # def delete(self, k):
    #     # Delete a key from the map, reflect this deletion in subsequent snapshots
    #     pass

s = SnapshotMap()

"""
PHASE 1 - Basic snapshot functionality
Please note that we're commenting out the delete for now!
"""
# Test for basic put and get operations
s.put("a", 1)
s.put("b", 2)
assert s.get("a") == 1
assert s.get("b") == 2

# Test for snapshot functionality
snap_id1 = s.take_snapshot()
s.put("a", 5)
snap_id2 = s.take_snapshot()
snap_id3 = s.take_snapshot()
# Uncomment for Phase 2 - reflect deletion in subsequent snapshots
# remember, below at `assert s.get("b", snap_id1)` we will expect `2`
# after this deletion step
# s.delete("b")
s.put("a", 10)
snap_id4 = s.take_snapshot()
snap_id5 = s.take_snapshot()


# Test for values in different snapshots
assert s.get("a", snap_id1) == 1
assert s.get("a", snap_id2) == 5
assert s.get("a", snap_id3) == 5
assert s.get("a", snap_id4) == 10
assert s.get("a", snap_id5) == 10
assert s.get("a") == 10

assert s.get("b", snap_id1) == 2
assert s.get("b", snap_id2) == 2
assert s.get("b", snap_id3) == 2
print("PHASE 1 PASSED")

# """
# PHASE 2 - Key deletion
# Great! Time to delete keys, so go ahead and uncomment the s.delete("b") in Phase 1!
# """
# # Test for deleted key
# try:
#     s.get("b", snap_id4)
#     raise Exception("KeyError was expected but not raised")
# except KeyError:
#     pass

# try:
#     s.get("b", snap_id5)
#     raise Exception("KeyError was expected but not raised")
# except KeyError:
#     pass

# try:
#     s.get("b")
#     raise Exception("KeyError was expected but not raised")
# except KeyError:
#     pass

# print("PHASE 2 PASSED")

"""
PHASE 3 - Efficiency
Please uncomment one loop at a time, since your system need only deal 
with *up to* 1 million keys!
"""
# # 10,000 keys
# for i in range(10_000):
#     s.put(f"key{i}", i)

# start_time = time.time()
# for snapshot in range(10):
#     for i in random.sample(range(10_000), 100):
#         s.put(f"key{i}", random.randint(0, 10_000))

#     s.take_snapshot()
# end_time = time.time()

# duration = end_time - start_time
# print("\n\n10,000 keys.\nTotal time for 10 snapshots with 1% key changes each:", round(duration, 6), "seconds")

# # 100,000 keys
# for i in range(100_000):
#     s.put(f"key{i}", i)

# start_time = time.time()
# for snapshot in range(10):
#     for i in random.sample(range(100_000), 1000):
#         s.put(f"key{i}", random.randint(0, 100_000))

#     s.take_snapshot()
# end_time = time.time()

# duration = end_time - start_time
# print("\n\n100,000 keys.\nTotal time for 10 snapshots with 1% key changes each:", round(duration, 6), "seconds")

# # 1,000,000 keys
# for i in range(1_000_000):
#     s.put(f"key{i}", i)

# start_time = time.time()
# for snapshot in range(10):
#     for i in random.sample(range(1_000_000), 10_000):
#         s.put(f"key{i}", random.randint(0, 1_000_000))

#     s.take_snapshot()
# end_time = time.time()

# duration = end_time - start_time
# print("\n\n1,000,000 keys.\nTotal time for 10 snapshots with 1% key changes each:", round(duration, 6), "seconds\n\n")

# # Assert that the operation is efficient
# assert duration < 10, "Total operation took longer than expected"

# print("PHASE 3 PASSED")