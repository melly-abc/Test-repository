#coding:utf-8
#Gauss-Legendre algorithm
if __name__ == "__main__":
  
 import math
 import sys

 #initial value setting
 a=1.0
 b=1.0/math.sqrt(2)
 t=1.0/4.0
 p=1.0

 sys.stdout.write('Input the number of iterations\n>n=')

 for i in range(int(input())):
  an=(a+b)/2.0
  b=math.sqrt(a*b)
  t-=p*(an-a)**2
  p*=2.0
  a=an

 print ((a+b)**2/(4*t))