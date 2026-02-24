
import numpy as np
# langsung ambil dari c jadi lebih cepat

my_list = [
    [1,2,3,4], 
    [5,6,7,8],
    [9,10,11,12]]

print(my_list*2)

#kalau numpy
arr = np.array(my_list)
print(my_list*2)

#stop di python itu selalu < dari (exclusive)
print("akses element 0", arr[0])

#slicing 
print(arr[ : ,2:3 ])
# kalau (,) itu dia misah gitu
# : itu dia ambil dari awal sampai akhir 
# ::2 itu berarti  dari awal sampai akhir, tapi dilongkap 2
print(arr*2)

# boolean indexing
print(arr[(arr > 15) & (arr < 22)])

# resyaping
# -1 itu automatic
# baris, jumlah isi tiap baris
# harus matrix persegi
reshape_arr = arr.reshape(4,-1)
print(arr.shape)

#transpose
transposedarr = arr.T
print(transposedarr)

#vstack
#itu tambah array ke bawah
#hstack

#special array
zero_arr = np.zeros((3,3), dtype = int)
ones_arr = np.ones((4,4), dtype=float)
