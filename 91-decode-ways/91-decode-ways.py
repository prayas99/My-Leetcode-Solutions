class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[len(s)] = 1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp[i] = 0
            elif i==len(s)-1:
                dp[i] = 1
            elif s[i]=='1' or (s[i]=='2' and int(s[i+1])<7):
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0] 