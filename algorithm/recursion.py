#coding:utf-8


def hannuo(num,sour,assis,dest):
    # sour  : A
    # assis : B
    # dest  : C
    if num == 1:
        # 只有一个盘子，从A移动到C
        print sour,"->",dest
    else:
        # 有多个盘子，先将上面的盘子移动到B
        hannuo(num-1,sour,dest,assis)
        # 移动到B,需要借助C，假如有三个盘子的话，应该是先将其移动至C再移动至B，这边应该打印移动至C的
        # 那一步
        print sour,"---->",dest
        # 将处于B柱的盘子移动到C柱上，借助A柱
        hannuo(num-1,assis,sour,dest) 

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)


if __name__ == "__main__":
    #hannuo(4,'a','b','c')
    print factorial(10)
