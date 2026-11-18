import threading
def d():
    print("\nSquare")
    for i in range(1,6):
        x=i*i
        print(x)

def dd(n):
    print("Cube")
    for i in range(1,n+1):
        x=i**3
        print(x)

t1=threading.Thread(target=d)
t2=threading.Thread(target=dd,args=(5,))

t1.join()
t2.join()
