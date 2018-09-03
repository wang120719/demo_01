# -*- coding:utf-8 -*-
#
# @Author: Miss
# @Time:   18/8/17   10:50
# @Name:   djiago
#
# import django
#
# print(django.get_version())
def maxSum(list):
    maxsum = list[0]
    for i in range(len(list)):
        maxtmp = 0
        for j in range(i,len(list)):
            maxtmp += list[j]
            if maxtmp > maxsum:
                maxsum = maxtmp
                print(maxsum)
    return maxsum

if __name__ == '__main__':
    list = [-1,3,-3,4,-6,5]
    maxsum = maxSum(list)
    print("maxsum is",maxsum)