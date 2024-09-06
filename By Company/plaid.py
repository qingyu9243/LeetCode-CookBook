"""
bank transfer 
follw up是给出一个提案 减少transaction总量，大概是利口 中等的难度。

pass: https://www.1point3acres.com/bbs/thread-802961-1-1.html
这轮结果不错然后约了coding interview，一共是2个session，每个session是1个小时的coding，连着的。IDE是自己本地的环境，通过google hangout screenshare（面试之前把电脑桌面和打开了的窗口收拾一下）。coding的内容本质还是leetcode，但是加了这个公司的context，大概就是正常难度，主要是考data structure，是挺实用的那种题（比如我觉得把一个binary tree颠倒过来这种题就很不实用，正常工作遇不到这种问题）写完代码以后要写一些test case，想一些edge case，然后讲一下要怎么测
这轮过了以后约onsite，onsite一共4轮，4个小时
1. 90分钟coding，其实和之前那两个coding interview难度和风格差不多，也是关于data structure，followup多一点。题量并没比之前的多太多，我70多分钟的时候做完了，问了问面试官一些问题以后就提前结束了这轮
2. 60分钟system design，也是这个公司业务的context，算是比较普通的题（比如我认为比较不普通的题是类似top K system这种我不去查就真的想不出该怎么设计的题，也加上我对data pipeline没有任何经验）反正就是中规中矩的题。自己建一个google drawing然后把链接share给面试官
3. 60分钟BQ，这个所有公司都差不多吧
4. 30分钟PM interview，这个其实还是BQ，但是是PM问的。Plaid的PM比例‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍很高，我以为这是个关于workstyle的面试，结果还是需要讲出具体的故事来，我现在的工作确实和PM打交道不多，一开始没明白这轮是干什么的，感觉答得一般
其实就是系统设计经典几大块：API，LB，services，database。API和DB schema要设计的详细一点，requests来的量大了怎么handle。然后DB选哪种，read-heavy还是write-heavy，sql vs nosql，consistency vs availability应该更偏向哪种情况，怎么partition。requests和数据多了以后系统怎么scale，bottleneck在哪里。感觉能展开讨论的地方还挺多的，但是最后没时间了

https://www.1point3acres.com/bbs/thread-766715-1-1.html
1. Coding:
[
# merchant, amount, date
("Netflix", 9.99, 10),
("Netflix", 9.99, 20),
("Netflix", 9.99, 30),
("Amzn", 27.12, 32),
("Sprint", 50.11, 45),
("Sprint", 50.11, 55),
("Sprint", 50.11, 65),
("Sprint", 60.13, 77),
]

给一个 transactions list，找到重复的 merchant，重复的意思 merchant 是出现三次，amount 相同并且之间相差相同的时间。 比如上面这个例子 output 是 ["Netflix"].
follow-up 是把重复的定义改成 amount 的最大值和最小值相差不超过20%，其他条件不变。
2. Technical Deep Dive：做一个 slide 讲自己做的一个项目.
3. Chat with an engineer


https://www.1point3acres.com/bbs/thread-726843-1-1.html
算法轮不是力扣原题，大概意思是说银行转帐都会通过一个中央行A转账，给一个list的转账信息 最后需要output一个简化版本的list
sample
input: ["AB1", "BA2", "BC3"] // A转$1到B，B转$2到A, B转$3到C
output: ["BA4", "AC3"] // 合起来算B转$4到A，A转$3到C
followup是 不指定中央行是A怎么找到一个最合适的中央行，然后output
（题目有点绕 看‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍sample比较好理解）


https://www.1point3acres.com/bbs/thread-582793-1-1.html
输入是一列transaction，例如
[
  ("支付宝", 19.99, 10),
  ("支付宝", 19.99, 20),
  ("支付宝", 19.99, 30),
  ("中国移动", 27.12, 32),
  ("优酷会员", 33.11, 45),
  ("优酷会员", 33.11, 55),
  ("优酷会员", 33.11, 65),
  ("优酷会员", 36.13, 76),
]
复制代码
每一个transaction是(merchant, cost, date)
第一问：
找出recurring transaction。recurring transaction定义是，同样的merchant，cost，所有transaction以相同间隔的date出现，至少3次
例子中的支付宝是，但是优酷会员不是，因为优酷会员最后一个transaction cost和date interval都改变了。
一个直接的思路是用dict，key是(merchant, cost)， value是list of date，最后验证
第二问：
放宽recurring transaction的条件，只要merchant相同，但cost或者date最大最小之间相差不超过20%。这样的话，例子中的优酷会员就是recurring transaction
我的解法是‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍，对每个merchant，用几个dict分别保存min_cost, max_cost, min_interval, max_interval, count, 对每个transaction验证是否符合cost和date的条件，最后挑出至少出现三次的


给一个list of tuples 比如 (company="company1", amount=100, date=20)， 要求返回所有的recurring company

Onsite https://www.1point3acres.com/bbs/thread-907775-1-1.html
1. 应用题，具体记不太清了，大体是设计一个job scheduler, 定时汇报需要更新的银行账户。需求非常奇怪，然而具体到编程, 难度就是LeetCode Easy. 一小时的面试时间，撸主花了整整30分钟来理解题目，然后十几分钟刷刷刷两问做出来了。
2. Credit/Loan Application System 变型。可以参考这个设计并思考怎么拓展（然而LeetCode这老哥RESTful API是有问题的

https://www.1point3acres.com/bbs/thread-442099-1-1.html
先去mini onsite做了两道题，Stack with min/max value. 写到一半发现写错了, 以为要挂；第二轮 log counter， 利口三六二，然后闲扯一番。
onsite 第一轮 behaviour，第二轮system deisgn，午饭，吃完饭又做了一题，file processing，然后写一个kmeans的算法，允许上网查资料。

两轮电面。一轮是简单题，lc min stack变种；一轮是涉及到multithread的，LC上的design hit counter
onsite一轮是写代码，1.5小时。在自己机器上写，投影到会议室的屏幕上。涉及到一个具体问题，写完编译运行，在测试数据上跑一下。
system design。题目很常见，当时回答的时候没有条理，明显感觉到面试官不知道该怎么问。面试官试图给我提示但我当时也不知道该如何回应了。这轮表现不好。
head of engineer。各种bq问题，你最喜欢的project，为什么喜欢；你project失败了的情况，你该如何做才能避免失败；有没有你不喜欢但必须做的工作，你如何处理。
hiring manager，类似的BQ问题。 the time you dropped the ball, what do yo‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍u do? the time others dropped the ball, what do you do?

"""
# 155. Min Stack
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
5, 4, -1, 5, 3, -1
5, 4, -1,  # make sure the min_stack[-1] is the min value, so use O(1) to retrieve 

