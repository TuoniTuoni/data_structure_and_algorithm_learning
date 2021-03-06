# -*-coding:utf-8-*-
from cmath import pi, exp

#设A(x)度数为n-1，A为多项式的系数表示，例如[3,4,0,0], A的长度为二的幂次方
def FFT(A, w):#w为单位的n次本原单位根，比如，n=4时w=i 
    length = len(A)

    if length == 1:#如果A只有常数项，返回常数项系数
        return [A[0]]

    A_even = []#在偶数位置的系数，例如[a_0,a_2，a_4]
    A_odd = []#在奇数位置的系数，例如[a_1,a_3，a_5]
    for i in range(0, length // 2):
        A_even.append(A[2 * i])
        A_odd.append(A[2 * i + 1])
    F_even = FFT(A_even, w ** 2)
    F_odd = FFT(A_odd, w ** 2)
    x = 1
    values = [0 for i in range(length)]
    for i in range(0, length // 2):
        values[i] = F_even[i] + x * F_odd[i]
        values[i + length // 2] = F_even[i] - x * F_odd[i]
        x = x * w
    return values


def solver(A, B):#A，B的系数表示，长度为各自的度数#length为大于len(A)+len(B)-1最小的2的幂次方
    length = len(A) + len(B) - 1
    n = 1
    while 2 ** n < length:
        n += 1
    length = 2 ** n
    A.extend([0 for i in range(length - len(A))])#填充0，将A，B的长度扩展到length
    B.extend([0 for i in range(length - len(B))])

    w = exp(2 * pi * 1j / length)#计算w，单位的length次本原单位根
    A_values = FFT(A, w)#A，B的点值表示，长度为length
    B_values = FFT(B, w)
    C_values = [A_values[i] * B_values[i] for i in range(length)]#C的点值表示
 					#将C的点值表示转换为系数表示，FFT传入w的倒数
    result = [int((x / length).real) for x in FFT(C_values, w ** -1)]

    while result[-1] == 0:#将result尾部不必要的0删除
        del result[-1]
    return result


#FFT算法要求多项式的系数表示长度为2的幂次方，因此solver方法用0扩展长度。
if __name__ == '__main__':
    input_A, input_B = [3, 2, 3, 4], [2, 0, 1]
    print("A", input_A)
    print("B", input_B)
    result = solver(input_A, input_B)
    print("C", result)
    

A [3, 2, 3, 4]
B [2, 0, 1]
C [6, 4, 9, 10, 3, 4]    
    
