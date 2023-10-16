#pake highlight
from colorama import Fore, Style, init

init()  # Inisialisasi colorama

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Temukan nilai minimum dalam sisa list yang belum diurutkan
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            print("Iterasi", i + 1, ":", end=" ")
            
            # Cetak elemen dengan warna merah jika sedang ditukar
            for idx, element in enumerate(arr):
                if idx == i:
                    print(Fore.RED + f"({element})", end=" ")
                elif idx == min_index:
                    print(Fore.RED + f"{element}", end=" ")
                else:
                    print(Fore.RESET + f"{element}", end=" ")
            print(Style.RESET_ALL)

        # Tukar elemen minimum dengan elemen pertama dalam sisa list
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Contoh penggunaan Selection Sort
data = [64, 25, 12, 22, 11]
    
print("Data sebelum diurutkan:", data)
    
selection_sort(data)
    
print("Data setelah diurutkan:", data)
