#dikasi hoghlight di elemen yang sedang disorting
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
                sorted_arr = " ".join([f"\033[91m{num}\033[0m" if index == j or index == j+1 else str(num) for index, num in enumerate(arr)])
                print(f"Iterasi {i + 1}: {sorted_arr}\n")
                time.sleep(2)
        
        if not swapped: #setara dengan if swapped==false
            break

#penggunaan 
arr = [64, 34, 25, 12, 22, 11, 90]
print("\n\n\nArray sebelum diurutkan:\n\n")
print("Iterasi 0:"," ".join(map(str,arr)),"\n")
bubble_sort(arr)
print("\n\n\n\nArray setelah diurutkan:\n")
print(arr,"\n\n\n")
