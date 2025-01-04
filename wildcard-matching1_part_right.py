class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        stack=''
        len_s = len(s)
        len_p = len(p)
        i1 = 0
        j1 = len_s-1

        i2 = 0
        j2 = len_p-1


        while i2<=j2 and p[i2]!="*":
            if i1>j1:
                return False

            if p[i2]=="?":
                i1+=1
                i2+=1
            elif s[i1]==p[i2]:
                i1+=1
                i2+=1
            else:
                return False
        

        while i2<=j2 and p[j2]!="*":
            if i1>j1:
                return False

            if p[j2]=="?":
                j1-=1
                j2-=1
            elif s[j1]==p[j2]:
                j1-=1
                j2-=1
            else:
                return False

        print("i1:", i1)
        print("j1:", j1)
        print("i2:", i2)
        print("j2:", j2)
        print("s:", s[i1:j1+1])
        print("p:", p[i2:j2+1])


        if i2>j2:
            if i1<=j1:
                return False
        # if :
        #     if i1<=j1:
        #         return False
        
        if i2==j2 and p[i2]=="*":
            return True

        if i1>j1 and i2>j2:
            return True


        stack_list = []
        stack = ""
        while i2<=j2:
            if p[i2]=="*":
                if stack:
                    stack_list.append(stack)
                    stack = ""
            else: #p[i2]!="*":
                stack+=p[i2]

            i2+=1


        # if i1>j1 and (not stack_list):
        #     return True

        if not stack_list:
            return True


        print("s:", s[i1:j1+1])
        print("p:", stack_list)

        def check_equal_with_question(s,p):
            if len(s)!=len(p):
                return False
            
            for i in range(len(p)):
                if p[i]=="?":
                    continue
                elif s[i]==p[i]:
                    continue
                else:
                    return False
            
            return True

        cur_stack = stack_list.pop(0)
        len_stack = len(cur_stack)
        while i1<=j1:
            print("cur_stack:", cur_stack)
            cur_s = s[i1:i1+len_stack]
            if check_equal_with_question(cur_s, cur_stack):
                if stack_list:
                    len_stack = len(cur_stack)
                    i1+=len_stack
                    cur_stack = stack_list.pop(0)
                else:
                    return True
            else:
                i1+=1

        # print("s:", s[i1:j1+1])
        # print("p:", p[i2:j2+1])


        return False
