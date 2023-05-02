#!/bin/env python3
dari telethon.sync impor TelegramClient
dari telethon.tl.functions.messages impor GetDialogsRequest
dari telethon.tl.types impor InputPeerEmpty, InputPeerChannel, InputPeerUser
dari telethon.errors.rpcerrorlist impor PeerFloodError, UserPrivacyRestrictedError
dari telethon.tl.functions.channels impor InviteToChannelRequest
impor configparser
impor os, sys
impor csv
impor traceback
waktu impor
impor acak

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def spanduk():
    cetak(f"""
{re}╔╦╗{cy}┌─┐┬ ┌─┐{re}╔═╗ ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re} ║ {cy}├┤ │ ├┤ {re}║ ╦ ╚═╗{cy}│ ├┬┘├─┤├─┘├┤ ├┬┘
{re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝ ╚═╝{cy}└─┘┴└─┴ ┴┴ └─┘┴└─

            versi : 1.0
        """)

cpass = configparser.RawConfigParser()
cpass.baca('config.data')

mencoba:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    telepon = cpass['cred']['telepon']
    klien = TelegramClient(telepon, api_id, api_hash)
kecuali KeyError:
    os.system('hapus')
    spanduk()
    print(re+"[!] jalankan python3 setup.py dulu!!\n")
    sys.keluar(1)

klien.sambungkan()
jika bukan client.is_user_authorized():
    client.send_code_request(telepon)
    os.system('hapus')
    spanduk()
    client.sign_in(phone, input(gr+'[+] Masukkan kode: '+re))
 
os.system('hapus')
spanduk()
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
 
obrolan = []
last_date = Tidak ada
chunk_size = 200
grup=[]
 
hasil = klien(GetDialogsRequest(
             offset_date=tanggal_terakhir,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             batas=potongan_ukuran,
             hash = 0
         ))
obrolan.memperpanjang(hasil.obrolan)
 
untuk obrolan dalam obrolan:
    mencoba:
        jika chat.megagroup== Benar:
            grup.tambahkan(obrolan)
    kecuali:
        melanjutkan
 
saya=0
untuk grup dalam grup:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+group.title)
    saya+=1

print(gr+'[+] Pilih grup untuk menambahkan anggota')
g_index = input(gr+"[+] Masukkan Angka : "+re)
target_group=grup[int(g_index)]
 
target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
 
print(gr+"[1] tambahkan anggota dengan ID pengguna\n[2] tambahkan anggota dengan nama pengguna ")
mode = int(input(gr+"Input : "+re))
n = 0
 
untuk pengguna di pengguna:
    n += 1
    jika n% 50 == 0:
	    waktu.tidur(1)
	    mencoba:
	        print ("Menambahkan {}".format(pengguna['id']))
	        jika modus == 1:
	            jika pengguna['nama pengguna'] == "":
	                melanjutkan
	            user_to_add = client.get_input_entity(pengguna['nama pengguna'])
	        modus elif == 2:
	            user_to_add = InputPeerUser(pengguna['id'], pengguna['akses_hash'])
	        kalau tidak:
	            sys.exit(re+"[!] Mode Tidak Valid Dipilih. Silakan Coba Lagi.")
	        klien(InviteToChannelRequest(target_group_entity,[user_to_add]))
	        print(gr+"[+] Menunggu 5-10 Detik...")
	        waktu.tidur(acak.rangkaian(5, 10))
	    kecuali PeerFloodError:
	        print(re+"[!] Mendapatkan Kesalahan Banjir dari telegram. \n[!] Skrip berhenti sekarang. \n[!] Silakan coba lagi setelah beberapa waktu.")
	    kecuali UserPrivacyRestrictedError:
	        print(re+"[!] Pengaturan privasi pengguna tidak mengizinkan Anda melakukan ini. Melewati.")
	    kecuali:
	        traceback.print_exc()
	        print(re+"[!] Kesalahan Tak Terduga")
	        melanjutkan
