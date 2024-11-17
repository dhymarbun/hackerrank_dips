# Tamus ialah pemilik Toko ABC yang menjual berbagai perlengkapan olahraga. Salah satu alat olahraga yang paling laris di Toko ABC adalah bola. Cara Tamus menjual bola cukup unik, yakni dengan ketentuan sebagai berikut.

# Jika seseorang membeli satu jenis bola dengan jumlah bola yang dibeli ganjil, harga tiap bola adalah 10000.
# Jika seseorang membeli satu jenis bola dengan jumlah bola yang dibeli genap, harga tiap bola adalah 11000.
# Jika seseorang membeli lebih dari satu jenis bola dengan jumlah bola yang dibeli ganjil, harga tiap bola adalah 15430.
# Jika seseorang membeli lebih dari satu jenis bola dengan jumlah bola yang dibeli genap, harga tiap bola adalah 17250.
# Tentukan total pemasukan yang diperoleh Tamus dari penjualan bola!

# Input Format
# Bola(daftar_bola)
# daftar_bola: list of list banyaknya bola yang dibeli, tiap elemennya adalah data satu pembeli.

# Constraints
# Semua atom dalam daftar_bola dipastikan tidak negatif.

# Output Format
# Total pendapatan Tamus dari penjualan bola.

# Sample Input 0
# Bola([1, 2, 3])
# Sample Output 0
# 62000

# Sample Input 1
# Bola([4])
# Sample Output 1
# 44000

# Sample Input 2
# Bola([123, [122, 145]])
# Sample Output 2
# 5349810

def IsEmpty(S):
    return S == []

def KonsLo(L,S):
    return [L] + S

def FirstList(S):
    return S[0]

def TailList(S):
    return S[1:]

def IsAtom(S):
    return type(S) != list

def IsList(S):
    return type(S) == list

def SumLoL(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return FirstList(S) + SumLoL(TailList(S))
    elif IsList(FirstList(S)):
        return SumLoL(FirstList(S)) + SumLoL(TailList(S))
    else:
        return 0

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:]

def Bola(daftar_bola):
    if IsEmpty(daftar_bola):
        return 0
    elif IsAtom(FirstList(daftar_bola)):
        if FirstList(daftar_bola) % 2 == 1:
            return FirstList(daftar_bola) * 10000 + Bola(TailList(daftar_bola))
        else:
            return FirstList(daftar_bola) * 11000 + Bola(TailList(daftar_bola))
    elif IsList(FirstList(daftar_bola)):
        if IsEmpty(FirstList(daftar_bola)):
            return Bola(TailList(daftar_bola))
        elif SumLoL(FirstList(daftar_bola)) % 2 == 1:
            return SumLoL(FirstList(daftar_bola)) * 15430 + Bola(TailList(daftar_bola))
        else:
            return SumLoL(FirstList(daftar_bola)) * 17250 + Bola(TailList(daftar_bola))

        
print(eval(input()))