import random
import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    curr = ListNode(0)
    dummyHead = curr

    while(1):

        if l1 == None and l2 == None and carry == 0 :
            break

        x = l1.val if l1 != None else 0
        y = l2.val if l2 != None else 0
        sum = x + y + carry

        carry = int((sum-sum%10)/10)
        curr.next = ListNode(int(sum%10))
        curr = curr.next

        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
    return dummyHead.next
def addTwoNumbers_Recursion(l1, l2, flag=False):
    if (l1 is None) and (l2 is None) and not flag:
        return None
    node = ListNode(None)
    carry = False

    if l1 is None:
        l1 = ListNode(0)
    if l2 is None:
        l2 = ListNode(0)
    sum = l1.val + l2.val + int(flag)
    node.val = int(sum%10)
    carry = False if sum<10 else True
    node.next = addTwoNumbers_Recursion(l1.next, l2.next, carry)
    return node

if __name__ == '__main__':
    x = ListNode(random.randint(0, 9))
    y = ListNode(random.randint(0, 9))
    a,b = x.val,y.val
    dummyHead1 = ListNode(0)
    dummyHead1.next = x
    dummyHead2 = ListNode(0)
    dummyHead2.next = y
    carry = 1

    for i in range(3):
        x.next = ListNode(random.randint(0, 9))
        x = x.next
        y.next = ListNode(random.randint(0, 9))
        y = y.next
        a += x.val * pow(10,i+1)
        b += y.val * pow(10,i+1)
    print("两个相加数为：",a,"和",b)
    print("1.常规方法\n2.递归方法")
    line = input()
    if line[0] == "1":
        res = addTwoNumbers(dummyHead1.next, dummyHead2.next)
    elif line[0] == "2":
        res = addTwoNumbers_Recursion(dummyHead1.next, dummyHead2.next, False)
    else:
        print("输入错误")
        exit()
    #常规方法
    #res = addTwoNumbers(dummyHead1.next, dummyHead2.next)
    #递归方法
    # res = addTwoNumbers_Recursion(dummyHead1.next,dummyHead2.next,False)

    c = 0
    count = 0
    while (1):
        #print(res.val)
        c += res.val * pow(10,count)
        if res.next == None:
            break
        res = res.next
        count += 1
    print("函数运算结果为：",c,"数字相加应为：",a+b)
    print("算法结果为：",a+b == c)

