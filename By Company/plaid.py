"""
bank transfer 
follw up是给出一个提案 减少transaction总量，大概是利口 中等的难度。



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
"""
class MinStack:
    def __init__(self) -> None:
        pass

    def push(self, int):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def getMin(self):
        pass

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
