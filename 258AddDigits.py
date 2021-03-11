'''

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

class Solution:
    def addDigits(self, num: int) -> int:
        if(len(str(num))==1):
            return num
        elif(num%9==0):return 9
            
        return num%9
'''


class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        if(len(str(num))==1):
            return num
        while(len(str(num))!=1):
            sum=0
            while(num!=0):
                sum=sum+(num%10)
                num=num//10
            num=sum
        return sum
