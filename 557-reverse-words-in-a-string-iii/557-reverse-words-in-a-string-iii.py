class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        print(li)
        li2 = ''
        st2 = ''
        for i,st in enumerate(li):
            st = list(st)
            st = st[::-1]            
            st2 += ''.join(st)
            li2 += st2
            st2 = ' '
        return li2