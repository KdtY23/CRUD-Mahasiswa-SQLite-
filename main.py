import sqlite3

HIJAU = "\033[92m"
MERAH = "\033[91m"
BIRU = "\033[94m"
RESET = "\033[0m"

conn = sqlite3.connect('data_mahasiswa.db')

cursor = conn.cursor()


cursor.execute(
     """
 CREATE TABLE IF NOT EXISTS data_mahasiswa (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         nama TEXT NOT NULL,
         umur INTEGER NOT NULL,
         kampus TEXT NOT NULL,
         prodi TEXT NOT NULL,
         password TEXT NOT NULL
     )
 """
 
)
def masukan_data():

 print("masukan data diri mu terlebih dahulu")
 nama = input("siapa namamu? \n")
 umur = input("berapa umur mu? \n")
 kuliah = input("kamu kuliah dimana? \n")
 prodi = input("kamu prodi mana?\n")
 password = input("silahkan masukan password \n")

 dataUser = {
    "nama_user": nama,
    "umur_user": umur,
    "nama_kampus_user": kuliah,
    "prodi_user": prodi,
    "password_user": password
 }


 try:
     cursor.execute(
          "INSERT INTO data_mahasiswa (nama, umur, kampus, prodi, password) VALUES (?, ?, ?, ?, ?)",
          (dataUser['nama_user'], dataUser['umur_user'], dataUser['nama_kampus_user'], dataUser['prodi_user'], dataUser['password_user'])
     )
     
     
     conn.commit()
     print(f"Data berhasil disimpan di database mahasiswa.")
     cursor.execute("SELECT id FROM data_mahasiswa WHERE nama = ?", (dataUser['nama_user'],))
     user_id = cursor.fetchone()[0]
     print(f"ID kamu adalah: {HIJAU}{user_id}{RESET}. Simpan ID ini untuk login di lain waktu.")
 except sqlite3.Error as e:
     print(f"Terjadi kesalahan saat menyimpan data: {e}")



def kondisi_login():
    if current_user is None:
        return False
    cursor.execute("SELECT nama FROM data_mahasiswa WHERE id = ?", (current_user['id'],))
    nama = cursor.fetchone()
    if current_user is not None and nama:
        print(f"Halo, {BIRU}{nama[0]}{RESET}!")
        return True
    return False
     


def lihat_semua_data():
 cursor.execute("SELECT * FROM data_mahasiswa")
 return cursor.fetchall()

def lihat_salah_satu_data(id):
 cursor.execute("SELECT * FROM data_mahasiswa WHERE id = ?", (id,))
 return cursor.fetchone()


def semua_data_dariID(id):
 cursor.execute("SELECT * FROM data_mahasiswa WHERE id = ?", (id,))
 data = cursor.fetchall()
 for mahasiswa in data:
     return f"""
           {HIJAU}ID: {mahasiswa[0]}{RESET}
           Nama: {mahasiswa[1]}
           Umur: {mahasiswa[2]}
           Kampus: {mahasiswa[3]}
           Prodi: {mahasiswa[4]}
           {MERAH}Password: {mahasiswa[5]}{RESET}
"""
def ubah_data(ubahData, id):
                
 cursor.execute(f"SELECT * FROM data_mahasiswa WHERE id = ?", (id,))
 mahasiswa = cursor.fetchone()
 if mahasiswa:
     if ubahData == '1':
         new_value = input("Masukkan nama baru: ")
         cursor.execute("UPDATE data_mahasiswa SET nama = ? WHERE id = ?", (new_value, id))
         print(f"Nama berhasil diperbarui menjadi {new_value}.")
     elif ubahData == '2':
         new_value = input("Masukkan umur baru: ")
         cursor.execute("UPDATE data_mahasiswa SET umur = ? WHERE id = ?", (new_value, id))
         print(f"Umur berhasil diperbarui menjadi {new_value}.")
     elif ubahData == '3':
         new_value = input("Masukkan nama kampus baru: ")
         cursor.execute("UPDATE data_mahasiswa SET kampus = ? WHERE id = ?", (new_value, id))
         print(f"Nama kampus berhasil diperbarui menjadi {new_value}.")
     elif ubahData == '4':
         new_value = input("Masukkan prodi baru: ")
         cursor.execute("UPDATE data_mahasiswa SET prodi = ? WHERE id = ?", (new_value, id))
         print(f"Prodi berhasil diperbarui menjadi {new_value}.")
     elif ubahData == '5':
         new_value = input("Masukkan password baru: ")
         cursor.execute("UPDATE data_mahasiswa SET password = ? WHERE id = ?", (new_value, id))
         print(f"Password berhasil diperbarui menjadi {new_value}.")
     else:
         print("Pilihan tidak valid.")
         return
     
     conn.commit()
     print("Data berhasil diperbarui.")
 else:
     print("ID tidak ditemukan.")

