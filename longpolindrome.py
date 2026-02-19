class Solution:
    def longpalindrome(self,s:str) -> str:
        if len(s) ==0:
            return ""
        def expand(left,right):
            if left >=0 and right <len(s) and s[left]==s[right]:
                left -=1
                right +=1
            return s[left+1:right]
        longest =""
        for i in range(len(s)):
            odd_pal=expand(i,i)
            even_pal=expand(i,i+1)
            if len(odd_pal) > len(longest):
                longest= len(odd_pal)
            if len(even_pal) > len(longest):
                longest=len(even_pal)
        return longest        