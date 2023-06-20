'''def cal(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
cal(3)'''



'''def rev(n):
    sum=0
    while n>0:
        a=n%10
        sum=sum*10+a
        n=n//10
    print(sum)
rev(10023)'''



'''
def rev():
    n=int(input("Enter a number:"))
    sum=0
    s=n
    while n>0:
        a=n%10
        sum=sum*10+a
        n=n//10
    if s==sum:
        print("Given number is palindrome")
    else:
        print("Given number is not a palindrome ")
rev()'''


'''def add():
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    sum=a+b
    print(sum)
add()'''

'''
def prime():
    n=int(input("Enter a number:"))
    for i in range(2,n):
        if n%i==0:
            print("Given number is not prime")
            break
    else:
        print("Given number is prime")
    
prime()'''

'''
def multiplaction():
    n=int(input("Enter a number:"))
    for i in range(1,11):
        print("{}*{}={}".format(n,i,n*i))
multiplaction()
'''

'''
def simpleint(p,t,r):
    print("The principal amount is :{}".format(p))
    print("The time period is :{}".format(t))
    print("The rate of interest is:{}".format(r))
    si=(p*t*r)/100
    print("The simple intrest is :{}".format(si))
    return si
simpleint(4000,12,2)'''










