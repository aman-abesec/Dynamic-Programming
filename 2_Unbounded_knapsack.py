#===========================================
# Unbounded Knapsack
#==========================================
#Multiple Occurences of a atom allowed

######PROBLEMS########
#Rod Cutting Problem
#Coin Change1(max no. of ways)
#Coin Change2(min no. of ways)
#Maximum Ribbon Cut

#================================================================
#       Rod Cutting Problem
#https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
#================================================================
#Recursiv Method
def rodCut(Larr,Parr,L,N):
    if L==0 or N==0:return 0
    if L>=Larr[N-1]:
        return max(Parr[N-1]+rodCut(Larr,Parr,L-Larr[N-1],N),
                rodCut(Larr,Parr,L-1,N))
    else:
        return rodCut(Larr,Parr,L,N-1)
Length=[1,2,3,4,5,6,7,8]
Price=[1,5,8,9,10,17,18,20]
#Length of Rod
L=8
N=8
# print(rodCut(Length,Price,L,N))

#Memorization
def solve(Larr,Parr,L,N,dp):
    if L==0 or N==0:return 0
    if dp[N][L]!=-1:return dp[N][L]
    if L>=Larr[N-1]:
        dp[N][L]=max(Parr[N-1]+solve(Larr,Parr,L-Larr[N-1],N,dp),
        solve(Larr,Parr,L,N-1,dp))
        return dp[N][L]
    else:
        dp[N][L]=self.solve(Larr,Parr,L,N-1,dp)
        return dp[N][L]

def cutRod(price, n):
    N=len(price)
    Larr=[i for i in range(1,N+1)]
    dp=[[-1]*(n+1) for _  in range(N+1)]
    return solve(Larr,price,n,N,dp)

#===================================================================
#  Coin Change1(Max No of ways)
#https://practice.geeksforgeeks.org/problems/coin-change2448/1
#==================================================================
#Recursive
def coinMaxWayRec(Carr,S,N):
    if S!=0 and N==0:return 0
    if S==0:return 1
    if S>=Carr[N-1]:
        return coinMaxWayRec(Carr,S-Carr[N-1],N)+coinMaxWayRec(Carr,S,N-1)
    else:
        return coinMaxWayRec(Carr,S,N-1)

#Memoization
dp=[[-1]*(10**3+2) for _ in range(10**3+2)]
class Solution:
    def coinMaxWay(self,Carr,S,N):
        global dp
        if S!=0 and N==0:return 0
        if S==0:return 1
        if dp[N][S]!=-1:return dp[N][S]
        if S>=Carr[N-1]:
            dp[N][S]=self.coinMaxWay(Carr,S-Carr[N-1],N)+self.coinMaxWay(Carr,S,N-1)
            return dp[N][S]
        else:
            dp[N][S]=self.coinMaxWay(Carr,S,N-1)
            return dp[N][S]

    def count(self, S, m, n):
        global dp
        dp=[[-1]*(10**3+2) for _ in range(10**3+2)]
        return self.coinMaxWay(S,n,m)

Carr=[1,2,3]
S=5
N=3
# print(coinMaxWay(Carr,S,N))

#========================================================================
#  Coin Change1(Min No of coins)
#https://practice.geeksforgeeks.org/problems/number-of-coins1824/1
#=======================================================================
import math
#Recursive
def minNoCoin(Carr,S,N):
    if S==0:return 0
    if S!=0 and N==0:return math.inf
    if S>=Carr[N-1]:
        return min(1+minNoCoin(Carr,S-Carr[N-1],N),
        minNoCoin(Carr,S,N-1))
    else:
        return minNoCoin(Carr,S,N-1)
Carr=[1,2,3]
S=12
N=3
# print(minNoCoin(Carr,S,N))

import math
dp=[]
#Memoization
class Solution:
    def minNoCoin(self,Carr,S,N):
        global dp
        if S==0:return 0
        if S!=0 and N==0:return math.inf
        if dp[N][S]!=-1:return dp[N][S]
        if S>=Carr[N-1]:
            dp[N][S]=min(1+self.minNoCoin(Carr,S-Carr[N-1],N),
            self.minNoCoin(Carr,S,N-1))
            return dp[N][S]
        else:
            dp[N][S]=self.minNoCoin(Carr,S,N-1)
            return dp[N][S]
	def minCoins(self, coins, M, V):
		# code here
		global dp
		dp=[[-1]*(V+1) for _ in range(M+1)]
		if self.minNoCoin(coins,V,M)==math.inf:
		    return -1
		return self.minNoCoin(coins,V,M)
