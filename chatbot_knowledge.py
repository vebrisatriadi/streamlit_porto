# chatbot_knowledge.py
# File ini berfungsi sebagai "otak" atau database terpusat untuk chatbot.
# Semua informasi tentang Anda disimpan di sini dalam format yang terstruktur.

# Kita bisa mengimpor daftar skill dari config.py agar tidak duplikat (Prinsip DRY)
from config import SKILLS_DATA

# --- PROFIL DASAR ---
PROFILE_INFO = {
    "Nama Lengkap": "Vebri Satriadi",
    "Jabatan": "Data Engineer",
    "Lokasi": "Jakarta Selatan, Indonesia",
    "Fokus Saat Ini": "Mendalami MLOps dan DataOps untuk menjembatani antara data engineering dan machine learning.",
    "Bahasa": "Indonesia (Native), Inggris (Professional)"
}

# --- PENGALAMAN KERJA (Lebih terstruktur) ---
WORK_EXPERIENCE = [
    {
        "role": "Senior Data Engineer",
        "company": "Alodokter",
        "period": "Agustus 2023 - Sekarang",
        "details": [
            "Mengoptimalkan pipeline ingesti dari MongoDB ke Data Lake, berhasil mengurangi penggunaan memori 6x (3GB -> 500MB) dan waktu eksekusi 50% (9 menit -> 4.5 menit).",
            "Meningkatkan produktivitas tim hingga 40% dengan mengembangkan code generator template berbasis Jinja2.",
            "Mengoptimalkan sumber daya Kubernetes (GKE) untuk layanan Airflow, berhasil mengurangi penggunaan CPU ~50% dan memori ~30%.",
            "Membimbing dan mendelegasikan tugas kepada junior data engineer untuk meningkatkan kapabilitas tim."
        ]
    },
    {
        "role": "Data Engineer",
        "company": "Startup XYZ",
        "period": "2020 - 2023",
        "details": [
            "Membangun pipeline ETL skalabel menggunakan Apache Spark dan Airflow yang mengurangi waktu proses dari 8 jam menjadi 2 jam.",
            "Mengimplementasikan streaming data real-time dengan Apache Kafka dan Flink untuk dashboard live dan deteksi anomali.",
            "Mempelopori penggunaan Infrastructure as Code (IaC) dengan Terraform untuk mengelola resource cloud di AWS."
        ]
    }
]

CULTURE_FIT = [
    
]

# --- PENDIDIKAN & SERTIFIKASI ---
EDUCATION_CERTIFICATIONS = [
    "S1 Teknik Informatika, Universitas Indonesia (2015-2019)",
    "Google Cloud Professional Data Engineer (2023)",
    "AWS Certified Solutions Architect – Associate (2022)"
]

def get_knowledge_base_string():
    """
    Fungsi ini merakit semua informasi di atas menjadi satu string panjang
    yang terformat dengan baik untuk diberikan sebagai konteks ke LLM.
    """
    
    # Membangun bagian profil
    profile_section = "### Informasi Pribadi\n"
    for key, value in PROFILE_INFO.items():
        profile_section += f"- **{key}:** {value}\n"
    
    # Membangun bagian pengalaman kerja
    experience_section = "\n### Pengalaman Kerja\n"
    for job in WORK_EXPERIENCE:
        experience_section += f"- **{job['role']} di {job['company']}** ({job['period']})\n"
        for detail in job['details']:
            experience_section += f"  - {detail}\n"
            
    # Membangun bagian pendidikan
    education_section = "\n### Pendidikan & Sertifikasi\n"
    for item in EDUCATION_CERTIFICATIONS:
        education_section += f"- {item}\n"
        
    # Membangun bagian skill (mengambil dari SKILLS_DATA di config.py)
    skills_section = "\n### Keahlian Teknis (Tech Stack)\n"
    for category, skills in SKILLS_DATA.items():
        skills_section += f"- **{category}:** {', '.join(skills)}\n"
        
    # Gabungkan semua bagian menjadi satu string
    full_knowledge = (
        profile_section + 
        experience_section + 
        education_section + 
        skills_section
    )
    
    return full_knowledge