"""
class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif len(self.min_stack) > 0 and self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            n = self.stack.pop()
            if n == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# Design Hit Counter
"""
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
"""
class HitCounter:
    def __init__(self) -> None:
        pass
    def hit(self, timestamp):
        pass
    def getHits(self, timestamp):
        pass


#############################
# transfer between accounts #
#############################
from collections import defaultdict
def bankTransfer(list, center_bank):
    balances = defaultdict(int)

    for transaction in list:
        sender = transaction[0]
        receiver = transaction[1]
        amount = int(transaction[2:])
        if sender != center_bank:
            balances[sender] -= amount
        if receiver != center_bank:
            balances[receiver] += amount
    #print(balances)
            
    simplified_transactions = []
    for bank, amount in balances.items():
        if amount > 0:
            simplified_transactions.append(center_bank+bank+str(amount))
        else:
            simplified_transactions.append(bank+center_bank+str(-amount))

    return simplified_transactions

def bankTransferWithoutCenterBank(list):
    net_balances = defaultdict(int)
    for trans in list:
        sender, receiver, amount = trans[0], trans[1], trans[2:]
        net_balances[sender] -= amount
        net_balances[receiver] += amount
    
    # find center bank
    center_bank = ""
    max_net_amount = 0
    for bank, net_amount in net_balances.items():
        if abs(net_amount) > max_net_amount:
            max_net_amount = abs(net_amount)
            center_bank = bank

    return bankTransfer(list, center_bank)

print(bankTransfer(["AB1", "BA2", "BC3"], "A"))
#assert bankTransfer(["AB1", "BA2", "BC3"]) == ["BA4", "AC3"]


#############################
#####    apply coupon   #####
#############################



coupons = [{"catogories": ["electronic", "food"], "percentage": 20, "off": 0, "min_quant": 0,
            }]



