'''
# https://cafe.daum.net/flowlife/RUrO/36
# 1. 알고리즘 sort
'''
#selection sort ------------------

arr = [4, 3, 5, 2, 1]



for i in range(0, len(arr)):  

    print('i가'+ str(i) +'일 때 ')  

    for j in range(i + 1, len(arr)):

        print('j는'+ str(j) + "번째와 비교,", end=' ')

        if arr[i] > arr[j]:

            temp = arr[i]

            arr[i] = arr[j]

            arr[j] = temp

    print()

        

print('정렬된 결과는 ')

for i in range(0, len(arr)):

    print(arr[i], end=' ')



print()

#bubble sort --------------------

arr = [4, 3, 5, 2, 1]



for i in range(0, len(arr) - 1):

    print('i가'+ str(i) +'일 때 ')  

    for j in range(0, len(arr) - i - 1):

        print('j는'+ str(j) + "번째와", end=' ')

        print(str(j + 1) + "번째와 비교,", end=' ')

        if arr[j] > arr[j + 1]:

            arr[j + 1], arr[j] = arr[j], arr[j + 1]

    print()



print('\n정렬된 결과는 ')

for i in range(0, len(arr)):

    print(arr[i], end=' ')