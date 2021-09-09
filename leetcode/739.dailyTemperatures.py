class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        for i in range(1,len(temperatures)):
            if temperatures[i]>temperatures[i-1]:

