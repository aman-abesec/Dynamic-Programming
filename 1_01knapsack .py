#===========================================
#01 knapsack Recursive Solution
#==========================================
def knapsackRec(wt,val,n,W):
    if W==0 or n==0:return 0
    if wt[n-1]<=W:
        return max(val[n-1]+knapsackRec(wt,val,n-1,W-wt[n-1]),
        knapsackRec(wt,val,n-1,W))
    else:
        return knapsackRec(wt,val,n-1,W)

#===========================================
#01 knapsack Memorization
#==========================================
m=7
n=4
dpMat=[[-1]*(m+1)]*(n+1)
def knapsackMemo(wt,val,n,W):
    if W==0 or n==0:return 0
    global dpMat
    if dpMat[n][W]!=-1:return dpMat[n][W]
    if W>=wt[n-1]:
        dpMat[n][W]=max(val[n-1]+knapsackMemo(wt,val,n-1,W-wt[n-1]),
        knapsackMemo(wt,val,n-1,W))
        return dpMat[n][W]
    else:
        dpMat[n][W]=knapsackMemo(wt,val,n-1,W)
        return dpMat[n][W]

#===========================================
#01 knapsack Top Down
#==========================================
m,n=7,4
dpTD=[[-1]*(m+1) for _ in range(n+1)]
def knapsackTD(wt,val,n,W):
    global dpTD
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                dpTD[i][j]=0
    for i in range(1,n+1):
        for j in range(1,W+1):
            if j>=wt[i-1]:
                dpTD[i][j]=max((val[i-1]+dpTD[i-1][j-wt[i-1]]),dpTD[i-1][j])
            else:
                dpTD[i][j]=dpTD[i-1][j]
    return dpTD[n][W]
# wt=[1,3,4,5]
# val=[1,4,5,7]
# W,n=7,4
# print(knapsackTD(wt,val,n,W))

#====================================================================
#             Subset Sum Problem
#====================================================================
#Recursive Solution
def subSetRec(arr,s,n):
    if s==0:return True
    if s!=0 and n==0:return False
    if s>=arr[n-1]:
        return subSetRec(arr,s-arr[n-1],n-1) or subSetRec(arr,s,n-1)
    else:
        return subSetRec(arr,s,n-1)

#Memorization Solution
s,N=10,5
dpSubMat=[[-1]*(s+1) for _ in range(N+1)]
def subSetMemo(arr,s,n):
    if s==0:return True
    if s!=0 and n==0:return False
    if dpSubMat[n][s]!=-1:return dpSubMat[n][s]
    if s>=arr[n-1]:
        dpSubMat[n][s]=subSetRec(arr,s-arr[n-1],n-1) or subSetRec(arr,s,n-1)
        return dpSubMat[n][s]
    else:
        dpSubMat[n][s]=subSetRec(arr,s,n-1)
        return dpSubMat[n][s]

#Top Down Approach
dpSubMat=[[-1]*(s+1) for _ in range(N+1)]
def subSetTD(arr,s,N):
    for i in range(s+1):
        dpSubMat[0][i]=0
    for j in range(N+1):
        dpSubMat[j][0]=1
    for i in range(1,N+1):
        for j in range(1,s+1):
            if j>=arr[i-1]:
                dpSubMat[i][j]=dpSubMat[i-1][j-arr[i-1]] or dpSubMat[i-1][j]
            else:
                dpSubMat[i][j]=dpSubMat[i-1][j]
    return dpSubMat[N][s]

#====================================================================
#             Equal Sum partition
#====================================================================
def equalSumPartition(arr,n):
    s=sum(arr)
    if s%2!=0:
        return 0
    else:
        return subSetTD(arr,s//2,n)

#===============================================================
#       Count of Subsets Sum with a Given Sum
#==============================================================
def CountSubsetSum(arr,s,N):
    if s==0:return 1
    if s!=0 and N==0: return 0
    if arr[N-1]<=s:
        return CountSubsetSum(arr,s-arr[N-1],N-1)+CountSubsetSum(arr,s,N-1)
    else:
        return CountSubsetSum(arr,s,N-1)
# N,s=10,31
# arr=[9,7,0,3,9,8,6,5,7,6]
# print(CountSubsetSum(arr,s,N))

N,s=10,31
arr=[9,7,0,3,9,8,6,5,7,6]
def CountSubsetSum(arr,s,N):
    dpSubMat=[[-1]*(s+1) for _ in range(N+1)]
    for i in range(s+1):
        dpSubMat[0][i]=0
    for j in range(N+1):
        dpSubMat[j][0]=1
    for i in range(1,N+1):
        for j in range(1,s+1):
            if j>=arr[i-1]:
                dpSubMat[i][j]=dpSubMat[i-1][j-arr[i-1]] + dpSubMat[i-1][j]
            else:
                dpSubMat[i][j]=dpSubMat[i-1][j]
    return dpSubMat[N][s]
# print(CountSubsetSum(arr,s,N))

#====================================================
#  Minimum Subset Sum Difference
#===================================================
import math
def MinSetDiff(arr,N):
    s=sum(arr)
    dpSubMat=[[-1]*(s+1) for _ in range(N+1)]
    for i in range(s+1):
        dpSubMat[0][i]=0
    for j in range(N+1):
        dpSubMat[j][0]=1
    for i in range(1,N+1):
        for j in range(1,s+1):
            if j>=arr[i-1]:
                dpSubMat[i][j]=dpSubMat[i-1][j-arr[i-1]] or dpSubMat[i-1][j]
            else:
                dpSubMat[i][j]=dpSubMat[i-1][j]
    ans=math.inf
    for m in range((s)//2+1):
        if dpSubMat[N][m]==1:
            ans=min(ans,s-2*m)
    return ans
# arr=[1, 6, 11, 5]
# N=4
# print(MinSetDiff(arr,4))

#====================================================
#  Count the number of subset with a given difference
#===================================================
def countSetWithDiff(arr,diff):
    s=(sum(arr)+diff)//2
    N=len(arr)
    return CountSubsetSum(arr,s,N)
arr=[1,1,2,3]
diff=1
# print(countSetWithDiff(arr,diff))

#====================================================
#  Target sum
#===================================================
def targetSum(arr,n,tar,ans=0):
    if tar==ans and n==0:return 1
    if tar!=ans and n==0:return 0
    return targetSum(arr,n-1,tar,ans+arr[n-1])+targetSum(arr,n-1,tar,ans-arr[n-1])
print(targetSum([1,1,2,3],4,1))
