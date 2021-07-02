n=5
w=10
g=[400,500,200,300,350]
p=[5,5,3,4,3]
def goldMining(n,w,g,p):
    #初始化数组，用于存储信息，注意为了更好计算，共有11列，第一列作为辅助位
    dp = [[0 for _ in range(w + 1)] for _ in range(n)]
    print(dp)
    #边界就是10个人只挖第1个金矿
    #[0, 0, 0, 0, 0, 400, 400, 400, 400, 400, 400]
    for i in range(1,w + 1):
        if i<p[0]:
            dp[0][i]=0
        else:
            dp[0][i]=g[0]
    #依次遍历金矿，人数
    for i in range(1,n):
        for j in range(1,w + 1):
            #如果当前人数小于挖这座金矿的人数
            if j<p[i]:
                #则当前最大金矿就是挖前一个金矿的相应人数的值
                dp[i][j]=dp[i-1][j]
            else:
                #否则就用如下公式计算
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-p[i]]+g[i])
    return dp

dp=goldMining(n,w,g,p)
for i in range(len(dp)):
    print(dp[i])
    
    
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
[0, 0, 0, 0, 0, 400, 400, 400, 400, 400, 400]
[0, 0, 0, 0, 0, 500, 500, 500, 500, 500, 900]
[0, 0, 0, 200, 200, 500, 500, 500, 700, 700, 900]
[0, 0, 0, 200, 300, 500, 500, 500, 700, 800, 900]
[0, 0, 0, 350, 350, 500, 550, 650, 850, 850, 900]



#递归方法
def gold_mining(n ,w, G, P):
    """
    利用递归实现动态规划算法过程
    :param n:
    :param w:
    :param G:
    :param P:
    :return:
    """
    if n <= 1 and w < P[0]:
        return 0
    if n == 1 and w >= P[0]:
        return G[0]
    if n > 1 and w < P[n-1]:
        return gold_mining(n-1, w, G, P)
    if n > 1 and w >= P[n-1]:
        return max(gold_mining(n-1, w, G, P), gold_mining(n-1, w-P[n-1], G, P) + G[n-1])


if __name__ == '__main__':
    G = [400, 500, 200, 300, 350]
    P = [5, 5, 3, 4, 3]
    n = 5
    w = 10
    print(gold_mining(n, w, G, P))
   
  ===
  900
    
    