def tampilkan_menu():

     print(f"""
        ==== Database kamu ada di dalam sistem kami ===
    1. Lihat Nama
    2. Lihat Umur
    3. Lihat Nama Kampus
    4. Lihat Prodi
    5. Lihat Password
    6. Lihat Semua Data
    7. Ubah Data
    """)
     response = input("Pilih menu (1-7): ")
     if response in ['1', '2', '3', '4', '5', '6']:
      print(lihat_data(response))
     elif response == '7':
         print(f"""
        ==== Ubah Data ===
    1. Ubah Nama
    2. Ubah Umur
    3. Ubah Nama Kampus
    4. Ubah Prodi
    5. Ubah Password
               """)
         ubahData = input("Masukkan pilihan (1-5): ")
         ubah_data(ubahData, current_user['id']) 
      
current_user = None

def login():
    global current_user
    
    while True:
        user_id = input("Masukkan ID kamu: ")
        password = input("Masukkan password kamu: ")
        
        cursor.execute("SELECT id, password FROM data_mahasiswa WHERE id = ? AND password = ?", (user_id, password))
        user = cursor.fetchone()
        
        cursor.execute("SELECT nama FROM data_mahasiswa WHERE id = ?", (user_id,))
        nama_dari_id = cursor.fetchone()
        
        if user:
            print(f"Selamat datang, {nama_dari_id[0]}!")
            
            current_user = {
                "id": user[0],
                "password": user[1],
            }
            return True
        else:
            print("Nama atau password salah. Silakan coba lagi. atau buat akun baru jika belum punya akun.")
            response = input("Tekan Enter untuk mencoba lagi atau ketik 'signup' untuk membuat akun baru: ")
            if response.lower() == 'signup':
                signup()
                return False

def signup():
    masukan_data()
    print("Akun berhasil dibuat. Silakan login.")
    login()
        
def lihat_data(lihatData):
    mahasiswa = lihat_salah_satu_data(current_user['id'])
    if lihatData == '1':
        return f'nama kamu adalah {mahasiswa[1]}'
    elif lihatData == '2':
        return f'umur kamu adalah {mahasiswa[2]}'  
    elif lihatData == '3':
        return f'nama kampus kamu adalah {mahasiswa[3]}'
    elif lihatData == '4':
        return f'prodi kamu adalah {mahasiswa[4]}'
    elif lihatData == '5':
        return f'password kamu adalah {mahasiswa[5]}'
    elif lihatData == '6':
        return semua_data_dariID(current_user['id'])
    else:
        return 'input tidak valid'

def main():
    while True:
     if not kondisi_login():
        print("Kamu belum login. Silakan login terlebih dahulu.")
        login()
        tampilkan_menu()
     else:
        tampilkan_menu()

try:
    main()
except sqlite3.Error as e:
    print(f"sepertinya anda belum membuat akun, silahkan buat akun terlebih dahulu")
    signup()
            
lagi = input("Apa ada lagi yang ingin kamu lakukan? (y/n): ")

if lagi.lower() != 'y':
        print("Terima kasih telah menggunakan program ini.")
        
else:
        main()
        login()

    

            