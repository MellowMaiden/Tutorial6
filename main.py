def f(x):
    return -x**2 + 3*x -2
print(" ##### f(x) = -x^2 +3x -2 from a=1 b=2")
for x in (n/10 for n in range(10,21)):
    print(f"when x ={x} => f(x)= {f(x)}")
print("##### Example of trapezium rule values #####")
first=f(1.0)
last=f(2.0)
print(f"first={first}")
print(f"last={last}")
middle= sum (f(n/10) for n in range(11,20))
print(f"middle sum= {middle}")
ita=0.1/2*(first+last+2*middle)
print(f"Integration is approximately {ita}")
print("True value of integration is 1/6")
error=abs(1/6-ita)/(1/6)*100
print(f"Therefore the error is {error}%")
