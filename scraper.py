dari telethon.sync impor TelegramClient
dari telethon.tl.functions.messages impor GetDialogsRequest
dari telethon.tl.types mengimpor InputPeerEmpty
impor os, sys
impor configparser
impor csv
waktu impor

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def spanduk():
    cetak(f"""
{re}╔╦╗{cy}┌─┐┬ ┌─┐{re}╔═╗ ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re} ║ {cy}├┤ │ ├┤ {re}║ ╦ ╚═╗{cy}│ ├┬┘├─┤├─┘├┤ ├┬┘
{re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝ ╚═╝{cy}└─┘┴└─┴ ┴┴ └─┘┴└─

            versi : 3.1
youtube.com/channel/UCnknCgg_3pVXS27ThLpw3xQ
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
 
print(gr+'[+] Pilih grup untuk mengikis anggota :'+re)
saya=0
untuk g dalam grup:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title)
    saya+=1
 
mencetak('')
g_index = input(gr+"[+] Masukkan Angka : "+re)
target_group=grup[int(g_index)]
 
print(gr+'[+] Mengambil Anggota...')
waktu.tidur(1)
semua_peserta = []
all_participants = client.get_participants(target_group, agresif=Benar)
 
print(gr+'[+] Menyimpan Dalam file...')
waktu.tidur(1)
dengan open("members.csv","w",encoding='UTF-8') sebagai f:
    penulis = csv.penulis(f,pembatas=",",lineterminator="\n")
    writer.writerow(['username','user id', 'akses hash','name','group', 'group id'])
    untuk pengguna di all_participants:
        jika pengguna. nama pengguna:
            nama pengguna = pengguna. nama pengguna
        kalau tidak:
            nama pengguna = ""
        jika pengguna.nama_pertama:
            nama_pertama= pengguna.nama_pertama
        kalau tidak:
            nama_depan= ""
        jika pengguna.nama_belakang:
            last_name= pengguna.nama_belakang
        kalau tidak:
            nama_belakang= ""
        nama= (nama_pertama + ' ' + nama_belakang).strip()
        writer.writerow([nama pengguna,user.id,user.access_hash,nama,target_group.title, target_group.id])      
print(gr+'[+] Anggota berhasil tergores.')
