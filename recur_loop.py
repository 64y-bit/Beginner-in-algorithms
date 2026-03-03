#前面提到栈溢出问题。现用一个现实的栈，手动管理递归调用数据
#迭代模拟递归过程,具体问题具体分析
"""学完栈之后理解"""
def recur_loop(n:int)->int:
    stack=[]
    res=0
    for i in range(n,0,-1):
        #n ->每次-1 ->n-1 ->每次-1 ->n-2 ->每次-1 ->...->1不含0
        #递归阶段，入栈操作（往下走）
        #stack=[5,4,3,2,1]
        stack.append(i)
    while stack:#返回（加法运算），出栈操作，不断弹出一个元素。
        res+=stack.pop()#pop()从list末尾依次移除一个元素。
        #内存res=0+1=1,1+2,1+2+3，1+2+3+4，直到n时。(n=5)
    return res
#res=1+2+3+4+5...+n
"""Driver code"""
if __name__=="__main__":
    n=5
    res=recur_loop(n)
    print(f"循环求和结果为: {res}")
#递：用入栈操作模拟递归函数调用参数压栈；
#归：用出栈操作模拟递归回溯过程，处理每一步的运算。