# Program menghitung total belanja dengan PPN 11%

def hitung_total_belanja():
    print("=== Program Penghitungan Total Belanja & PPN 11% ===")

    daftar_harga = []

    while True:
        try:
            masukan = input("Masukkan harga barang (ketik 'selesai' atau 's' untuk mengakhiri): ")
            if masukan.lower() in ['selesai', 's']:
                break

            harga = float(masukan)
            if harga < 0:
                print("Harga tidak boleh bernilai negatif. Silakan coba lagi.")
                continue

            daftar_harga.append(harga)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang benar atau ketik 'selesai'.")

    if not daftar_harga:
        print("\nBelum ada barang yang dimasukkan.")
        return

    subtotal = sum(daftar_harga)
    tarif_ppn = 0.11
    jumlah_ppn = subtotal * tarif_ppn
    total_akhir = subtotal + jumlah_ppn

    print("\n" + "=" * 35)
    print("          STRUK BELANJA          ")
    print("=" * 35)
    print(f"Jumlah Barang    : {len(daftar_harga)} item")
    print(f"Subtotal         : Rp {subtotal:,.2f}")
    print(f"PPN (11%)        : Rp {jumlah_ppn:,.2f}")
    print("-" * 35)
    print(f"Total Pembayaran : Rp {total_akhir:,.2f}")
    print("=" * 35)


if __name__ == "__main__":
    hitung_total_belanja()