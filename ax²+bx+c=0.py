import math
print("请依次输入ax²+bx+c=0（a≠0）的a,b,c")
global x1
global x2
global w
a=int(input())
b=int(input())
c=int(input())
w=b*b-4*a*c
if w<0:
    print("此题无解")
if w==0:
    print("此题只有一个解")
    x1=-b/2*a
    print("x=%.2f"%x1)
if w>0:
    print("此题有两个解")
    x1=(-b+math.sqrt(w))/2*a
    x2=(-b-math.sqrt(w))/2*a
    print("x1=%.2f"%x1)
    print("x2=%.2f"%x2)