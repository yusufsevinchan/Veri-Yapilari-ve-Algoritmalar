#Problem
"""
Proje 1
[22,27,16,2,18,6] ->  Insertion Sort

-Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
-Big-O gösterimini yazınız.
-Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız
Average case: Aradığımız sayının ortada olması
Worst case: Aradığımız sayının sonda olması
Best case: Aradığımız sayının dizinin en başında olması.
///
///
[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.
"""

#Solution for sort algorithm 1
"""
--->[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımı:
     -        -
Adım 1-> [2, 3,5,8,7,9,4,15,6]

            -
    Adım 2-> [2, 3, 5,8,7,9,4,15,6]

                   -        - 
        Adım 3-> [2, 3, 4, 8,7,9,5,15,6]

                          -     -
            Adım 4-> [2, 3, 4, 5,7,9,8,15,6]
"""

#Code
def swap(collection, index1, index2):
    if index1==index2: return
    
    temp=collection[index1]
    collection[index1]=collection[index2]
    collection[index2]=temp

def list_yazdir(collection):
    print(5*"--")
    print(*collection, sep=", ")


#Selection Sort
list = [22,27,16,2,18,6]
list_yazdir(list)

#küçükten büyüğe sıralamak için sırasıyla en küçük sayıyı bulup başa getiricem, sıralanana kadar
count=len(list)
min_index = 0
for index in range(count):
    min_index = index

    for index2 in range(index+1, count):

        if list[index2] < list[min_index]:
            min_index = index2
    
    swap(list, min_index, index)

list_yazdir(list)

