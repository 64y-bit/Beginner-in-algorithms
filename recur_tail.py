#python尾递归
#Python 默认不支持尾递归优化，
# 因此即使函数是尾递归形式，仍然可能会遇到栈溢出问题。
def recur_tail(n,res):
    #终止条件
    if n==0:
        return res
    #调用
    return recur_tail(n-1,res+n)

"""Driver code"""
if __name__=="__main__":
    n=5
    res=recur_tail(n,0)
    print(f"尾递归求和结果为: {res}")
"""n=5,res=0
(5,0)-->(4,5)-->(3,4+5)-->(3-1,9+3)-->(1,2+12)-->(0,14+1)-->15"""
#res=5+3+2+1=15