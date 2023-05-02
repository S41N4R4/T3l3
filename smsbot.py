#!/bin/env python3
dari telethon.sync impor TelegramClient
dari telethon.tl.types impor InputPeerUser
dari telethon.errors.rpcerrorlist impor PeerFloodError
impor configparser
impor os, sys
impor csv
impor acak
waktu impor

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
SLEEP_TIME = 30

kelas utama():

    def spanduk():
        
        cetak(f"""
    {re}╔╦╗{cy}┌─┐┬ ┌─┐{re}╔═╗ ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
    {re} ║ {cy}├┤ │ ├┤ {re}║ ╦ ╚═╗{cy}│ ├┬┘├─┤├─┘├┤ ├┬┘
    {re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝ ╚═╝{cy}└─┘┴└─┴ ┴┴ └─┘┴└─

                versi : 3.1
    youtube.com/channel/UCnknCgg_3pVXS27ThLpw3xQ
            """)

    def send_sms():
        mencoba:
            cpass = configparser.RawConfigParser()
            cpass.baca('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            telepon = cpass['cred']['telepon']
        kecuali KeyError:
            os.system('hapus')
            main.banner()
            print(re+"[!] jalankan python3 setup.py dulu!!\n")
            sys.keluar(1)

        klien = TelegramClient(telepon, api_id, api_hash)
         
        klien.sambungkan()
        jika bukan client.is_user_authorized():
            client.send_code_request(telepon)
            os.system('hapus')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Masukkan kode: '+re))
        
        os.system('hapus')
        main.banner()
        input_file = sys.argv[1]
        pengguna = []
        dengan open(input_file, encoding='UTF-8') sebagai f:
            baris = csv.reader(f,delimiter=",",lineterminator="\n")
            berikutnya(baris, Tidak ada)
            untuk baris dalam baris:
                pengguna = {}
                pengguna['nama pengguna'] = baris[0]
                pengguna['id'] = int(baris[1])
                pengguna['akses_hash'] = int(baris[2])
                pengguna['nama'] = baris[3]
                pengguna.tambahkan(pengguna)
        print(gr+"[1] kirim sms dengan ID pengguna\n[2] kirim sms dengan nama pengguna ")
        mode = int(input(gr+"Input : "+re))
         
        pesan = input(gr+"[+] Masukkan Pesan Anda : "+re)
         
        untuk pengguna di pengguna:
            jika modus == 2:
                jika pengguna['nama pengguna'] == "":
                    melanjutkan
                penerima = client.get_input_entity(pengguna['nama pengguna'])
            modus elif == 1:
                penerima = InputPeerUser(pengguna['id'],pengguna['akses_hash'])
            kalau tidak:
                print(re+"[!] Mode Tidak Valid. Keluar.")
                klien.putuskan()
                sys.keluar()
            mencoba:
                print(gr+"[+] Mengirim Pesan ke:", user['nama'])
                client.send_message(penerima, pesan.format(pengguna['nama']))
                print(gr+"[+] Menunggu {} detik".format(SLEEP_TIME))
                waktu.tidur(SLEEP_TIME)
            kecuali PeerFloodError:
                print(re+"[!] Mendapatkan Kesalahan Banjir dari telegram. \n[!] Skrip berhenti sekarang. \n[!] Silakan coba lagi setelah beberapa waktu.")
                klien.putuskan()
                sys.keluar()
            kecuali Pengecualian sebagai e:
                print(re+"[!] Kesalahan:", e)
                print(re+"[!] Mencoba melanjutkan...")
                melanjutkan
        klien.putuskan()
        print("Selesai. Pesan terkirim ke semua pengguna.")



main.send_sms()
