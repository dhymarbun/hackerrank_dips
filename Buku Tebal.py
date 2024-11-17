# Kiko adalah seorang jenius yang sangat gemar membaca. Setiap hari, tak ada buku yang tak ia baca. Kiko sudah terbiasa membaca buku-buku tebal sehingga ia hanya ingin membaca buku yang tebal saja. Di dalam perpustakaan pribadinya, ia memiliki segudang buku dari berbagai genre. Tiap pagi hari, pelayan pribadi Kiko membawa daftar sekumpulan buku untuk dibaca Kiko. Ia memberikan daftar judul buku dan banyaknya halaman masing-masing buku. Mata Kiko selalu tertuju pada buku yang paling tebal, yakni dengan jumlah halaman terbanyak.

# Input Format
# BukuTebal(daftar_buku)
# daftar_buku adalah list of list yang terdiri dari judul buku dan banyak halaman.

# Constraints
# daftar_buku tidak kosong
# elemen daftar_buku memiliki dua komponen: judul dan halaman
# tidak ada elemen list kosong dalam daftar_buku
# tidak ada elemen list of list dalam list of list daftar_buku
# judul buku dipastikan unik

# Output Format
# Mengembalikan judul buku dengan jumlah halaman terbanyak.

# Sample Input 0
# KutuBuku([['Kisah Sang Kancil', 80], ['Dongeng Putri Tidur', 80], ['Legenda Prambanan', 70]])
# Sample Output 0
# Kisah Sang Kancil

# Sample Input 1
# KutuBuku([['Ily', 380], ['Toko Kelontong Namiya', 400], ['Si Anak Badai', 322], ['Negeri 5 Menara', 423]])
# Sample Output 1
# Negeri 5 Menara

# Sample Input 2
# KutuBuku([['Diktat Dasar Pemrograman', 127], ['Algoritma dan Pemrograman', 95], ['Discrete Mathematics and Its Applications', 1071], ['Logic and Computer Design Fundamentals', 674]])
# Sample Output 2
# Discrete Mathematics and Its Applications

def Konso(e,L):
    return [e] + L

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Tail(L):
    return L[1:]

def firstList(S):
    return S[0]

def tailList(S):
    return S[1:]

def isOneElmt(S):
    return len(S) == 1

def BukuTebal(daftar_buku):
    if isOneElmt(daftar_buku):
        return FirstElmt(daftar_buku)
    else:
        buku_pertama = FirstElmt(daftar_buku)
        buku_tebal = BukuTebal(Tail(daftar_buku))

        if LastElmt(Konso(LastElmt(buku_pertama), [])) >= LastElmt(Konso(LastElmt(buku_tebal), [])):
            return buku_pertama
        else:
            return buku_tebal

def KutuBuku(daftar_buku):
    return FirstElmt(BukuTebal(daftar_buku))

print(eval(input()))