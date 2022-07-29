#===========================================
# Longest Common Subsequence(LCS)
#==========================================
#########PROBLEMS#########
#Largest Common Substring
#Print Largest Common Substring
#Shortest Common supersequence
#Print Shortest Common supersequence
#Min no. of insertion and deletion
#Largest Repeating Subsequence
#Length of largest Subsequence of a which is a substring in b
#Subsequence Matching Problem
#Count how many time a appear as subsequence in b
#Largest Palindrome Subsequence
#Largest Palindrome Substring
#Min no of deletion in a string to make itv a Palindrome
#Min no of insertion in a string to makke it a palindroome

#==================================================================================
# Length of Longest Common Subsequence(LCS)
#https://leetcode.com/problems/longest-common-subsequence/
#=================================================================================
# str1="abcdgh"
# str2="abedfhr"
str1="ABCDGH"
str2="ACDGHR"
m=len(str1)
n=len(str2)
#Recursiv
def LCSRec(str1,str2,m,n):
    if m==0 or n==0:return 0
    if str1[m-1]==str2[n-1]:
        return 1+LCSRec(str1,str2,m-1,n-1)
    else:
        return max(LCSRec(str1,str2,m-1,n),LCSRec(str1,str2,m,n-1))
# print(LCS(str1,str2,m,n))

#Memoization Solution
dpLCS=[[-1]*(n+1) for _ in range(m+1)]
def LCSMemo(str1,str2,m,n):
    if m==0 or n==0:return 0
    if dpLCS[m][n]!=-1:return dpLCS[m][n]
    if str1[m-1]==str2[n-1]:
        dpLCS[m][n]=1+LCSMemo(str1,str2,m-1,n-1)
        return dpLCS[m][n]
    else:
        dpLCS[m][n]=max(LCSMemo(str1,str2,m-1,n),LCSMemo(str1,str2,m,n-1))
        return dpLCS[m][n]
# print(LCSMemo(str1,str2,m,n))

#Top Down
def LCSTD(str1,str2,m,n):
    dpLCSTD=[[-1]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dpLCSTD[i][j]=0
    for i in range(m+1):
        for j in range(n+1):
            if str1[i-1]==str2[j-1]:
                dpLCSTD[i][j]=1+dpLCSTD[i-1][j-1]
            else:
                dpLCSTD[i][j]=max(dpLCSTD[i-1][j],dpLCSTD[i][j-1])
    return dpLCSTD[m][n]
# print(LCSTD(str1,str2,m,n))

#==================================================================================
# Length of Longest Common Substring(LCS)
#=================================================================================
# s1="geeksforgeeks"
# s2="geeksquiz"
# s1="LRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCO"
# s2="QHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCAC"
s1="ABCD"
s2="ABC"
m=len(s1)
n=len(s2)
def LCSubstringRec(s1,s2,m,n,c):
    if m==0 or n==0:return c
    if s1[m-1]==s2[n-1]:
        return LCSubstringRec(s1,s2,m-1,n-1,c+1)
    else:
        return max(c,LCSubstringRec(s1,s2,m,n-1,0),LCSubstringRec(s1,s2,m-1,n,0))

ans=0
dpSubMat=[[-1]*(n+1) for _ in range(m+1)]
def LCSubstringMemo(s1,s2,m,n):
    global ans
    if m==0 or n==0:return ans
    if dpSubMat[m][n]!=-1:return dpSubMat[m][n]
    if s1[m-1]==s2[n-1]:
        ans+=1
        dpSubMat[m][n]=max(ans,LCSubstringMemo(s1,s2,m-1,n-1,))
        return dpSubMat[m][n]
    else:
        ans=0
        dpSubMat[m][n]=max(ans,LCSubstringMemo(s1,s2,m,n-1),LCSubstringMemo(s1,s2,m-1,n))
        return dpSubMat[m][n]
print(LCSubstringMemo(s1,s2,m,n))
print(dpSubMat)
