# 🎓 Student Database CLI

Aplikasi database mahasiswa berbasis **Python CLI** dengan penyimpanan data menggunakan **SQLite3**.

Project ini dibuat untuk mempelajari konsep dasar:
- Database integration
- CRUD (Create, Read, Update, Delete)
- User authentication
- Data management menggunakan Python

---

## 📌 Features

### 🔐 Authentication
- Register akun mahasiswa baru
- Login menggunakan ID dan password
- Sistem session user sederhana

### 📄 Data Management
- Melihat data pribadi:
  - Nama
  - Umur
  - Kampus
  - Program Studi
  - Password
- Melihat seluruh data akun sendiri
- Mengubah data mahasiswa

### 💾 Database
- Menggunakan SQLite3
- Database otomatis dibuat saat program pertama kali dijalankan

---

## 🛠️ Technologies

- Python 3
- SQLite3
- Command Line Interface (CLI)

---

## 📂 Project Structure

```
Student-Database-CLI/
│
├── main.py                 # Program utama
├── data_mahasiswa.db       # Database SQLite (dibuat otomatis)
├── README.md               # Dokumentasi project
```

---

## 🚀 How To Run

### 1. Clone repository

```bash
git clone https://github.com/username/student-database-cli.git
```

### 2. Masuk ke folder project

```bash
cd student-database-cli
```

### 3. Jalankan program

```bash
python main.py
```

---

## 🖥️ Example Flow

```
Kamu belum login. Silakan login terlebih dahulu.

1. Login
2. Signup

Masukkan data mahasiswa...

ID berhasil dibuat:
001

Login menggunakan:
ID: 001
Password: ****
```

---

## 📚 Learning Goals

Project ini dibuat sebagai latihan untuk memahami:

- Cara menghubungkan Python dengan database
- Query SQL dasar
- Penggunaan function dalam Python
- Pengelolaan data user
- Struktur program CLI

---

## ⚠️ Notes

Project ini masih berupa aplikasi pembelajaran.

Beberapa peningkatan yang dapat dilakukan:
- Password hashing
- Validasi input user
- Pemisahan file menjadi beberapa module
- Implementasi delete account
- Penggunaan environment variable

---

## 👤 Author

Adityo  
Informatics Student at Institut Teknologi Kalimantan.
