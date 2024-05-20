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
[22,27,16,2,18,6] ->  Insertion Sort

-Yukarı verilen dizinin sort türüne göre aşamalarını yazalım:
---> [22,27,16,2,18,6]
               |
          =-----
Adım 1-> [2, 22,27,16,18,6]
                         |
             =------------
Adım 2-> [2, 6, 22,27,16,18]
                      |
                =------
Adım 3-> [2, 6, 16, 22,27,18]
                           |
                    =-------
Adım 4-> [2, 6, 16, 18, 22,27] #Bundan sonra kontrol edilsede sıralama bu şekilde olur. 

-Big-O Gösterimi:
En kötü durumda, iç döngünün her adımda çalışma sayısı:
adım: 0 kez
adım: 1 kez
adım: 2 kez
...
n. adım: n-1 kez 
n-0, n-1, n-2, n-3 adım ile gerçekleştiriyoruz yani n*(n-1)/2 = n^2-n/2 => Big-O: O(n^2) 

-Time Complexity: Dizi sıralandıktan sonra 18 sayısı, Average case: Aradığımız sayının ortada olmasıdır(sona yakın olsada zaten O(n^2))
Worst case ve Average case: O(n^2) 
Ancak sıralı listelerde (Best case) O(n) çünkü dizi zaten sıralıdır. İç döngü de bir kez çalışır
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

# Insertion Sort
list2 = [22, 27, 16, 2, 18, 6]
list_yazdir(list2)

count = len(list2)

for i in range(1, count):
    key = list2[i]
    j = i - 1
    # Sıralı kısmı sağa kaydırarak doğru pozisyonu bul
    while j >= 0 and key < list2[j]:
        list2[j + 1] = list2[j]
        j -= 1
    # Anahtarı doğru pozisyona yerleştir
    list2[j + 1] = key

list_yazdir(list2)
