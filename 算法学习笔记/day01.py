#coding:utf-8

def calXiaoji():
    for x in range(0,21):
        for y in range(0,40):
            z = 100 - x -y
            if z % 3==0 and x*5+y*3 + z/3 == 100:
                print "公鸡:",x,"母鸡:",y,"小鸡:",z
 
def shutui():
    res = [1,1]
    for i in range(2,13):
        s  = res[i-1] + res[i-2]
        res.append(res[i-1]+res[i-2])
    for i in range(len(res)):
        print res[i]
        
def fib1(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a

if __name__=='__main__':
    print fib1(5)
