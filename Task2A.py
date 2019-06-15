def check(ins):
    stack=[]
    if ins[0]=='>':
        print (0)
    else:
       
        for i in ins:
            if i=='<':
                stack.append(i)
            elif i=='>':
                if (len(stack)>0 and (stack[len(stack)-1]=='<')):
                    stack.pop()
                else:
                    stack.append(i)
        print (len(ins)-len(stack))

n=int(input("Enter number of test cases: "))
for i in range(0,n):
    ins=input("Enter instruction: ")
    check(ins)
