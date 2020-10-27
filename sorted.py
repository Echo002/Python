# default asc
listArray = [49, 38, 65, 97, 76, 13, 27, 49, 72, 15]

# 冒泡排序
# def BubbleSort(listArray):
#     n = len(listArray)
#     for i in range(n):
#         for j in range(1, n - i):
#             if listArray[j] < listArray[j - 1]:
#                 listArray[j - 1], listArray[j] = listArray[j], listArray[j - 1]
#     return listArray

# 选择排序
# def SelectSort(listArray):
#     n = len(listArray)
#     for i in range(n):
#         index = i
#         for j in range(i, n):
#             if listArray[j] < listArray[index]:
#                 index = j
#         listArray[i], listArray[index] = listArray[index], listArray[i]
#     return listArray

# 插入排序
# def InsertSort(listArray):
#     n = len(listArray)
#     for i in range(n - 1):
#         for j in range(i + 1, 0, -1):
#             if listArray[j] < listArray[j - 1]:
#                 listArray[j], listArray[j - 1] = listArray[j - 1], listArray[j]
#     return listArray

# 归并排序
# def MergeSort(listArray):
#     n = len(listArray)
#     if n <= 1:
#         return listArray
#     num = int(n / 2)
#     left = MergeSort(listArray[:num])
#     right = MergeSort(listArray[num:])
#     return Merge(left, right)

# def Merge(left, right):
#     l,r = 0, 0
#     result = []
#     while l < len(left) and r < len(right):
#         if left[l] > right[r]:
#             result.append(right[r])
#             r += 1
#         else:
#             result.append(left[l])
#             l += 1
#     result += left[l:]
#     result += right[r:]
#     return result

# 快速排序
def QuickSort(listArray):
    return Qsort(listArray,0,len(listArray)-1)

def Qsort(listArray, left, right):
    if left >= right:
        return listArray
    key = listArray[left]
    lp = left
    rp = right
    while lp < rp :
        while listArray[rp] >= key and lp < rp :
            rp -= 1
        while listArray[lp] <= key and lp < rp :
            lp += 1
        listArray[lp], listArray[rp] = listArray[rp], listArray[lp]
    listArray[left], listArray[lp] = listArray[lp], listArray[left]
    Qsort(listArray, left, lp - 1)
    Qsort(listArray, rp + 1, right)
    return listArray

# print(BubbleSort(listArray))
# print(SelectSort(listArray)) 
# print(InsertSort(listArray))
# print(MergeSort(listArray))
print(QuickSort(listArray))
