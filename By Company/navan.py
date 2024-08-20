# 256. Paint House
def paintHouse1(costs):
    n = len(costs)
    dp = [] # dp[red, blue, green] represent the min costs until this house if choose red/blue/green color to paint
    for i in range(3):
        dp.append(costs[0][i])
    
    for i in range(1, n):
        red = costs[i][0] + min(dp[1], dp[2])
        blue = costs[i][1] + min(dp[0], dp[2])
        green = costs[i][2] + min(dp[0], dp[1])

        dp = [red, blue, green]

    return min(dp)
assert paintHouse1([[17,2,17],[16,16,5],[14,3,19]]) == 10

# 265. Paint House II
from typing import List
def minCostII(self, costs: List[List[int]]) -> int:
    n, k = len(costs), len(costs[0])
    dp = []
    for i in range(k):
        dp.append(costs[0][i])
    #print(dp)

    for house in range(1, n):
        tmp_list = []
        for color in range(k):
            smallest = float('inf')
            for pre_color in range(k):
                if color == pre_color: continue
                smallest = min(smallest, dp[pre_color])
            tmp_list.append(costs[house][color]+smallest)
        dp = tmp_list
    return min(dp)
# 1473. Paint House III

# LRU
"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""
from collections import OrderedDict
class LRU_OrderedDic:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key):
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key, value):
        self.dic[key] = value
        self.dic.move_to_end(key)
        if len(self.dic) > self.capacity:
            self.dic.popitem(last = False)

#########################
#####     DLL       #####
#########################
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

# 130. Sorrounded Regions.
"""
replace surrounded regions to X.
"""
from collections import deque
def solve(board):

    if not board:
        return
    m, n = len(board), len(board[0])
    stack = []
    # put "O" (i, j) in the stack
    for i in range(m): # left most column and right most column
        if board[i][0] == 'O':
            stack.append((i, 0))
        if board[i][n - 1] == 'O':
            stack.append((i, n - 1))
    for i in range(1, n - 1): # up most row and bottom most row
        if board[0][i] == 'O':
            stack.append((0, i))
        if board[m - 1][i] == 'O':
            stack.append((m - 1, i))
    #print(stack)
    # loop stack, change all the cells that connected to edge to another sign - #
    while stack:
        i, j = stack.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = "#"
            stack += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
    # change # to O, change O to X.
    board[:] = [['XO'[c == '#'] for c in row] for row in board]
solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])

# 1167. Minimum Cost to Connect Sticks [medium]
import heapq
def connectSticks(self, sticks: List[int]) -> int:
    cost = 0
    heapq.heapify(sticks)
    while len(sticks) > 1:
        acc = heapq.heappop(sticks) + heapq.heappop(sticks)
        cost += acc
        heapq.heappush(sticks, acc)
    return cost

# 316. Remove Duplicate Letters [medium]
"""
Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.
"""
def removeDuplicateLetters(self, s) -> int:
    stack = []
    seen = set()
    last = {c: i for i, c in enumerate(s)}
    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < last[stack[-1]]:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
    return ''.join(stack)

"""
ood 设计calendar，然后问了怎么实现给一堆users，怎么找他们共同的available time
"""


"""
Design an Event Manager
my solution:
Class EventManager {
// singleton
var events = [EventName: [UUID: Action]]()
func subscribe(eventName) -> token {}
func unsubscribe(eventName‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍, token) {}
func publish(eventName, Data) {}

"""
class EventManager:
    def __init__(self):
        self.events = [] #(event: action)

    def subscribe(self, eventName):
        pass

    def unsubscribe(self, eventName, token):
        pass

    def publish(self, eventName, data):
        pass

"""
Snake string to Camel case string.
"""
def snake_to_camel_case(snake_str):
    # Identify leading and trailing underscores
    leading_underscores = len(snake_str) - len(snake_str.lstrip('_'))
    trailing_underscores = len(snake_str) - len(snake_str.rstrip('_'))
    
    # Extract the main content between the underscores
    content = snake_str.strip('_')
    print("content", content)
    
    if not content:
        # If the content is empty, return the original string
        return snake_str
    
    # Split the content by underscores
    parts = content.split('_')
    print("parts", parts)

    # Convert to camel case
    camel_case_parts = [parts[0].lower()] + [part.capitalize() for part in parts[1:]]
    camel_case_content = ''.join(camel_case_parts)
    
    # Reassemble the string with the retained leading and trailing underscores
    return '_' * leading_underscores + camel_case_content + '_' * trailing_underscores

