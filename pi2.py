#coding:utf-8
# Leibniz formula

pi=0.0

sys.stdout.write('Input the number of iterations\n>n=')

for i in range(int(raw_input())):
        a=1.0
        for j in range(0,i):
                a=a*(-1.0)
        pi=pi+a/(2.0*float(i)+1.0)

print (4.0*pi)
