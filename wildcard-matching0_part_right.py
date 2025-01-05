class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        stack=''
        len_s = len(s)
        len_p = len(p)
        i = 0
        j = 0
        while i<len_s and j<len_p:
            cur_s = s[i]
            cur_p = p[j]

            if cur_p=="?":
                i+=1
                j+=1
            elif cur_p=='*':
                while j+1<len_p:
                    next_p = p[j+1]
                    if next_p=="*":
                        break
                    else:
                        stack+=next_p
                    j+=1

                if stack:
                    matched = False
                    len_st = len(stack)
                    while i<len_s-len_st:
                        print("stack:", stack)
                        if s[i:i+len_st]==stack:
                            stack=""
                            i = i + len_st
                            matched = True
                            break
                        
                        i+=1
                        
                    print("matched:", matched)
                    if not matched:
                        return False
                else:
                    j+=1

            elif cur_s==cur_p:
                i+=1
                j+=1
            else:
                return False

        if cur_p!="*":
            if i<len_s-1:
                return False

            if j<len_p-1:
                return False

            if i==len_s-1 and j>len_p-1:
                return False
        else:
            if j<len_p-1:
                return False

        print("i:",i)
        print("j:",j)

        return True

        