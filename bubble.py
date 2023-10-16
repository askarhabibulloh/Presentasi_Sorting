#dikasi delay biar bisa diamati
import time

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag untuk memeriksa apakah ada pertukaran elemen
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Menukar elemen jika elemen saat ini lebih besar dari elemen berikutnya
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                 # Mencetak array setiap akhir iterasi
                print(f"Iterasi {i + 1}: {arr}\n")
                time.sleep(2)
        
        
        
        if not swapped: #setara dengan if swapped==false
            break

#penggunaan 
arr = [64, 34, 25, 12, 22, 11, 90]
print("\n\n\nArray sebelum diurutkan:")
print(arr,"\n\n\n")
bubble_sort(arr)
print("\n\n\n\nArray setelah diurutkan:\n\n\n")
print(arr)
