a=int(input());
sum=0;
b=1;
c=a;
while b<=a:
    sum=sum+b*c;
    b=b+1;
    c=c-1;
print(sum)