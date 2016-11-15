#coding:utf-8

RATE = 0.0171
def backCasting(lastFetch):
    mon = range(48)
    mon[47] = lastFetch
    for i in range(47):
        mon[46-i] = (mon[47-i]+lastFetch)/(1+RATE/12)
    for i in mon[::-1]:
        print i
    
if __name__ == "__main__":
    backCasting(1000)
