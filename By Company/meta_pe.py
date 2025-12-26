### Arrays & String
# 1. array split equal sum

# 2. goat latin
def toGoatLatin(S: str) -> str:
    res = []
    for i, word in enumerate(S.split()):
        if word[0].lower() in 'aeiou':
            res.append(word + 'ma' + 'a'*(i + 1))
        else:
            res.append(word[1:] + word[0] + 'ma' + 'a'*(i + 1))
    return ' '.join(res)

# 3. validate palindrome
def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

# 438. find all anagrams
def findAnagrams(s, p):
    return

# 161. One edit distance
def isOneEditDistance(s, t):
    return

### Tree Problems
class TreeNode:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None

# 98. Validate Binary Search Tree


# filter BST

# 426. convert BST to sorted DDL

# binary tree paths
def binaryTreePath(root):
    return

### Permutation & Combinations
def primeProducts(primes):
    return

from collections import Counter
# 824. 
def numFriendRequests(ages) -> int:
    def will_send_request(age_x: int, age_y: int) -> bool:
        """Check if person with age_x will send request to person with age_y"""
        # Condition 1: age[y] must be > 0.5 * age[x] + 7
        if age_y <= 0.5 * age_x + 7:
            return False
        # Condition 2: age[y] must be <= age[x]
        if age_y > age_x:
            return False  
        # Condition 3: NOT (age[y] > 100 AND age[x] < 100)
        if age_y > 100 and age_x < 100:
            return False    
        return True

    age_count = Counter(ages)
    count = 0
    for age_x, count_x in age_count.items():
        for age_y, count_y in age_count.items():
            if will_send_request(age_x, age_y):
                if age_x == age_y:
                    # Same age group: each person sends to others in same group
                    # count_x people, each sends to (count_x - 1) others
                    count += count_x * (count_x - 1)
                else:
                    # Different age groups: all people of age_x send to all of age_y
                    count += count_x * count_y
    return count


### Bash Programming
import sys
from collections import deque
# monitor vmstat for vilations that exceed threshold
def process_vmstat(metric, limit, count, window):
    limit = int(limit)
    count = int(count)
    violations = deque()
    headers = []
    first_line_skipped = False
    for line in sys.stdin:
        if line.startswith('procs'):
            headers = next(sys.stdin).split()
            metric_idx = headers.index(metric)
            continue
        if headers and not first_line_skipped:
            first_line_skipped = True
            continue
        #if he
    return

## 5. Data center failure simulation
from datetime import datetime
import heapq
class DataCenterSimulator:
    def __init__(self) -> None:
        self.servers = {} # server_id -> status
        self.failure_events = [] # min heap of (time, server_id)
        self.recovery_events = [] # min heap of (time, server_id)

    def add_server(self, server_id, initial_status = 'active'):
        self.servers[server_id] = initial_status

    def add_failure(self, server_id, failure_time):
        heapq.heappush(self.failure_events, (failure_time, server_id))

    def add_recovery(self, server_id, recovery_time):
        heapq.heappush(self.recovery_events, (recovery_time, server_id))
    
    def simulate_units(self, end_time):
        """ Run simulation until specified time """
        events = []
        for time, server in self.failure_events:
            if time <= end_time:
                events.append((time, server, "failure"))
        for time, server in self.recovery_events:
            if time <= end_time:
                events.append((time, server, "recovery"))
        # sort events by time
        events.sort()
        # process event
        timeline = []
        for time, server, type in events:
            if type == "failure":
                self.servers[server] = "failed"
            else:
                self.servers[server] = "active"
            timeline.append({
                'time': time,
                'server': server,
                'event': type,
                'total_failed': sum(1 for s in self.servers.values() if s == 'failed')
            })
        return timeline

    def get_availability(self, start_time, end_time):
        """ calculate availability percentage"""
        total_server_time = len(self.servers) * (end_time - start_time)
        failed_time = 0
        # calculate downtime for each server

        return (total_server_time - failed_time)/total_server_time * 100

# file I/O
# dinosur 

from collections import defaultdict, deque
# log processing system
class LogProcessing:
    def __init__(self, window_size = 3600) -> None: # 1hr window
        self.window_size = window_size
        self.error_counts = defaultdict(deque())
        self.alert_threshold = 100

    def process_log_line(self, timestamp, log_line):
        if self._is_error(log_line):
            error_type = self._extract_error_type(log_line)
            self._update_counts(error_type, timestamp)
            self._check_alerts(error_type, timestamp)
    
    def _update_counts(self, error_type, timestamp):
        self.error_counts[error_type].append(timestamp)
        current_time = timestamp
        cutoff_time = current_time - self.window_size
        # remove timestamps older than the window
        while self.error_counts[error_type] and self.error_counts[error_type][0] < cutoff_time:
            self.error_counts[error_type].popleft()
    
    def _is_error(self, log_line):
        return
    
    def _extract_error_type(self, log_line):
        return
    
    def _check_alerts(self, error_type, timestamp):
        alert_list = self.error_counts[error_type]
        # ...
        return
    




"""sed -i -e "s/test@fb\.com/removed@fb\.com/g" *.html"""