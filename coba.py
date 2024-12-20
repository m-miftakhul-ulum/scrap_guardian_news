from dataclasses import dataclass, asdict
import dataset

# Deklarasi model menggunakan @dataclass
@dataclass
class Company:
    title: str
    url: str
    content: str

# Koneksi ke SQLite
db = dataset.connect('sqlite:///mydatabase.db')

# Tabel untuk menyimpan data Company
table = db['companies']

# Contoh data dengan @dataclass
company = Company(
    title="Miftakhul Project",
    url="https://miftakhul.com",
    content="Website tentang pemrograman dan cloud computing."
)

# Menyimpan data ke database
table.insert(asdict(company))  # Konversi dataclass ke dictionary

# Menampilkan data dari database
print("Data di tabel 'companies':")
for row in table.all():
    print(row)

# Query data berdasarkan kriteria
queried_company = table.find_one(title="Miftakhul Project")
if queried_company:
    print("\nData perusahaan yang ditemukan:")
    print(queried_company)
