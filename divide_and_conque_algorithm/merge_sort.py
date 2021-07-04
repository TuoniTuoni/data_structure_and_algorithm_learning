#递归法recursion
def mergeSort(myList):						#传入参数myList
     if len(myList)<2:							#如果myList只有一个元素，终止
       return
     cut = len(myList)//2						#找到列表中点
     listA = myList[:cut]						#左子列表
     listB = myList[cut:]						#右子列表
     mergeSort(listA)							#把左子列表归并排序
     mergeSort(listB)							#把右子列表归并排序
     pointerA = 0								#指针A
     pointerB = 0								#指针B
     counter=0								#定义一个counter
     while (pointerA<len(listA) and pointerB <len(listB)):	#如果两个指针都没走到头
       if(listA[pointerA]<listB[pointerB]):				#比子列表元素大小
         myList[counter]=listA[pointerA]				#小的元素替换myList[counter]
         pointerA+=1								#移动指针
       else:
         myList[counter]=listB[pointerB] 
         pointerB+=1
       counter+=1								#counter加一
     while pointerA<len(listA):					#如果指针B走到头了但指针A没有
       myList[counter]=listA[pointerA]				#指针A对应的元素替换myList[counter]
       pointerA+=1
       counter+=1
     while pointerB<len(listB):					#如果指针A走到头了但指针B没有	
       myList[counter]=listB[pointerB] 				#指针B对应的元素替换myList[counter]
       pointerB+=1
       counter+=1
listX = [2,3,4,1,3,0]							
mergeSort(listX)
print(listX)

[0, 1, 2, 3, 3, 4]



#迭代法iteration

def mergeSort(myList):								#传入参数myList
    length = len(myList)     							#myList的长度
    n = 1									#n为子数组长度，初始值为1
    while n <length:							#如果子数组长度小于myList的长度
      for i in range(0,length,n*2):					#利用for loop把子数组成对排序
        listA = myList[i:i+n]						#listA与listB为一对长度为n的子数组
        listB = myList[i+n:i+n*2]
        pointerA = 0							#利用指针将listA与listB排序
        pointerB = 0
       	counter = i
        while (pointerA<len(listA) and pointerB <len(listB)):
           if(listA[pointerA]<listB[pointerB]):
             myList[counter]=listA[pointerA]
             pointerA+=1
           else:
             myList[counter]=listB[pointerB] 
             pointerB+=1
           counter+=1
        while pointerA<len(listA):				
           myList[counter]=listA[pointerA]			
           pointerA+=1
           counter+=1
        while pointerB<len(listB):				
           myList[counter]=listB[pointerB] 				
           pointerB+=1
           counter+=1
      n=n*2									#将n乘2
listX = [-2,9,0,8,5,-4,8]
mergeSort(listX)
print(listX)

[-4, -2, 0, 5, 8, 8, 9]