# Test cases
#print(snake_to_camel_case("__hello__world___"))  # __helloWorld___
#print(snake_to_camel_case("__hello__"))          # __hello__
#print(snake_to_camel_case("___"))                # ___
#print(snake_to_camel_case("hello"))              # hello
#print(snake_to_camel_case("__hello"))            # __hello
#print(snake_to_camel_case("hello__"))            # hello__

"""
Navan operates a sophisticated rewards banking system where accounts are structured in a hierarchical manner.
Each account can have multiple sub-accounts representing different teams or departments. Today our task is to Design and implement a simplified version of this account service that could
hypothetically be used in Navan's production environment.
Business requirements:
The account system is hierarchical; for example, the Infrastructure Engineering account might have sub-accounts for the Kafka team, S3 team, and DynamoDB team.
                        Infra Eng Account
                     /        |         \
Kafka Team acount   S3 Team account    DDB Team account
 /      |       \
Eng1  Eng2      Eng3
Functional Requirements:
Your system should support the following operations:
    fetchAccount(String uuid): Retrieve an account's details using its UUID.
    countTotalAccounts(String uuid, String status): Count all sub-accounts (recursively) under a given account that match a specific status.
    closeAccount(String uuid): Deactivate an account and optionally all its sub-accounts. Remember we can only close the account if the current account status is Active
    addBalance(String uuid, BigDecimal amount): Add a specified amount to the account's balance if the account is active.
    refreshTotalBalance(String uuid): Recalculate and update the total balance of the account and all its sub-accounts for active accounts only.
Tasks:
1.Design the Account data model suitable for a hierarchical structure.
2.Implement the backend logic for the account service described above.
3.Provide your own test cases for API, which will cover various scenarios including edge cases for the operations described.
"""
"""
from sqlalchemy import create_engine, Column, String, DECIMAL, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    uuid = Column(String, primary_key=True)
    parent_uuid = Column(String, ForeignKey('accounts.uuid'), nullable=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False, default='Active')
    balance = Column(DECIMAL(19, 2), default=0.00)
    total_balance = Column(DECIMAL(19, 2), default=0.00)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    parent = relationship('Account', remote_side=[uuid], backref='sub_accounts')

# Setup the database engine and session
engine = create_engine('sqlite:///accounts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from decimal import Decimal
from typing import Optional
from models import Account

class AccountService:
    def __init__(self, session: Session):
        self.session = session

    def fetch_account(self, uuid: str) -> Optional[Account]:
        return self.session.query(Account).filter_by(uuid=uuid).first()

    def count_total_accounts(self, uuid: str, status: str) -> int:
        sub_accounts = self.session.query(Account).filter_by(parent_uuid=uuid).all()
        count = 0
        for account in sub_accounts:
            if account.status == status:
                count += 1
            count += self.count_total_accounts(account.uuid, status)
        return count

    def close_account(self, uuid: str) -> None:
        account = self.fetch_account(uuid)
        if account and account.status == 'Active':
            account.status = 'Inactive'
            self.session.commit()
            for sub_account in account.sub_accounts:
                self.close_account(sub_account.uuid)

    def add_balance(self, uuid: str, amount: Decimal) -> None:
        account = self.fetch_account(uuid)
        if account and account.status == 'Active':
            account.balance += amount
            self.session.commit()

    def refresh_total_balance(self, uuid: str) -> None:
        account = self.fetch_account(uuid)
        if account and account.status == 'Active':
            total_balance = account.balance
            for sub_account in account.sub_accounts:
                self.refresh_total_balance(sub_account.uuid)
                total_balance += sub_account.total_balance
            account.total_balance = total_balance
            self.session.commit()


import unittest
from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from account_service import AccountService
from models import Base, Account

class TestAccountService(unittest.TestCase):
    def setUp(self):
        # Setup in-memory SQLite database for testing
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.service = AccountService(self.session)
        self.insert_test_data()

    def insert_test_data(self):
        accounts = [
            Account(uuid='1', name='Infra Eng Account', status='Active', balance=Decimal('0.00')),
            Account(uuid='2', parent_uuid='1', name='Kafka Team Account', status='Active', balance=Decimal('50.00')),
            Account(uuid='3', parent_uuid='1', name='S3 Team Account', status='Active', balance=Decimal('100.00')),
            Account(uuid='4', parent_uuid='1', name='DynamoDB Team Account', status='Active', balance=Decimal('150.00')),
            Account(uuid='5', parent_uuid='2', name='Eng1 Account', status='Active', balance=Decimal('20.00')),
            Account(uuid='6', parent_uuid='2', name='Eng2 Account', status='Active', balance=Decimal('30.00')),
            Account(uuid='7', parent_uuid='2', name='Eng3 Account', status='Active', balance=Decimal('40.00'))
        ]
        self.session.bulk_save_objects(accounts)
        self.session.commit()

    def test_fetch_account(self):
        account = self.service.fetch_account('1')
        self.assertIsNotNone(account)
        self.assertEqual(account.name, 'Infra Eng Account')

    def test_count_total_accounts(self):
        count = self.service.count_total_accounts('1', 'Active')
        self.assertEqual(count, 6)

    def test_close_account(self):
        self.service.close_account('1')
        account = self.service.fetch_account('1')
        self.assertEqual(account.status, 'Inactive')
        count = self.service.count_total_accounts('1', 'Active')
        self.assertEqual(count, 0)

    def test_add_balance(self):
        self.service.add_balance('2', Decimal('100.00'))
        account = self.service.fetch_account('2')
        self.assertEqual(account.balance, Decimal('150.00'))

    def test_refresh_total_balance(self):
        self.service.refresh_total_balance('1')
        account = self.service.fetch_account('1')
        self.assertEqual(account.total_balance, Decimal('390.00')) # 0 + 50 + 100 + 150 + 20 + 30 + 40

if __name__ == '__main__':
    unittest.main()
"""


