#coding:utf-8
# Leibniz formula
if __name__=="__main__":
 import sys
 
 pi=0.0

 sys.stdout.write('Input the number of iterations\n>n=')

 for i in range(int(input())):
        a=1.0
        for j in range(i):
                a*=(-1.0)
        pi+=a/(2.0*float(i)+1.0)

 print (4.0*pi)
