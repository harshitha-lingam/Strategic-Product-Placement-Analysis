def stack_search(key,a,b,c):
    while a:
        i=a.pop()
        if i==key:
            print(" element Found in stack  A")
            print("element not found in stack A==> moving to stack B")
            pass
            while b:
                j=b.pop()
                if j==key:
                    print(" element Found in stack  B")
                    print("element not found in stack B==> moving to stack C")
                    while c:
                        k=c.pop()
                        if k==key:
                            print(" element Found in stack  C")
                            return
                    print("element not found in stack C")
                    return
            print("element not found in stack B==> moving to stack C")
            while c:
                k=c.pop()
                if k==key:
                    print(" element Found in stack  C")
                    return
            print("element not found in stack C")
            return
   
key = input()
A=input().split()
B=input().split()
C=input().split()
print(stack_search(key,A,B,C))