"""
* Navan is a business travel agency. One of the most core functions of our product is to sell flight bookings to our customers. This interview question dives into this core workflow.
* Today we are going to implement the booking flow for a single passenger, one way booking. You are given the following interfaces/classes, however some are intentionally left blank.
*
* Implement FlightBookingService. As a part of this, we need to collect a payment, contact the remote airline and send the booking, and also record the booking in our system.
* Be careful and consider the failure / faults which can occur in the system and how to handle them.
*/
class FlightBookingService {
    private FlightProvider flightProvider = new FlightProvider(){
    @Override
    public void bookFlight(Flight flight, User user) {
        // TODO Auto-generated method stub
    }
    public boolean isValidSeat(Flight flight) {
        // TODO Auto-generated method stub
        return true;
    }
    public boolean isValidPaymentInfo(CreditCard creditCard, User user) {
        // TODO Auto-generated method stub
        return true;
    }
    };
    private PaymentService paymentService = new PaymentService() {
    }

    };
    private DatabaseService databaseService = new DatabaseService() {
    };
    public Booking bookFlight(Flight flight, CreditCard creditCard, User user) {
    }
    private boolean makeCharge(BigDecimal price, CreditCard creditCard, User user){
    }
}
enum Cabin {
    ECONOMY, PREMIUM_ECONOMY, BUSINESS, FIRST;
}
@Value
class Flight {
    private String flightNumber;
    public Instant departure;
    private String departureAirport;
    private String arrivalAirport;
    private String airlineCode;
    private Cabin cabin;
    private BigDecimal price;
}
@Value
class User {
    UUID uuid;
    String email;
}
@Value
class Booking {
    Flight flight;
    User user;
    UUID uuid;
}
@Value
class CreditCard {
    UUID uuid;
    String cardNumber;
    String ccv;
    Strng cardHolderFirstName;
    String cardHolderLastName;
    LocalDate expirationMonthYear;
}
interface DatabaseService {
    private HashMap<String, Flight> bookedFlights;
}
interface FlightProvider {
    public void bookFlight(Flight flight);
}
interface PaymentService {
}
"""
