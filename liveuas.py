class Node:
    def __init__(self, cicilan, kode_va, nama_pembayar, jumlah_tagihan, biaya_admin, total_keseluruhan):
        self.cicilan = cicilan  
        self.kode_va = kode_va 
        self.nama_pembayar = nama_pembayar
        self.jumlah_tagihan = jumlah_tagihan
        self.biaya_admin = biaya_admin
        self.total_keseluruhan = total_keseluruhan
        self.next = None  

def tampilkan_cicilan(): 
    cicilan_list = [
        "1. Kredivo",
        "2. Home Credit",
        "3. SPayLater",
        "4. GoPay Later",
        "5. Indodana"
    ]
    print("Pilih jenis Cicilan:") 
    for cicilan in cicilan_list: 
        print(cicilan)

def pilih_cicilan():
    tampilkan_cicilan()
    while True: 
        pilihan = int(input("\nPilih cicilan (1-5): "))
        if 1 <= pilihan <= 5:
            return pilihan
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-5.")

def buat_tagihan(cicilan):
    kode_va = input("Masukkan kode VA: ")
    nama_pembayar = input("Masukkan nama pembayar: ")
    jumlah_tagihan = int(input("Masukkan jumlah tagihan: "))
    biaya_admin = 2500
    total_keseluruhan = jumlah_tagihan + biaya_admin
    
    return kode_va, nama_pembayar, jumlah_tagihan, biaya_admin, total_keseluruhan

def tampilkan_tagihan(head):
    current_node = head 
    while current_node:
        print(f"Kode VA: {current_node.kode_va}, Nama Pembayar: {current_node.nama_pembayar}, "
              f"Jumlah Tagihan: {current_node.jumlah_tagihan}, Biaya Admin: {current_node.biaya_admin}, "
              f"Total Keseluruhan: {current_node.total_keseluruhan}, Cicilan: {current_node.cicilan}")
        current_node = current_node.next

def cari_cicilan(nama_cicilan, head):  
    results = []
    current_node = head
    while current_node:
        if current_node.cicilan == nama_cicilan:
            results += [current_node]
        current_node = current_node.next
    return results  

def menu_pencarian(head):
    print("\nDaftar Cicilan yang Tersedia:")
    tampilkan_cicilan()  
    pilihan_cicilan = int(input("Pilih cicilan berdasarkan nomor (1-5): "))
    
    if 1 <= pilihan_cicilan <= 5:
        cicilan_names = [
            "Kredivo",
            "Home Credit",
            "SPayLater",
            "GoPay Later",
            "Indodana"
        ]
        nama_cicilan = cicilan_names[pilihan_cicilan - 1]
        hasil = cari_cicilan(nama_cicilan, head)
        
        if hasil:
            print(f"Cicilan '{nama_cicilan}' ditemukan dengan detail berikut:")
            for tagihan in hasil:
                print(f"Kode VA: {tagihan.kode_va}, Nama Pembayar: {tagihan.nama_pembayar}, "
                      f"Jumlah Tagihan: {tagihan.jumlah_tagihan}, Biaya Admin : {tagihan.biaya_admin}, "
                      f"Total Keseluruhan: {tagihan.total_keseluruhan}, Cicilan: {tagihan.cicilan}")
        else:
            print(f"Cicilan '{nama_cicilan}' tidak ditemukan.")
    else:
        print ("Pilihan tidak valid. Silakan pilih nomor cicilan yang benar.")

def bubble_sort(head):  
    if head is None:
        return head

    pindah = True
    while pindah:
        pindah = False
        current_node = head
        while current_node.next:
            if current_node.jumlah_tagihan > current_node.next.jumlah_tagihan:
                current_node.cicilan, current_node.next.cicilan = current_node.next.cicilan, current_node.cicilan
                current_node.kode_va, current_node.next.kode_va = current_node.next.kode_va, current_node.kode_va
                current_node.nama_pembayar, current_node.next.nama_pembayar = current_node.next.nama_pembayar, current_node.nama_pembayar
                current_node.jumlah_tagihan, current_node.next.jumlah_tagihan = current_node.next.jumlah_tagihan, current_node.jumlah_tagihan
                current_node.biaya_admin, current_node.next.biaya_admin = current_node.next.biaya_admin, current_node.biaya_admin
                current_node.total_keseluruhan, current_node.next.total_keseluruhan = current_node.next.total_keseluruhan, current_node.total_keseluruhan
                pindah = True
            current_node = current_node.next

def menu_sorting(head):
    bubble_sort(head)
    print("Tagihan telah diurutkan berdasarkan jumlah tagihan:")
    tampilkan_tagihan(head)

if __name__ == "__main__":
    head = None  
    tail = None  

    while True:
        print("\nMenu:")
        print("1. Pilih Cicilan")
        print("2. Cari Cicilan")
        print("3. Sorting Tagihan")
        print("4. Keluar")
        pilihan_menu = int(input("Pilih menu (1-4): "))
        
        if pilihan_menu == 1:
            pilihan_cicilan = pilih_cicilan()
            cicilan_names = [
                "Kredivo",
                "Home Credit",
                "SPayLater",
                "GoPay Later",
                "Indodana"
            ]
            print(f"Nama Tagihan Cicilan: {cicilan_names[pilihan_cicilan - 1]}")

            kode_va, nama_pembayar, jumlah_tagihan, biaya_admin, total_keseluruhan = buat_tagihan(cicilan_names[pilihan_cicilan - 1])
            new_node = Node(cicilan_names[pilihan_cicilan - 1], kode_va, nama_pembayar, jumlah_tagihan, biaya_admin, total_keseluruhan)

            if head is None:  
                head = new_node
                tail = new_node
            else:  
                tail.next = new_node
                tail = new_node  

            print("Tagihan baru telah ditambahkan.")
            
        elif pilihan_menu == 2:
            menu_pencarian(head)
        
        elif pilihan_menu == 3:
            menu_sorting(head)
        
        elif pilihan_menu == 4:
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")