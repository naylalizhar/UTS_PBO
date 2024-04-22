class Buku:
    def _init_(self, judul, pengarang, isbn, tersedia=True):
        self.judul = judul
        self.pengarang = pengarang
        self.isbn = isbn
        self.tersedia = tersedia

    def _str_(self):
        return f"{self.judul} oleh {self.pengarang}"

class Anggota:
    def _init_(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if buku.tersedia:
            self.buku_dipinjam.append(buku)
            buku.tersedia = False
            print(f"{self.nama} telah meminjam {buku}")
        else:
            print("Maaf, buku tidak tersedia untuk dipinjam.")

    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            self.buku_dipinjam.remove(buku)
            buku.tersedia = True
            print(f"{self.nama} telah mengembalikan {buku}")
        else:
            print("Anda belum meminjam buku ini.")

class Perpustakaan:
    def _init_(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"{buku} telah ditambahkan ke dalam perpustakaan.")

    def cari_buku_berdasarkan_judul(self, judul):
        ditemukan = [buku for buku in self.daftar_buku if judul.lower() in buku.judul.lower()]
        if ditemukan:
            print(f"Buku ditemukan dengan judul yang mengandung '{judul}':")
            for buku in ditemukan:
                print(buku)
        else:
            print(f"Tidak ada buku yang ditemukan dengan judul yang mengandung '{judul}'.")

    def cari_buku_berdasarkan_pengarang(self, pengarang):
        ditemukan = [buku for buku in self.daftar_buku if pengarang.lower() in buku.pengarang.lower()]
        if ditemukan:
            print(f"Buku ditemukan oleh pengarang '{pengarang}':")
            for buku in ditemukan:
                print(buku)
        else:
            print(f"Tidak ada buku yang ditemukan oleh pengarang '{pengarang}'.")

if __name__ == "_main_":
    perpustakaan = Perpustakaan()

    buku1 = Buku("Dear J", "Idea Fina", "9786026144058")
    buku2 = Buku("Senjakala", "Risa Saraswati", "9786022202943")
    perpustakaan.tambah_buku(buku1)
    perpustakaan.tambah_buku(buku2)

    perpustakaan.cari_buku_berdasarkan_judul("Dear J")
    perpustakaan.cari_buku_berdasarkan_pengarang("Risa Saraswati")

    anggota1 = Anggota("Nayla", "023")

    anggota1.pinjam_buku(buku1)

    anggota1.kembalikan_buku(buku1)
