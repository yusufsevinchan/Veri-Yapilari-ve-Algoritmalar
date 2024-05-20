"""
Proje 2
[16,21,11,8,12,22] -> Merge Sort

Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.
"""

#Solution (Explain)
"""
                                            [16,21,11,8,12,22]

                                          [16,21,11]    |   [8,12,22]

                                   [16,21]      |   [11]   ||       [8,12]   |   [22]

                                [16]  |  [21]   ||  [11]    |||  [8]  ||  [12]  |  [22]

                                                --=>> Merging <<=--

                                   [16, 21]     |   [11]   ||       [8, 12]  |   [22]

                                        [11, 16, 21]        |       [8, 12, 22]

                                                [8, 11, 12, 16, 21, 22]
"""
#Her adımda ikiye bölünüyor N elemanlı dizi (koleksiyon) 2^x=N x = log N
#Ve Birleştirme (Merging) esnasında her eleman için, N kez, kontrol yapılıyor.              Sonuç = N * Log N =>O(N LogN)