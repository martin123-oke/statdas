import streamlit as st
import pandas as pd
import random
import numpy as np
import math
import matplotlib.pyplot as plt
import altair as alt
from statistics import mean, median, multimode
import plotly.express as px
from scipy.stats import norm
from scipy import stats
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from scipy.stats import chi2_contingency, chisquare
from scipy.stats import wilcoxon, mannwhitneyu, kruskal
import seaborn as sns

st.set_page_config(page_title="Pengantar Statistika", page_icon="📊", layout="wide")

if "kondisi" not in st.session_state:
    st.session_state.kondisi = {'kondisi1':True,'kondisi2':False,'kondisi3':False, 'kondisi4':False,
                                'kondisi5':False,'kondisi6':False, 'kondisi7':False, 'kondisi8':False,
                                'kondisi9':False,'kondisi10':False, 'kondisi11':False, 'kondisi12':False,
                                'kondisi13':False,'kondisi14':False,'kondisi15':False, 'kondisi16':False,
                                'kondisi17':False,'kondisi18':False, 'kondisi19':False, 'kondisi20':False,
                                'kondisi21':False, 'kondisi22':False, 'kondisi23':False}
st.markdown('''
    <style>
        #konsep1{
            font-family:"bauhaus 93";
            font-size:15px;
            color:yellow;
            text-shadow:2px 2px 5px red, -2px -2px 5px blue;
        }
        .rumus{
            font-family:broadway;
            font-size:20px;
            color:blue;
            text-shadow:0px 0px 4px  yellow;
            border-radius:5px;
            background-color:pink;
            width:200px;
            text-align:center;
        }
        .hasil{
            font-family:"Britanic Bold";
            font-size:20px;
            color:yellow;
            text-shadow:0px 0px 4px  yellow;
            border-radius:5px;
            background-color:purple;
            width:500px;
            text-align:center;
            box-shadow:2px 2px 2px 5px red, -2ps -2px 2px 5px blue;
        }
    </style>
''',unsafe_allow_html=True)
#=======================================
def cover():
    koding='''
    <!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statistik Dasar</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .cover-container {
            width: 800px;
            height: 600px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
            border-radius: 30px;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.4);
            position: relative;
            overflow: hidden;
            animation: floatCover 6s ease-in-out infinite;
        }

        @keyframes floatCover {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        .background-shapes {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        .shape {
            position: absolute;
            opacity: 0.1;
            animation: float 20s infinite ease-in-out;
        }

        .shape.circle {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: white;
            top: -50px;
            right: -50px;
            animation: rotate 30s linear infinite;
        }

        .shape.square {
            width: 150px;
            height: 150px;
            background: white;
            bottom: 50px;
            left: -30px;
            transform: rotate(45deg);
            animation: pulse 4s ease-in-out infinite;
        }

        .shape.triangle {
            width: 0;
            height: 0;
            border-left: 100px solid transparent;
            border-right: 100px solid transparent;
            border-bottom: 180px solid white;
            top: 50%;
            right: 10%;
            animation: float 15s infinite ease-in-out;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes pulse {
            0%, 100% { transform: rotate(45deg) scale(1); }
            50% { transform: rotate(45deg) scale(1.2); }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-30px); }
        }

        .content {
            position: relative;
            z-index: 10;
            padding: 60px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .header {
            text-align: center;
        }

        .category {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            color: white;
            padding: 10px 25px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
            animation: fadeInDown 1s ease-out;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .main-title {
            margin-top: 40px;
        }

        .main-title h1 {
            font-size: 72px;
            font-weight: 900;
            color: white;
            text-align: center;
            line-height: 1.2;
            animation: fadeInUp 1s ease-out 0.3s both;
            text-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .main-title .highlight {
            background: linear-gradient(135deg, #ffd700, #ffed4e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: inline-block;
            animation: glow 2s ease-in-out infinite;
        }

        @keyframes glow {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.3); }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .stats-icons {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 30px;
            animation: fadeIn 1s ease-out 0.6s both;
        }

        .icon-item {
            text-align: center;
            color: white;
            animation: bounce 2s ease-in-out infinite;
        }

        .icon-item:nth-child(1) { animation-delay: 0s; }
        .icon-item:nth-child(2) { animation-delay: 0.2s; }
        .icon-item:nth-child(3) { animation-delay: 0.4s; }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .icon-circle {
            width: 80px;
            height: 80px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 10px;
            font-size: 32px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            transition: all 0.3s ease;
        }

        .icon-circle:hover {
            transform: scale(1.1);
            background: rgba(255, 255, 255, 0.25);
        }

        .icon-label {
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .footer {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            animation: fadeInUp 1s ease-out 0.9s both;
        }

        .author {
            color: white;
        }

        .author-label {
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 5px;
            opacity: 0.8;
        }

        .author-name {
            font-size: 24px;
            font-weight: 700;
        }

        .target-audience {
            text-align: right;
            color: white;
        }

        .target-label {
            font-size: 14px;
            font-weight: 600;
            opacity: 0.9;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            padding: 12px 24px;
            border-radius: 20px;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .particles {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        .particle {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: particleFloat 10s infinite ease-in-out;
        }

        @keyframes particleFloat {
            0%, 100% { 
                transform: translateY(0) translateX(0);
                opacity: 0;
            }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { 
                transform: translateY(-600px) translateX(50px);
                opacity: 0;
            }
        }
    </style>
</head>
<body>
    <div class="cover-container">
        <div class="background-shapes">
            <div class="shape circle"></div>
            <div class="shape square"></div>
            <div class="shape triangle"></div>
        </div>

        <div class="particles" id="particles"></div>

        <div class="content">
            <div class="header">
                <div class="category">Materi Pembelajaran</div>
            </div>

            <div class="main-title">
                <h1>
                    <span class="highlight">STATISTIK</span><br>
                    DASAR
                </h1>
                
                <div class="stats-icons">
                    <div class="icon-item">
                        <div class="icon-circle">📊</div>
                        <div class="icon-label">Data</div>
                    </div>
                    <div class="icon-item">
                        <div class="icon-circle">📈</div>
                        <div class="icon-label">Analisis</div>
                    </div>
                    <div class="icon-item">
                        <div class="icon-circle">🎯</div>
                        <div class="icon-label">Interpretasi</div>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div class="author">
                    <div class="author-label">Disusun Oleh</div>
                    <div class="author-name">Martin Bernard, M.Pd</div>
                </div>
                <div class="target-audience">
                    <div class="target-label">Untuk Mahasiswa</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const particlesContainer = document.getElementById('particles');
        
        function createParticle() {
            const particle = document.createElement('div');
            particle.classList.add('particle');
            
            const size = Math.random() * 4 + 2;
            particle.style.width = size + 'px';
            particle.style.height = size + 'px';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
            particle.style.animationDelay = Math.random() * 5 + 's';
            
            particlesContainer.appendChild(particle);
            
            setTimeout(() => {
                particle.remove();
            }, 15000);
        }
        
        setInterval(createParticle, 300);
        
        for (let i = 0; i < 20; i++) {
            setTimeout(createParticle, i * 150);
        }
    </script>
</body>
</html>
    '''
    st.components.v1.html(koding,height=650)
def materi1():
    st.title("📘 Pengantar Statistika")
    st.write("Pelajari konsep dasar statistika dan coba latihan interaktif di bawah ini!")

    # ===== Materi =====
    with st.expander("📖 Pengertian Statistika dan Statistik"):
        st.markdown("""
        **Statistika** → ilmu tentang cara mengumpulkan, mengolah, dan menganalisis data.  
        **Statistik** → hasil dari proses analisis data berupa angka atau nilai tertentu.  
        """)
        st.info("Contoh: Rata-rata nilai mahasiswa kelas A = 82 adalah sebuah **statistik**.")

    with st.expander("🎯 Fungsi dan Tujuan Statistika"):
        st.markdown("""
        - Mendeskripsikan data (deskriptif)  
        - Membuat kesimpulan dari sampel ke populasi (inferensial)  
        - Membantu pengambilan keputusan  
        - Menemukan pola atau tren
        """)
        st.success("Contoh: Universitas menggunakan data IPK untuk evaluasi kebijakan akademik.")

    with st.expander("🔢 Jenis Data: Kualitatif & Kuantitatif"):
        st.markdown("""
        | Jenis Data | Keterangan | Contoh |
        |-------------|-------------|--------|
        | **Kualitatif** | Data berbentuk kategori atau label | Jenis kelamin, jurusan |
        | **Kuantitatif** | Data berbentuk angka | Umur, nilai ujian, tinggi badan |
        """)
        st.info("Coba tentukan jenis data di bawah ini!")

    # ===== Interaktif 1: Jenis Data =====
    st.subheader("🧩 Aktivitas 1: Tentukan Jenis Data")

    contoh_data = ["Nilai ujian mahasiswa", "Jurusan kuliah", "Tinggi badan", "Tingkat kepuasan dosen"]
    for data in contoh_data:
        jawaban = st.radio(f"Data: {data}", ["","Kualitatif", "Kuantitatif"], key=data,index=0)
        if data in ["Nilai ujian mahasiswa", "Tinggi badan"]:
            benar = "Kuantitatif"
        else:
            benar = "Kualitatif"

        if jawaban == benar:
            st.success("✅ Benar!")
        else:
            st.warning("❌ Coba lagi!")

    # ===== Interaktif 2: Skala Pengukuran =====
    st.subheader("🧩 Aktivitas 2: Tentukan Skala Pengukuran")

    soal_skala = {
        "Jenis kelamin": "Nominal",
        "Tingkat kepuasan": "Ordinal",
        "Suhu ruangan (°C)": "Interval",
        "Berat badan (kg)": "Rasio"
    }

    for pertanyaan, jawaban_benar in soal_skala.items():
        pilihan = st.selectbox(f"Data: {pertanyaan}", ["Nominal", "Ordinal", "Interval", "Rasio"], key=pertanyaan)
        if pilihan == jawaban_benar:
            st.success("✅ Tepat sekali!")
        else:
            st.warning("❌ Belum tepat.")

    # ===== Interaktif 3: Populasi & Sampel =====
    st.subheader("🧩 Aktivitas 3: Populasi dan Sampel")

    st.markdown("""
        **Kasus:**  
    Seorang dosen ingin mengetahui rata-rata nilai UAS mahasiswa di universitasnya.  
    Ia mengambil **100 mahasiswa dari 1000 mahasiswa** yang ada.
    """)

    pilih = st.radio("Yang termasuk *sampel* adalah...", 
                     ["100 mahasiswa yang diambil", "Seluruh 1000 mahasiswa", "Nilai UAS"], key="sampel")

    if pilih == "100 mahasiswa yang diambil":
        st.success("✅ Benar! Sampel adalah sebagian dari populasi.")
    else:
        st.warning("❌ Coba pikirkan kembali.")

    # ===== Kesimpulan =====
    st.subheader("📊 Kesimpulan")
    st.write("""
    Statistika membantu kita memahami data untuk pengambilan keputusan.  
    Data bisa bersifat **kualitatif atau kuantitatif**, dan memiliki **skala pengukuran** yang berbeda.  
    Dalam penelitian, penting membedakan antara **populasi, sampel, parameter, dan statistik**.
    """)

    st.balloons()

def materi2():
    st.title("📘 Pengumpulan Data - Statistika Dasar")
    st.write("Pelajari berbagai metode dan coba simulasi pengumpulan data sederhana!")

    # ======== Bagian Materi ========
    with st.expander("📖 Metode Pengumpulan Data"):
        st.markdown("""
        | Metode | Penjelasan | Contoh |
        |--------|-------------|--------|
        | **Observasi** | Mengamati langsung objek penelitian | Mengamati kehadiran mahasiswa di kelas |
        | **Wawancara** | Tanya jawab langsung dengan responden | Menanyakan kebiasaan belajar mahasiswa |
        | **Kuesioner** | Daftar pertanyaan tertulis | Form survei Google tentang waktu belajar |
        | **Eksperimen** | Memberi perlakuan tertentu untuk melihat pengaruh | Mencoba metode belajar baru lalu membandingkan hasilnya |
        """)

    with st.expander("📚 Sumber Data"):
        st.markdown("""
        | Jenis Sumber | Penjelasan | Contoh |
        |---------------|-------------|---------|
        | **Data Primer** | Diperoleh langsung dari sumber pertama | Survei mahasiswa di kelas |
        | **Data Sekunder** | Sudah dikumpulkan pihak lain | Data IPK dari biro akademik |
        """)

    with st.expander("🎯 Teknik Sampling"):
        st.markdown("""
        | Teknik Sampling | Penjelasan Singkat | Contoh |
        |-----------------|-------------------|--------|
        | **Acak Sederhana** | Semua anggota punya peluang sama | Undian nama mahasiswa |
        | **Berstrata** | Populasi dibagi strata (misal jurusan) | Tiap jurusan diambil 5 mahasiswa |
        | **Berkelompok** | Populasi dibagi kelompok, kelompok dipilih acak | Pilih 2 kelas dari 10 kelas |
        | **Sistematik** | Ambil setiap elemen ke-n dari daftar | Pilih setiap mahasiswa ke-5 dari daftar hadir |
        """)

    with st.expander("⚠️ Kesalahan dalam Pengambilan Sampel"):
        st.markdown("""
        - **Sampling Error:** ukuran sampel terlalu kecil atau tidak representatif  
        - **Non-Sampling Error:** kesalahan pencatatan atau responden tidak jujur  
        - **Bias Peneliti:** peneliti tidak netral dalam memilih sampel  
        """)

    st.markdown("---")

    # ======== Aktivitas Interaktif ========
    st.subheader("🧩 Aktivitas: Simulasi Pengumpulan Data di Kelas")

    st.write("Mari lakukan simulasi survei sederhana tentang **kebiasaan belajar mahasiswa** 👇")

    # Input jumlah mahasiswa
    jumlah = st.slider("Jumlah mahasiswa yang disurvei:", 5, 30, 10)

    # Input metode sampling
    metode = st.selectbox("Pilih teknik sampling yang digunakan:", 
                      ["", "Acak Sederhana", "Berstrata", "Berkelompok", "Sistematik"])

    # Simulasi nama dan kebiasaan belajar
    nama_mahasiswa = [f"Mahasiswa-{i+1}" for i in range(30)]
    kebiasaan = ["Belajar malam", "Belajar pagi", "Belajar kelompok", "Belajar sendiri"]

    if metode:
        if metode == "Acak Sederhana":
            sampel = random.sample(nama_mahasiswa, jumlah)
        elif metode == "Sistematik":
            interval = max(1, len(nama_mahasiswa)//jumlah)
            sampel = nama_mahasiswa[::interval][:jumlah]
        elif metode == "Berstrata":
            # Asumsi 3 jurusan
            jurusan = ["Matematika", "Fisika", "Kimia"]
            sampel = [f"{random.choice(jurusan)}-{i+1}" for i in range(jumlah)]
        elif metode == "Berkelompok":
            kelompok = random.choice(["Kelas A", "Kelas B", "Kelas C"])
            sampel = [f"{kelompok} - {i+1}" for i in range(jumlah)]
        else:
            sampel = random.sample(nama_mahasiswa, jumlah)

        data = pd.DataFrame({
            "Nama": sampel,
            "Kebiasaan Belajar": [random.choice(kebiasaan) for _ in sampel]
        })

        st.dataframe(data, use_container_width=True)
        st.success(f"Data berhasil dikumpulkan menggunakan metode: **{metode}**")

        st.download_button(
            label="💾 Unduh Data Survei (CSV)",
            data=data.to_csv(index=False).encode('utf-8'),
            file_name="data_survei.csv",
            mime="text/csv"
        )

    st.markdown("---")

    # ======== Kuis Ringan ========
    st.subheader("🧠 Kuis Cepat")

    pertanyaan = st.radio(
        "Metode apa yang digunakan jika peneliti membagi populasi menjadi jurusan lalu mengambil sampel dari tiap jurusan?",
        ["", "Acak Sederhana", "Berstrata", "Berkelompok", "Sistematik"]
    )

    if pertanyaan == "Berstrata":
        st.success("✅ Benar! Itu adalah metode sampling berstrata.")
    elif pertanyaan != "":
        st.warning("❌ Belum tepat, coba lagi!")

    st.balloons()

def materi3():
    st.title("📊 Tabel Distribusi Frekuensi Interaktif")
    st.markdown("Belajar membuat tabel distribusi frekuensi **data tunggal** dan **data berkelompok** secara interaktif.")

    # Input data
    data_input = st.text_area("Masukkan data (pisahkan dengan koma):", "12, 15, 13, 15, 17, 20, 21, 19, 15, 14, 20, 18, 19, 17, 16")
    data = sorted([int(i.strip()) for i in data_input.split(",") if i.strip().isdigit()])

    if len(data) > 0:
        st.subheader("📋 Data Tersusun")
        st.write(str(data))
        n = len(data)
        st.write(f"Jumlah data: **{n}**")

        tab1, tab2 = st.tabs(["Data Tunggal", "Data Berkelompok"])

        # ------------------------------
        # TAB 1: DATA TUNGGAL
        # ------------------------------
        with tab1:
            st.subheader("📘 Distribusi Frekuensi Data Tunggal")

            freq_table = pd.Series(data).value_counts().sort_index().reset_index()
            freq_table.columns = ["Nilai", "Frekuensi"]
            freq_table["Frekuensi Kumulatif"] = freq_table["Frekuensi"].cumsum()
            st.table(freq_table)

            st.subheader("📈 Histogram Data Tunggal")
            fig, ax = plt.subplots()
            ax.hist(data, bins=len(freq_table), edgecolor='black')
            ax.set_xlabel("Nilai")
            ax.set_ylabel("Frekuensi")
            st.pyplot(fig)

        # ------------------------------
        # TAB 2: DATA BERKELOMPOK
        # ------------------------------
        with tab2:
            st.subheader("📗 Distribusi Frekuensi Data Berkelompok")

            # Hitung parameter dasar
            st.markdown("<div class='rumus'>Jangkauan(R)</div>",unsafe_allow_html=True)
            st.latex("R=x_{max}-x_{min}")
            xmin, xmax = min(data), max(data)
            R = xmax - xmin
            k = round(1 + 3.3 * math.log10(n))
            c = math.ceil(R / k)

            st.markdown(f"<div class='hasil'>Range (R) = {R}</div>",unsafe_allow_html=True)
            st.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
            st.markdown("<div class='rumus'>Banyak Kelas(k)</div>",unsafe_allow_html=True)
            st.latex("k=1+3.3\\times{\\log{n}}")
            st.markdown(f"<div class='hasil'>Banyak kelas (k) ≈ {k}</div>",unsafe_allow_html=True)
            st.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
            st.markdown("<div class='rumus'>Interval (c)</div>",unsafe_allow_html=True)
            st.latex("c=\\frac{R}{k}")
            st.markdown(f"<div class='hasil'>Interval (c) ≈ {c}</div>",unsafe_allow_html=True)
            st.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)

            # Buat interval
            batas_bawah = xmin
            interval = []
            freq = []

            for i in range(k):
                batas_atas = batas_bawah + c - 1
                count = sum((x >= batas_bawah) & (x <= batas_atas) for x in data)
                interval.append(f"{batas_bawah} - {batas_atas}")
                freq.append(count)
                batas_bawah = batas_atas + 1

            df = pd.DataFrame({
                "Kelas": interval,
                "Frekuensi": freq,
                "Frekuensi Kumulatif": np.cumsum(freq)
            })
            df["Titik Tengah"] = df["Kelas"].apply(lambda x: np.mean([int(i) for i in x.split(" - ")]))
            st.table(df)

            st.subheader("📊 Histogram Data Berkelompok")
            fig2, ax2 = plt.subplots()
            ax2.bar(df["Titik Tengah"], df["Frekuensi"], width=c-0.5, edgecolor='black')
            ax2.set_xlabel("Titik Tengah")
            ax2.set_ylabel("Frekuensi")
            st.pyplot(fig2)

    # ------------------------------
    # LATIHAN INTERAKTIF
    # ------------------------------
    st.markdown("---")
    st.header("🧠 Latihan Interaktif")

    with st.expander("💡 Soal 1: Data Tunggal"):
        st.write("Diketahui data nilai siswa: 10, 12, 13, 12, 11, 13, 14, 12, 10, 13")
        jawaban = st.number_input("Berapa frekuensi dari nilai 12?", min_value=0)
        if st.button("Cek Jawaban Soal 1"):
            if jawaban == 3:
                st.success("✅ Benar! Nilai 12 muncul sebanyak 3 kali.")
            else:
                st.error("❌ Belum tepat, coba hitung ulang ya!")

    with st.expander("💡 Soal 2: Data Berkelompok"):
        st.write("Jika data memiliki nilai minimum 20 dan maksimum 68, tentukan range (R).")
        jawaban2 = st.number_input("Masukkan nilai Range (R):", min_value=0)
        if st.button("Cek Jawaban Soal 2"):
            if jawaban2 == 48:
                st.success("✅ Benar! R = 68 - 20 = 48.")
            else:
                st.error("❌ Coba lagi, gunakan rumus R = Xmax - Xmin.")

    st.info("💬 Cobalah ganti data di atas untuk melihat perubahan tabel distribusi frekuensi dan histogram.")

def materi4():
    # =========================
    # 🎯 Judul dan Deskripsi
    # =========================
    st.title("📊 Materi Interaktif: Batas Kelas, Titik Tengah, & Frekuensi Kumulatif")

    st.markdown("""
    Garis besar materi ini:
    - **Batas Kelas** → Nilai batas bawah dan batas atas setiap kelas interval  
    - **Titik Tengah (Class Mark)** → Nilai rata-rata antara batas bawah dan batas atas  
    - **Frekuensi Kumulatif** → Jumlah frekuensi yang dijumlahkan secara bertahap
    """)

    st.markdown("<hr style='border: 2px solid #00BFFF; border-radius: 5px;'>", unsafe_allow_html=True)

    # =========================
    # 📘 Input Data Kelas
    # =========================
    st.subheader("🔹 Input Data Distribusi Frekuensi")

    st.write("Masukkan data kelas interval dan frekuensinya:")

    # Input jumlah kelas
    jumlah_kelas = st.number_input("Jumlah Kelas Interval:", min_value=2, max_value=10, value=5)

    # Buat input dinamis
    kelas_data = []
    for i in range(int(jumlah_kelas)):
        col1, col2, col3 = st.columns(3)
        with col1:
            bawah = st.number_input(f"Batas Bawah Kelas {i+1}", key=f"bawah_{i}")
        with col2:
            atas = st.number_input(f"Batas Atas Kelas {i+1}", key=f"atas_{i}")
        with col3:
            frek = st.number_input(f"Frekuensi {i+1}", min_value=0, key=f"frek_{i}")
            kelas_data.append((bawah, atas, frek))

    # Buat DataFrame
    df = pd.DataFrame(kelas_data, columns=["Batas Bawah", "Batas Atas", "Frekuensi"])

    # =========================
    # 📊 Perhitungan
    # =========================
    df["Titik Tengah"] = (df["Batas Bawah"] + df["Batas Atas"]) / 2
    df["Batas Bawah Nyata"] = df["Batas Bawah"] - 0.5
    df["Batas Atas Nyata"] = df["Batas Atas"] + 0.5
    df["Frekuensi Kumulatif"] = df["Frekuensi"].cumsum()

    # =========================
    # 📋 Tampilkan Hasil
    # =========================
    st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)
    st.subheader("📋 Tabel Distribusi Lengkap")

    st.dataframe(df, use_container_width=True)

    # =========================
    # 📈 Visualisasi
    # =========================
    st.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
    st.subheader("📈 Visualisasi Frekuensi Kumulatif")

    chart = alt.Chart(df).mark_line(point=True, color="#FF5733").encode(
        x=alt.X("Batas Atas Nyata", title="Batas Atas Nyata"),
        y=alt.Y("Frekuensi Kumulatif", title="Frekuensi Kumulatif"),
        tooltip=["Batas Atas Nyata", "Frekuensi Kumulatif"]
    ).properties(
        width=600, height=400, title="Grafik Frekuensi Kumulatif"
    )

    st.altair_chart(chart, use_container_width=True)

    # =========================
    # 🧩 Aktivitas Interaktif
    # =========================
    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)
    st.subheader("🧩 Aktivitas Mahasiswa")

    st.markdown("""
    **Tugas Interaktif:**
    1. Buat tabel distribusi frekuensi dengan 5 kelas dari data tinggi badan teman sekelas.  
    2. Tentukan:
       - Batas kelas setiap interval  
       - Titik tengah  
       - Frekuensi kumulatif  
    3. Masukkan hasil ke tabel di atas dan amati perubahan grafik.  
    """)

    # Pertanyaan reflektif
    jawaban = st.text_area("Apa hubungan antara batas kelas dan titik tengah menurutmu?")
    if st.button("Kirim Jawaban"):
        st.success("Terima kasih! Jawabanmu tersimpan untuk diskusi kelas. 😊")

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)
    st.caption("💡 Tips: Gunakan contoh data seperti tinggi badan (cm), nilai ujian, atau waktu belajar per minggu.")

def materi5():
    # ==============================
    # 🎓 HEADER APLIKASI
    # ==============================
    st.title("📊 Materi & Latihan: Diagram Batang, Lingkaran, Histogram, Poligon, dan Ogive")

    st.markdown("""
    Aplikasi ini membantu memahami berbagai **diagram penyajian data statistik** secara interaktif.

    ### 🔍 Materi Singkat
    - **Diagram Batang (Bar Chart)** → membandingkan frekuensi tiap kategori  
    - **Diagram Lingkaran (Pie Chart)** → menunjukkan proporsi dari keseluruhan  
    - **Histogram** → menyajikan distribusi data berkelompok  
    - **Poligon Frekuensi** → menghubungkan titik tengah kelas interval  
    - **Ogive (Frekuensi Kumulatif)** → menggambarkan pertambahan frekuensi secara bertahap  
    """)

    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)

    # ==============================
    # 📥 INPUT DATA
    # ==============================
    st.subheader("🔹 Input Data")

    with st.expander("Masukkan Data Kategori atau Kelas"):
        jenis_data = st.radio("Pilih jenis data yang akan divisualisasikan:", 
                          ["Data Kategori (untuk batang & lingkaran)", "Data Numerik (untuk histogram & poligon)"])

    # ==============================
    # 🧮 INPUT DATA KATEGORI
    # ==============================
    if jenis_data == "Data Kategori (untuk batang & lingkaran)":
        st.write("Masukkan kategori dan frekuensinya:")
        n = st.number_input("Jumlah kategori:", min_value=2, max_value=10, value=4)

        kategori, frekuensi = [], []
        for i in range(n):
            col1, col2 = st.columns(2)
            with col1:
                k = st.text_input(f"Nama kategori {i+1}", key=f"k{i}")
            with col2:
                f = st.number_input(f"Frekuensi {i+1}", min_value=0, key=f"f{i}")
            kategori.append(k)
            frekuensi.append(f)

        df = pd.DataFrame({"Kategori": kategori, "Frekuensi": frekuensi})
        df = df[df["Kategori"] != ""]

        st.markdown("### 📋 Data Kategori")
        st.dataframe(df, use_container_width=True)

        if not df.empty:
            tab1, tab2 = st.tabs(["📊 Diagram Batang", "🟢 Diagram Lingkaran"])
            with tab1:
                chart = alt.Chart(df).mark_bar(color="#1E90FF").encode(
                    x=alt.X("Kategori", sort=None),
                    y="Frekuensi",
                    tooltip=["Kategori", "Frekuensi"]
                ).properties(title="Diagram Batang")
                st.altair_chart(chart, use_container_width=True)

            with tab2:
                st.write("Proporsi (%) tiap kategori:")
                df["Persentase"] = (df["Frekuensi"] / df["Frekuensi"].sum()) * 100
                pie = alt.Chart(df).mark_arc(innerRadius=0).encode(
                    theta="Frekuensi",
                    color="Kategori",
                    tooltip=["Kategori", "Persentase"]
                ).properties(title="Diagram Lingkaran")
                st.altair_chart(pie, use_container_width=True)

    # ==============================
    # 📈 INPUT DATA NUMERIK
    # ==============================
    else:
        st.write("Masukkan data numerik untuk histogram, poligon, dan ogive:")
        data_str = st.text_area("Masukkan data (pisahkan dengan koma):", "60,65,70,72,75,77,78,80,82,85,88,90,91,95,97")
    
        if data_str:
            try:
                data = [float(x.strip()) for x in data_str.split(",")]
                df_num = pd.DataFrame({"Data": data})
                st.dataframe(df_num.describe(), use_container_width=True)
            
                # Pilih jumlah kelas
                k = st.slider("Jumlah kelas (interval):", 3, 10, 5)
            
                # Buat histogram data berkelompok
                hist_data, bins = np.histogram(data, bins=k)
                kelas_bawah = bins[:-1]
                kelas_atas = bins[1:]
                titik_tengah = (kelas_bawah + kelas_atas) / 2
                frek_kum = np.cumsum(hist_data)
            
                df_hist = pd.DataFrame({
                    "Kelas Bawah": kelas_bawah,
                    "Kelas Atas": kelas_atas,
                    "Titik Tengah": titik_tengah,
                    "Frekuensi": hist_data,
                    "Frekuensi Kumulatif": frek_kum
                })

                st.markdown("### 📋 Tabel Distribusi Data Berkelompok")
                st.dataframe(df_hist, use_container_width=True)

                tab1, tab2, tab3, tab4 = st.tabs(["📊 Histogram", "📈 Poligon", "📈 Ogive", "📚 Gabungan"])

                with tab1:
                    chart = alt.Chart(df_hist).mark_bar(color="#FFA500").encode(
                        x=alt.X("Kelas Bawah:Q", bin="binned", title="Kelas Interval"),
                        x2="Kelas Atas:Q",
                        y="Frekuensi:Q",
                        tooltip=["Kelas Bawah", "Kelas Atas", "Frekuensi"]
                    ).properties(title="Histogram Data")
                    st.altair_chart(chart, use_container_width=True)

                with tab2:
                    poly = alt.Chart(df_hist).mark_line(point=True, color="#008000").encode(
                        x="Titik Tengah",
                        y="Frekuensi",
                        tooltip=["Titik Tengah", "Frekuensi"]
                    ).properties(title="Poligon Frekuensi")
                    st.altair_chart(poly, use_container_width=True)

                with tab3:
                    ogive = alt.Chart(df_hist).mark_line(point=True, color="#FF5733").encode(
                        x="Kelas Atas",
                        y="Frekuensi Kumulatif",
                        tooltip=["Kelas Atas", "Frekuensi Kumulatif"]
                    ).properties(title="Ogive (Frekuensi Kumulatif)")
                    st.altair_chart(ogive, use_container_width=True)

                with tab4:
                    st.write("Gabungan Poligon dan Ogive:")
                    combined = alt.Chart(df_hist).mark_line(point=True).encode(
                        x="Titik Tengah",
                        y="Frekuensi",
                        color=alt.value("#008000")
                    ) + alt.Chart(df_hist).mark_line(point=True).encode(
                        x="Kelas Atas",
                        y="Frekuensi Kumulatif",
                        color=alt.value("#FF5733")
                    )
                    st.altair_chart(combined, use_container_width=True)
            except:
                st.error("⚠️ Pastikan data berupa angka yang dipisahkan koma.")

    # ==============================
    # 🧩 AKTIVITAS MAHASISWA
    # ==============================
    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)
    st.subheader("🧩 Aktivitas dan Latihan")

    st.markdown("""
    ### 📌 Tugas Interaktif:
    1. Buatlah data hasil nilai ujian kelas Anda.  
    2. Tampilkan:
       - Diagram batang (kategori: nilai A, B, C, D, E)
       - Histogram dan poligon dari data numerik nilai.  
    3. Bandingkan bentuk histogram dan ogive — apakah distribusinya simetris atau condong?

    💬 Tuliskan hasil pengamatanmu di bawah ini:
    """)

    jawaban = st.text_area("🖋️ Hasil pengamatan:")
    if st.button("Kirim Jawaban"):
        st.success("Terima kasih! Jawabanmu tersimpan untuk evaluasi kelas. 😊")

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)
    st.caption("💡 Gunakan data nyata agar hasil visualisasi lebih bermakna.")

def materi6():
    # ==============================
    # 🎓 HEADER APLIKASI
    # ==============================
    st.title("📊 Materi & Latihan: Ukuran Pemusatan Data (Tendensi Sentral)")

    st.markdown("""
    Aplikasi interaktif ini membantu memahami **ukuran pemusatan data** seperti:
    - **Mean (rata-rata)**  
    - **Median (nilai tengah)**  
    - **Modus (nilai yang paling sering muncul)**  
    - **Rata-rata gabungan**  
    """)

    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)

    # ==============================
    # 📚 MENU MATERI
    # ==============================
    menu = st.radio("Pilih materi yang ingin dipelajari:", [
        "1️⃣ Mean, Median, dan Modus",
        "2️⃣ Rata-rata Gabungan",
        "3️⃣ Aplikasi pada Data Tunggal dan Berkelompok"
    ], horizontal=True)

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)

    # ==============================
    # 1️⃣ Mean, Median, Modus
    # ==============================
    if menu == "1️⃣ Mean, Median, dan Modus":
        st.subheader("📘 Materi 1: Mean, Median, dan Modus")

        st.markdown("""
        - **Mean (Rata-rata):**  
          $$ \\bar{x} = \\frac{\\sum x_i}{n} $$

        - **Median:**  
          Nilai yang berada di tengah setelah data diurutkan.

        - **Modus:**  
          Nilai yang paling sering muncul dalam data.
        """)

        st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)

        st.subheader("🧩 Latihan Data Tunggal")

        data_str = st.text_area("Masukkan data nilai mahasiswa (pisahkan dengan koma):", "70,75,80,80,85,90,95,95,100")
        if data_str:
            try:
                data = [float(x.strip()) for x in data_str.split(",")]
                data_sorted = sorted(data)
                df = pd.DataFrame({"Data": data_sorted})
                st.write("📋 Data Terurut:")
                st.dataframe(df, use_container_width=True)

                # Hitung ukuran pemusatan
                mean_val = mean(data)
                median_val = median(data)
                mode_val = multimode(data)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Mean", round(mean_val, 2))
                with col2:
                    st.metric("Median", round(median_val, 2))
                with col3:
                    st.metric("Modus", ", ".join(map(str, mode_val)))

                st.success("✅ Hasil dihitung otomatis dari data yang kamu masukkan.")
            except:
                st.error("⚠️ Pastikan format data benar, misalnya: 70, 75, 80, 90")

    # ==============================
    # 2️⃣ Rata-rata Gabungan
    # ==============================
    elif menu == "2️⃣ Rata-rata Gabungan":
        st.subheader("📘 Materi 2: Rata-rata Gabungan")

        st.markdown("""
        Rata-rata gabungan digunakan jika terdapat **dua atau lebih kelompok data** dengan rata-rata dan jumlah data berbeda.  
        Rumus:
        $$
        \\bar{X} = \\frac{n_1 \\bar{X}_1 + n_2 \\bar{X}_2 + \\dots + n_k \\bar{X}_k}{n_1 + n_2 + \\dots + n_k}
        $$
        """)

        st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)

        st.subheader("🧩 Latihan Rata-rata Gabungan")

        jml_kelompok = st.number_input("Jumlah kelompok data:", 2, 5, 2)
        kelompok = []

        for i in range(int(jml_kelompok)):
            col1, col2 = st.columns(2)
            with col1:
                n = st.number_input(f"Jumlah data kelompok {i+1} (n{i+1})", min_value=1, key=f"n{i}")
            with col2:
                x = st.number_input(f"Rata-rata kelompok {i+1} (X̄{i+1})", key=f"x{i}")
            kelompok.append((n, x))

        if st.button("Hitung Rata-rata Gabungan"):
            total_nx = sum([n * x for n, x in kelompok])
            total_n = sum([n for n, x in kelompok])
            rata_gab = total_nx / total_n if total_n > 0 else 0

            st.success(f"📊 Rata-rata Gabungan = {round(rata_gab, 2)}")

    # ==============================
    # 3️⃣ Aplikasi pada Data Berkelompok
    # ==============================
    elif menu == "3️⃣ Aplikasi pada Data Tunggal dan Berkelompok":
        st.subheader("📘 Materi 3: Aplikasi Data Berkelompok")

        st.markdown("""
        Untuk **data berkelompok**, mean dihitung dengan:
        $$
        \\bar{X} = \\frac{\\sum f_i x_i}{\\sum f_i}
        $$

        di mana:
        - $ f_i $ = frekuensi kelas  
        - $ x_i $ = titik tengah kelas
        """)

        st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)

        st.subheader("🧩 Latihan Interaktif")

        jml_kelas = st.number_input("Jumlah kelas interval:", 2, 10, 5)
        data_kelas = []

        for i in range(int(jml_kelas)):
            col1, col2, col3 = st.columns(3)
            with col1:
                bawah = st.number_input(f"Batas bawah kelas {i+1}", key=f"bawah{i}")
            with col2:
                atas = st.number_input(f"Batas atas kelas {i+1}", key=f"atas{i}")
            with col3:
                f = st.number_input(f"Frekuensi {i+1}", min_value=0, key=f"f{i}")
            data_kelas.append((bawah, atas, f))

        df = pd.DataFrame(data_kelas, columns=["Batas Bawah", "Batas Atas", "Frekuensi"])
        df["Titik Tengah"] = (df["Batas Bawah"] + df["Batas Atas"]) / 2
        df["f.x"] = df["Frekuensi"] * df["Titik Tengah"]

        if st.button("Hitung Ukuran Pemusatan"):
            total_fx = df["f.x"].sum()
            total_f = df["Frekuensi"].sum()
            mean_group = total_fx / total_f if total_f > 0 else 0

            st.markdown("### 📋 Tabel Distribusi Frekuensi")
            st.dataframe(df, use_container_width=True)

            st.metric("Mean (Data Berkelompok)", round(mean_group, 2))
            st.info("📌 Median & modus data berkelompok bisa dihitung dari tabel dengan rumus khusus (materi lanjutan).")

    # ==============================
    # 🧩 REFLEKSI MAHASISWA
    # ==============================
    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)
    st.subheader("🧩 Refleksi & Latihan")

    st.markdown("""
    **Latihan Akhir:**
    Hitung mean, median, dan modus dari data nilai mahasiswa berikut:
    70, 75, 80, 85, 90, 90, 95, 100
    """)

    jawaban = st.text_area("Tuliskan langkah dan hasil perhitunganmu:")
    if st.button("Kirim Jawabannya"):
        st.success("Terima kasih! Jawabanmu tersimpan untuk evaluasi kelas. 😊")

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)
    st.caption("💡 Gunakan aplikasi ini untuk bereksperimen dengan berbagai jenis data.")

def materi7():
    # =========================
    # 🎓 JUDUL DAN PENJELASAN
    # =========================
    st.title("📘 Materi Interaktif: Ukuran Letak Data (Kuartil, Desil, Persentil)")

    st.markdown("""
    ### 🎯 Tujuan Pembelajaran
    Mahasiswa dapat:
    1. Memahami konsep **kuartil, desil, dan persentil**  
    2. Menentukan **posisi data** dari suatu distribusi  
    3. Menerapkan perhitungan **Q3 (Kuartil ke-3)** secara langsung
    """)

    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)

    # =========================
    # 📚 PENJELASAN KONSEP
    # =========================
    st.subheader("📖 1. Konsep Dasar Ukuran Letak")
    st.markdown("""
    - **Kuartil (Q)** membagi data menjadi **empat bagian yang sama besar**:
      - Q1 = 25% data
      - Q2 = 50% data (sama dengan median)
      - Q3 = 75% data

    - **Desil (D)** membagi data menjadi **10 bagian**.  
      Contoh: D3 = data pada posisi ke-30%.

    - **Persentil (P)** membagi data menjadi **100 bagian**.  
      Contoh: P70 = data pada posisi ke-70%.
    """)

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)

    # =========================
    # 🧮 INPUT DATA
    # =========================
    st.subheader("📊 2. Input Data Nilai Mahasiswa")

    data_input = st.text_area(
        "Masukkan data nilai mahasiswa (pisahkan dengan koma):",
        "60,70,80,75,85,90,95,100,65,70,80,85,90"
    )

    try:
        data = sorted([float(x.strip()) for x in data_input.split(",") if x.strip() != ""])
        n = len(data)
        df = pd.DataFrame({"Data": data},index=[1,2,3,4,5,6,7,8,9,10,11,12,13])
        st.dataframe(df, use_container_width=True)

        # =========================
        # 📈 PEMUSATAN & POSISI DATA
        # =========================
        st.subheader("📌 3. Posisi Data dan Nilai Ukuran Letak")

        k_pilihan = st.radio("Pilih ukuran letak yang ingin dihitung:", ["Kuartil", "Desil", "Persentil"])
        if k_pilihan == "Kuartil":
            k = st.slider("Pilih Kuartil (Q1-Q3):", 1, 3, 3)
            posisi = k * (n + 1) / 4
            tipe = "Kuartil"
        elif k_pilihan == "Desil":
            k = st.slider("Pilih Desil (D1-D9):", 1, 9, 5)
            posisi = k * (n + 1) / 10
            tipe = "Desil"
        else:
            k = st.slider("Pilih Persentil (P1-P99):", 1, 99, 70)
            posisi = k * (n + 1) / 100
            tipe = "Persentil"

        # =========================
        # 🔢 PERHITUNGAN INTERPOLASI
        # =========================
        if n > 0:
            posisi_bulat = int(np.floor(posisi))
            posisi_desimal = posisi - posisi_bulat

            if posisi_bulat == 0:
                nilai = data[0]
            elif posisi_bulat >= n:
                nilai = data[-1]
            else:
                nilai = data[posisi_bulat - 1] + posisi_desimal * (data[posisi_bulat] - data[posisi_bulat - 1])

            st.success(f"{tipe} ke-{k} berada pada posisi ke-{posisi:.2f} dengan nilai sekitar **{nilai:.2f}**")

            # =========================
            # 📉 Visualisasi
            # =========================
            df["Urutan"] = range(1, n+1)
            chart = alt.Chart(df).mark_circle(size=80, color="#FF6B6B").encode(
                x=alt.X("Urutan", title="Posisi Data"),
                y=alt.Y("Data", title="Nilai"),
                tooltip=["Urutan", "Data"]
            ).properties(
                title=f"Distribusi Nilai Mahasiswa dan {tipe} ke-{k}",
                width=600, height=400
            )

            garis = alt.Chart(pd.DataFrame({'y': [nilai]})).mark_rule(color='green', strokeDash=[5,5]).encode(y='y')
            st.altair_chart(chart + garis, use_container_width=True)

    except Exception as e:
        st.warning("⚠️ Masukkan data numerik yang benar, pisahkan dengan koma.")

    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)

    # =========================
    # 🧩 LATIHAN MAHASISWA
    # =========================
    st.subheader("🧩 Latihan Mahasiswa")

    st.markdown("""
    **Tugas:**
    1. Gunakan data nilai ujian mahasiswa di kelasmu (minimal 10 data).  
    2. Hitung **kuartil ke-3 (Q3)** secara manual.  
    3. Bandingkan hasil manualmu dengan hasil perhitungan otomatis di atas.  
    4. Tuliskan langkah-langkah dan kesimpulanmu di bawah ini.
    """)

    jawaban = st.text_area("💬 Jawaban Mahasiswa:")
    if st.button("Kirim Jawaban"):
        st.success("Terima kasih! Jawabanmu tersimpan untuk evaluasi dosen. ✅")

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)
    st.caption("💡 Tips: Data sebaiknya diurutkan dari kecil ke besar sebelum menghitung ukuran letak.")
def materi8():
    # ===========================================
    # 🎓 JUDUL DAN PENJELASAN
    # ===========================================
    st.title("📘 Materi Interaktif: Ukuran Penyebaran Data")

    st.markdown("""
    ### 📖 Materi Pembelajaran
    Ukuran penyebaran data menunjukkan **seberapa jauh nilai-nilai data tersebar dari nilai rata-ratanya**.

    #### 1️⃣ Rentang (Range)
    $$ R = X_{maks} - X_{min} $$

    #### 2️⃣ Simpangan Rata-rata
    $$ SR = \\frac{\\sum |X_i - \\bar{X}|}{n} $$

    #### 3️⃣ Varians
    $$ S^2 = \\frac{\\sum (X_i - \\bar{X})^2}{n} $$

    #### 4️⃣ Standar Deviasi
    $$ S = \\sqrt{S^2} $$

    #### 5️⃣ Koefisien Variasi (CV)
    $$ CV = \\frac{S}{\\bar{X}} \\times 100\\% $$

    > Semakin kecil CV, semakin **stabil atau konsisten** data tersebut.
    """)

    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)

    # ===========================================
    # 🧮 INPUT DATA
    # ===========================================
    st.subheader("📊 Input Data Dua Kelas Mahasiswa")

    col1, col2 = st.columns(2)
    with col1:
        data1_input = st.text_area("Nilai Kelas A (pisahkan dengan koma)", "60,65,70,75,80,85,90,95")
    with col2:
        data2_input = st.text_area("Nilai Kelas B (pisahkan dengan koma)", "50,55,60,65,70,75,80,85,90,95")

    def convert_to_array(data_str):
        try:
            return np.array([float(x.strip()) for x in data_str.split(",") if x.strip() != ""])
        except:
            return np.array([])

    data1 = convert_to_array(data1_input)
    data2 = convert_to_array(data2_input)

    if len(data1) > 0 and len(data2) > 0:
        st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)
        st.subheader("📈 Statistik Deskriptif Kelas A dan Kelas B")

        def hitung_statistik(data):
            mean = np.mean(data)
            range_ = np.max(data) - np.min(data)
            deviasi_rata = np.mean(np.abs(data - mean))
            var = np.var(data)
            std = np.std(data)
            cv = (std / mean) * 100 if mean != 0 else 0
            return {
                "Rata-rata": mean,
                "Rentang": range_,
                "Simpangan Rata-rata": deviasi_rata,
                "Varians": var,
                "Standar Deviasi": std,
                "Koefisien Variasi (%)": cv
            }

        hasil_a = hitung_statistik(data1)
        hasil_b = hitung_statistik(data2)

        df = pd.DataFrame({
            "Ukuran": list(hasil_a.keys()),
            "Kelas A": list(hasil_a.values()),
            "Kelas B": list(hasil_b.values())
        })
        st.dataframe(df, use_container_width=True)

        # ===========================================
        # 📉 VISUALISASI SEBARAN DATA
        # ===========================================
        st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)
        st.subheader("📉 Visualisasi Sebaran Data")

        df_viz = pd.DataFrame({
            "Nilai": np.concatenate([data1, data2]),
            "Kelas": ["A"] * len(data1) + ["B"] * len(data2)
        })
        chart = alt.Chart(df_viz).mark_circle(size=90).encode(
            x=alt.X("Nilai", title="Nilai Mahasiswa"),
            y=alt.Y("Kelas", title="Kelas"),
            color="Kelas",
            tooltip=["Kelas", "Nilai"]
        ).properties(
            width=600, height=200, title="Sebaran Nilai Dua Kelas"
        )

        st.altair_chart(chart, use_container_width=True)

        # ===========================================
        # 🔍 INTERPRETASI HASIL
        # ===========================================
        st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)
        st.subheader("🔍 Interpretasi")
    
        if hasil_a["Koefisien Variasi (%)"] < hasil_b["Koefisien Variasi (%)"]:
            st.success(f"✅ **Kelas A lebih stabil**, karena memiliki CV lebih kecil ({hasil_a['Koefisien Variasi (%)']:.2f}%) dibandingkan Kelas B ({hasil_b['Koefisien Variasi (%)']:.2f}%).")
        elif hasil_a["Koefisien Variasi (%)"] > hasil_b["Koefisien Variasi (%)"]:
            st.success(f"✅ **Kelas B lebih stabil**, karena memiliki CV lebih kecil ({hasil_b['Koefisien Variasi (%)']:.2f}%) dibandingkan Kelas A ({hasil_a['Koefisien Variasi (%)']:.2f}%).")
        else:
            st.info("⚖️ Kedua kelas memiliki tingkat kestabilan yang sama berdasarkan CV.")

    else:
        st.warning("⚠️ Masukkan data numerik yang valid untuk kedua kelas (pisahkan dengan koma).")

    # ===========================================
    # 🧩 AKTIVITAS MAHASISWA
    # ===========================================
    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)
    st.subheader("🧩 Aktivitas Mahasiswa")

    st.markdown("""
    **Tugas:**
    1. Masukkan data nilai dua kelas berbeda di atas.  
    2. Amati tabel hasil perhitungan dan grafik sebarannya.  
    3. Tentukan kelas mana yang lebih **stabil** dan jelaskan alasannya.  
    4. Tulis hasil pengamatanmu di bawah ini 👇
    """)

    jawaban = st.text_area("💬 Jawaban Mahasiswa:")
    if st.button("Kirim Jawaban"):
        st.success("Terima kasih! Jawabanmu telah disimpan untuk evaluasi kelas. ✅")

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)
    st.caption("💡 Tips: Gunakan koefisien variasi untuk membandingkan dua kelompok data dengan satuan yang sama.")

def materi9():
    # ============================================================
    # 🎓 JUDUL DAN PENJELASAN MATERI
    # ============================================================
    st.title("📘 Analisis Data Kelompok (Interaktif)")

    st.markdown("""
    ### 📖 Materi Pembelajaran

    Dalam analisis data berkelompok, kita menyusun data dalam bentuk **tabel distribusi frekuensi** agar lebih mudah dianalisis.

    #### 1️⃣ Frekuensi Kumulatif
    Frekuensi yang dijumlahkan secara bertahap dari kelas pertama sampai kelas terakhir.

    #### 2️⃣ Distribusi Relatif
    Frekuensi tiap kelas dibandingkan dengan total data:
    $$ f_{rel} = \\frac{f_i}{\\sum f_i} $$

    #### 3️⃣ Grafik Ogive
    Grafik garis yang menggambarkan **frekuensi kumulatif** terhadap **batas atas kelas**.

    #### 4️⃣ Estimasi Mean Data Berkelompok
    $$ \\bar{X} = \\frac{\\sum (f_i \\times x_i)}{\\sum f_i} $$  
    di mana \\( x_i \\) = titik tengah kelas.

    #### 5️⃣ Estimasi Simpangan Baku (Standar Deviasi)
    $$ S = \\sqrt{\\frac{\\sum f_i (x_i - \\bar{X})^2}{\\sum f_i}} $$

    """)

    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)

    # ============================================================
    # 🧮 INPUT DATA DISTRIBUSI KELOMPOK
    # ============================================================
    st.subheader("📊 Input Data Kelompok")

    jumlah_kelas = st.number_input("Jumlah Kelas Interval:", min_value=3, max_value=12, value=5)
    data_kelas = []

    for i in range(int(jumlah_kelas)):
        col1, col2, col3 = st.columns(3)
        with col1:
            batas_bawah = st.number_input(f"Batas Bawah Kelas {i+1}", key=f"bawah_{i}")
        with col2:
            batas_atas = st.number_input(f"Batas Atas Kelas {i+1}", key=f"atas_{i}")
        with col3:
            frek = st.number_input(f"Frekuensi Kelas {i+1}", min_value=0, key=f"frek_{i}")
        data_kelas.append((batas_bawah, batas_atas, frek))

    # ============================================================
    # 📋 BUAT DATAFRAME
    # ============================================================
    df = pd.DataFrame(data_kelas, columns=["Batas Bawah", "Batas Atas", "Frekuensi"])
    df["Titik Tengah"] = (df["Batas Bawah"] + df["Batas Atas"]) / 2
    df["Frekuensi Kumulatif"] = df["Frekuensi"].cumsum()
    total_frek = df["Frekuensi"].sum()
    df["Frekuensi Relatif"] = (df["Frekuensi"] / total_frek) if total_frek > 0 else 0

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)
    st.subheader("📋 Tabel Distribusi Frekuensi")
    st.dataframe(df, use_container_width=True)

    # ============================================================
    # 📊 OGIVE
    # ============================================================
    st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)
    st.subheader("📈 Grafik Ogive (Frekuensi Kumulatif)")

    if total_frek > 0:
        chart_ogive = alt.Chart(df).mark_line(point=True, color="#FF6B6B").encode(
            x=alt.X("Batas Atas", title="Batas Atas Kelas"),
            y=alt.Y("Frekuensi Kumulatif", title="Frekuensi Kumulatif"),
            tooltip=["Batas Atas", "Frekuensi Kumulatif"]
        ).properties(
            title="Grafik Ogive",
            width=600, height=400
        )
        st.altair_chart(chart_ogive, use_container_width=True)
    else:
        st.info("Masukkan frekuensi lebih dari 0 untuk menampilkan ogive.")

    # ============================================================
    # 📈 ESTIMASI MEAN DAN SIMPANGAN BAKU
    # ============================================================
    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)
    st.subheader("📉 Estimasi Mean dan Simpangan Baku")

    if total_frek > 0:
        mean_est = np.sum(df["Frekuensi"] * df["Titik Tengah"]) / total_frek
        var_est = np.sum(df["Frekuensi"] * (df["Titik Tengah"] - mean_est)**2) / total_frek
        std_est = np.sqrt(var_est)

        st.success(f"**Estimasi Mean (Rata-rata):** {mean_est:.2f}")
        st.success(f"**Estimasi Simpangan Baku (Standar Deviasi):** {std_est:.2f}")
    else:
        st.warning("⚠️ Data belum lengkap. Masukkan nilai frekuensi terlebih dahulu.")

    # ============================================================
    # 📊 VISUALISASI DISTRIBUSI RELATIF
    # ============================================================
    st.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
    st.subheader("📊 Diagram Distribusi Relatif")

    if total_frek > 0:
        chart_rel = alt.Chart(df).mark_bar(color="#4FC3F7").encode(
            x=alt.X("Titik Tengah:O", title="Titik Tengah Kelas"),
            y=alt.Y("Frekuensi Relatif", title="Frekuensi Relatif"),
            tooltip=["Titik Tengah", "Frekuensi Relatif"]
        ).properties(
            title="Diagram Distribusi Relatif",
            width=600, height=400
        )
        st.altair_chart(chart_rel, use_container_width=True)

    # ============================================================
    # 🧩 AKTIVITAS MAHASISWA
    # ============================================================
    st.markdown("<hr style='border: 2px solid #00BFFF;'>", unsafe_allow_html=True)
    st.subheader("🧩 Aktivitas Mahasiswa")

    st.markdown("""
    **Tugas:**
    1. Gunakan data nilai dari **100 mahasiswa** di kelasmu.  
    2. Buatlah **distribusi frekuensi berkelompok** (misalnya interval 50–59, 60–69, dst).  
    3. Tentukan:
       - Frekuensi kumulatif  
       - Frekuensi relatif  
       - Estimasi mean dan simpangan baku  
    4. Buat **grafik ogive** dari hasil data tersebut.  
        5. Tuliskan hasil dan kesimpulanmu di bawah ini 👇
    """)

    jawaban = st.text_area("Jawabam Mahasiswa1")
    if st.button("Kirim Jawaban1"):
        st.success("Terima kasih! Jawabanmu telah disimpan untuk evaluasi. ✅")

    st.markdown("<hr style='border: 1px dashed gray;'>", unsafe_allow_html=True)
    st.caption("💡 Tips: Semakin kecil simpangan baku, semakin homogen atau seragam data tersebut.")

def materi10():
    # ===============================
    # 📚 MATERI TEORI PELUANG
    # ===============================

    st.title("🎲 Materi dan Latihan: Probabilitas (Teori Peluang)")

    st.markdown("---")

    st.header("1️⃣ Konsep Peluang dan Ruang Sampel")

    st.write("""
    Peluang (probability) adalah ukuran kemungkinan terjadinya suatu peristiwa.  
    Nilai peluang **berada antara 0 dan 1**:
    - 0 berarti peristiwa **tidak mungkin terjadi**
    - 1 berarti peristiwa **pasti terjadi**

    **Ruang sampel (S)** adalah himpunan dari semua hasil yang mungkin dari suatu percobaan.
    """)

    st.info("🧩 Contoh: Melempar sebuah dadu memiliki ruang sampel S = {1, 2, 3, 4, 5, 6}")

    st.markdown("---")

    st.header("2️⃣ Peluang Kejadian Tunggal dan Gabungan")

    st.write("""
    - **Kejadian tunggal:** satu peristiwa yang diamati.  
      Contoh: muncul angka 3 saat melempar dadu.
  
    - **Kejadian gabungan:** dua atau lebih peristiwa yang diamati bersama.  
      Contoh: muncul angka genap **dan** lebih dari 3.
    """)

    st.code("P(A) = n(A) / n(S)  # jumlah kejadian yang diinginkan / jumlah semua kejadian", language="python")

    st.markdown("---")

    st.header("3️⃣ Aturan Penjumlahan dan Perkalian Peluang")

    st.write("""
    - **Penjumlahan (OR):**  
      Jika A dan B saling lepas,  
      P(A ∪ B) = P(A) + P(B)`

    - **Perkalian (AND):**  
      Jika A dan B **independen**,  
  `P(A ∩ B) = P(A) × P(B)`
    """)
 
    st.info("Contoh: Peluang muncul angka genap dan lebih dari 2 pada dadu")

    if st.button("🔍 Hitung Contoh"):
        P_genap = 3 / 6
        P_lebih2 = 4 / 6
        P_gabungan = P_genap * P_lebih2
        st.success(f"P(A ∩ B) = {P_genap:.2f} × {P_lebih2:.2f} = {P_gabungan:.2f}")

    st.markdown("---")

    st.header("4️⃣ Peluang Bersyarat")

    st.write("""
    Peluang bersyarat digunakan ketika kejadian **A** bergantung pada kejadian **B**.

    Rumus:
    > P(A|B) = P(A ∩ B) / P(B)
    """)

    st.info("🧠 Contoh: Peluang siswa laki-laki yang lulus, diketahui siswa tersebut lulus ujian")

    st.markdown("---")
    
    # ===============================
    # 🧩 PERMAINAN INTERAKTIF
    # ===============================

    st.header("🎮 Simulasi Peluang: Lempar Koin dan Dadu")

    st.subheader("🪙 Lempar Koin")
    coin_side = st.radio("Pilih sisi tebakanmu:", ["Angka", "Gambar"], index=None)
    if st.button("Lempar Koin"):
        result = random.choice(["Angka", "Gambar"])
        st.write(f"🎲 Hasil lemparan: **{result}**")
        if coin_side:
            if coin_side == result:
                st.success("Selamat! Tebakanmu benar 🎉")
            else:
                st.error("Sayang sekali, tebakanmu salah 😅")

    st.markdown("---")

    st.subheader("🎲 Lempar Dadu")
    jumlah = st.slider("Berapa kali lempar dadu?", 1, 20, 5)
    if st.button("Lempar Dadu"):
        hasil = [random.randint(1, 6) for _ in range(jumlah)]
        df = pd.DataFrame({"Lempar Ke-": range(1, jumlah+1), "Hasil": hasil})
        st.table(df)
        fig = px.histogram(df, x="Hasil", nbins=6, title="Distribusi Hasil Lempar Dadu", color_discrete_sequence=["#00BFFF"])
        st.plotly_chart(fig)
        st.success(f"Rata-rata hasil: {np.mean(hasil):.2f}")

    st.markdown("---")

    st.header("🧮 Latihan Probabilitas")

    st.write("""
    Misal: dari 52 kartu remi, tentukan peluang muncul kartu **hati (♥)**.
    """)

    if st.button("Tampilkan Jawaban"):
        P = 13 / 52
        st.success(f"Peluang = 13/52 = {P:.2f}")

    st.markdown("---")

    st.header("📊 Kesimpulan")
    st.write("""
    - Peluang adalah ukuran kemungkinan suatu kejadian.
    - Nilainya antara **0 dan 1**.
    - Ada berbagai konsep penting seperti **peluang gabungan, bersyarat, dan independen**.
    - Simulasi koin & dadu membantu memahami konsep probabilitas secara nyata.
    """)

    st.markdown("<hr style='border: 2px solid #00BFFF; border-radius: 10px;'>", unsafe_allow_html=True)
    st.success("🎯 Coba ubah jumlah lemparan atau ulangi percobaan untuk melihat perbedaan hasil distribusi!")

def materi11():
    # ================================
    # 🎓 MATERI: DISTRIBUSI BINOMIAL
    # ================================
    st.title("🎯 Distribusi Binomial - Materi, Permainan, dan Latihan Interaktif")

    st.markdown("---")

    st.header("📘 1️⃣ Konsep Distribusi Binomial")

    st.write("""
    Distribusi **Binomial** digunakan untuk menggambarkan jumlah keberhasilan (sukses) 
    dari sejumlah percobaan yang **independen** dengan dua kemungkinan hasil: *berhasil (success)* atau *gagal (failure)*.

    Contoh situasi binomial:
    - Melempar koin sebanyak 10 kali dan menghitung berapa kali muncul sisi angka.
    - Menghitung berapa mahasiswa yang lulus dari 20 orang, jika peluang lulus 0.7.
    """)

    st.info("Distribusi binomial digunakan ketika setiap percobaan hanya memiliki dua hasil: sukses atau gagal.")

    st.markdown("---")

    st.header("🧮 2️⃣ Rumus Distribusi Binomial")

    st.latex(r"""
    P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}
    """)

    st.write("""
    Keterangan:  
    - **n** = jumlah percobaan  
    - **k** = jumlah keberhasilan  
    - **p** = peluang sukses tiap percobaan  
    - **C(n, k)** = kombinasi = n! / (k!(n - k)!)
    """)

    st.markdown("---")

    st.header("🎲 3️⃣ Simulasi: Permainan Lempar Koin Binomial")

    st.write("Coba simulasi lempar koin beberapa kali dan hitung berapa kali muncul sisi **Angka (Sukses)**.")

    n = st.slider("Berapa kali kamu ingin melempar koin (n)?", 1, 50, 10)
    p = st.slider("Peluang muncul sisi Angka (p):", 0.0, 1.0, 0.5, step=0.1)
    if st.button("🎮 Jalankan Simulasi"):
        hasil = np.random.binomial(n, p, size=1000)
        df = pd.DataFrame({"Jumlah Sukses": hasil})
        st.write(f"📊 Dari 1000 simulasi, rata-rata sukses: **{np.mean(hasil):.2f}**")

        fig = px.histogram(df, x="Jumlah Sukses", nbins=n+1, title="Distribusi Hasil Simulasi Binomial",
                       color_discrete_sequence=["#00BFFF"])
        st.plotly_chart(fig, use_container_width=True)
        st.success("✨ Lihat bagaimana bentuk distribusi mendekati distribusi normal saat n besar!")

    st.markdown("---")

    st.header("🎮 4️⃣ Permainan Probabilitas Binomial")

    st.write("Bayangkan kamu melempar koin 5 kali. Berapa peluang muncul **tepat 3 sisi Angka** jika p = 0.5?")

    if st.button("🔍 Tampilkan Jawaban Contoh"):
        n, k, p = 5, 3, 0.5
        kombinasi = math.comb(n, k)
        peluang = kombinasi * (p ** k) * ((1 - p) ** (n - k))
        st.success(f"P(X=3) = C(5,3) × 0.5³ × 0.5² = {peluang:.3f}")

    st.markdown("---")

    st.header("🧩 5️⃣ Latihan Interaktif")

    st.write("Sekarang giliran kamu menghitung peluang binomial dari data yang kamu pilih 👇")

    col1, col2, col3 = st.columns(3)
    with col1:
        n_user = st.number_input("Jumlah percobaan (n):", min_value=1, max_value=100, value=10)
    with col2:
        k_user = st.number_input("Jumlah keberhasilan (k):", min_value=0, max_value=100, value=3)
    with col3:
        p_user = st.number_input("Peluang sukses (p):", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

    if st.button("🧮 Hitung Peluang"):
        try:
            kombinasi_user = math.comb(n_user, k_user)
            prob_user = kombinasi_user * (p_user ** k_user) * ((1 - p_user) ** (n_user - k_user))
            st.success(f"P(X={k_user}) = {prob_user:.4f}")
        except:
            st.error("⚠️ Pastikan nilai k ≤ n!")

    st.markdown("---")

    st.header("📈 6️⃣ Visualisasi Distribusi Binomial")

    st.write("Lihat grafik distribusi peluang untuk berbagai nilai keberhasilan (k).")

    n_graph = st.slider("Jumlah percobaan n:", 1, 30, 10)
    p_graph = st.slider("Peluang sukses p:", 0.0, 1.0, 0.5, step=0.05)

    x = np.arange(0, n_graph + 1)
    y = [math.comb(n_graph, k) * (p_graph ** k) * ((1 - p_graph) ** (n_graph - k)) for k in x]

    fig2 = px.bar(x=x, y=y, title=f"Distribusi Binomial (n={n_graph}, p={p_graph})",
                  labels={'x': 'Jumlah Keberhasilan (k)', 'y': 'P(X=k)'},
                  color_discrete_sequence=["#FF6347"])
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    st.header("🧭 7️⃣ Kesimpulan")
    st.write("""
    - Distribusi binomial digunakan ketika percobaan memiliki dua hasil (sukses/gagal).  
    - Parameter utama: **n (jumlah percobaan)** dan **p (peluang sukses)**.  
    - Bentuk distribusinya **simetris jika p = 0.5**, dan **miring** jika p mendekati 0 atau 1.  
    - Bisa digunakan untuk memodelkan berbagai fenomena seperti ujian, percobaan, atau eksperimen acak.
    """)

    st.markdown("<hr style='border: 2px solid #00BFFF; border-radius: 10px;'>", unsafe_allow_html=True)
    st.success("🎯 Coba ubah nilai n dan p untuk melihat perubahan bentuk distribusi binomial!")

def materi12():
    # ================================
    # 🎓 MATERI: DISTRIBUSI POISSON
    # ================================

    st.title("💡 Distribusi Poisson - Materi, Permainan, dan Latihan Interaktif")

    st.markdown("---")

    st.header("📘 1️⃣ Konsep Distribusi Poisson")

    st.write("""
    Distribusi **Poisson** digunakan untuk menghitung banyaknya kejadian dalam suatu interval waktu, jarak, atau area tertentu,  
    **dengan asumsi kejadian terjadi secara acak dan independen**.

    Contoh penggunaan:
    - Jumlah kendaraan yang lewat di jalan dalam 1 menit.  
    - Banyaknya pelanggan datang ke toko dalam 1 jam.  
    - Jumlah email yang masuk dalam 10 menit.
    """)

    st.info("Distribusi Poisson cocok untuk data yang menunjukkan *jumlah kejadian dalam interval waktu atau ruang tertentu*.")

    st.markdown("---")

    st.header("🧮 2️⃣ Rumus Distribusi Poisson")

    st.latex(r"""
    P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}
    """)

    st.write("""
    Keterangan:  
    - **λ (lambda)** = rata-rata kejadian dalam interval  
    - **k** = jumlah kejadian yang diamati  
    - **e** = bilangan eksponensial (~2.71828)  
    """)

    st.markdown("---")

    # ================================
    # 🎲 3️⃣ PERMAINAN SIMULASI POISSON
    # ================================
    st.header("🎲 Simulasi Kejadian Poisson")

    st.write("Bayangkan kamu mencatat jumlah pelanggan yang datang ke toko per jam dengan rata-rata λ = 4. Mari kita lihat hasil acak 100 kali pengamatan.")

    lambda_sim = st.slider("Tentukan nilai rata-rata kejadian (λ):", 1, 20, 4)
    if st.button("🎮 Jalankan Simulasi Poisson"):
        hasil = np.random.poisson(lambda_sim, 100)
        df = pd.DataFrame({"Kejadian": hasil})
        st.write(f"📊 Rata-rata dari simulasi: **{np.mean(hasil):.2f}**")

        fig = px.histogram(df, x="Kejadian", nbins=lambda_sim*2,
                           title=f"Distribusi Simulasi Poisson (λ = {lambda_sim})",
                           color_discrete_sequence=["#00BFFF"])
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ================================
    # 🎮 4️⃣ PERMAINAN TEBAK KEJADIAN
    # ================================
    st.header("🎯 Permainan: Tebak Kejadian")

    st.write("""
    Sebuah pusat panggilan menerima rata-rata **λ = 3 panggilan per menit**.  
    Berapa peluang menerima **tepat 5 panggilan** dalam satu menit?
    """)

    if st.button("🔍 Tampilkan Jawaban Contoh"):
        lambd = 3
        k = 5
        prob = (math.exp(-lambd) * lambd**k) / math.factorial(k)
        st.success(f"P(X=5) = e^-3 × 3⁵ / 5! = {prob:.4f}")

    st.markdown("---")

    # ================================
    # 🧩 5️⃣ LATIHAN INTERAKTIF
    # ================================
    st.header("🧩 Latihan Interaktif Poisson")

    st.write("Masukkan nilai λ (rata-rata kejadian) dan k (jumlah kejadian yang diinginkan):")

    col1, col2 = st.columns(2)
    with col1:
        lambda_user = st.number_input("Masukkan λ (rata-rata kejadian):", min_value=0.1, max_value=50.0, value=4.0)
    with col2:
        k_user = st.number_input("Masukkan k (jumlah kejadian yang diamati):", min_value=0, max_value=100, value=2)

    if st.button("🧮 Hitung Peluang Poisson"):
        prob_user = (math.exp(-lambda_user) * (lambda_user ** k_user)) / math.factorial(k_user)
        st.success(f"P(X={k_user}) = {prob_user:.5f}")

    st.markdown("---")

    # ================================
    # 📈 6️⃣ VISUALISASI DISTRIBUSI POISSON
    # ================================
    st.header("📈 Visualisasi Distribusi Poisson")

    st.write("Lihat bagaimana bentuk distribusi berubah jika λ (rata-rata kejadian) meningkat.")

    lambda_graph = st.slider("Ubah nilai λ untuk grafik:", 1, 30, 5)

    x = np.arange(0, lambda_graph + 10)
    y = [(math.exp(-lambda_graph) * lambda_graph**k) / math.factorial(k) for k in x]

    fig2 = px.bar(x=x, y=y, title=f"Distribusi Poisson (λ = {lambda_graph})",
                  labels={'x': 'Jumlah Kejadian (k)', 'y': 'P(X=k)'},
                  color_discrete_sequence=["#FF6347"])
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ================================
    # 🎓 7️⃣ RANGKUMAN
    # ================================
    st.header("📚 Kesimpulan")

    st.write("""
✅ **Distribusi Poisson** digunakan untuk menghitung peluang jumlah kejadian dalam periode tertentu.  
✅ Parameter utamanya adalah **λ (rata-rata kejadian)**.  
✅ Distribusi Poisson **mendekati distribusi normal** jika λ besar (λ > 20).  
✅ Cocok digunakan untuk memodelkan data seperti kedatangan, panggilan, atau kejadian acak lainnya.
    """)

    st.markdown("<hr style='border: 2px solid #00BFFF; border-radius: 10px;'>", unsafe_allow_html=True)
    st.success("🎯 Coba ubah nilai λ untuk melihat bagaimana distribusi Poisson berubah bentuknya!")

def materi13():
    st.title("🎲 Ekspektasi dan Variansi Variabel Acak")
    st.markdown("Pelajari konsep ekspektasi dan variansi melalui simulasi interaktif!")

    menu = st.radio("📘 Menu", ["Materi", "Simulasi Ekspektasi", "Permainan Nilai Harapan", "Latihan"])

    # =================== 1. Materi ===================
    if menu == "Materi":
        st.header("📖 Materi Teori")
        st.markdown("""
        ### Ekspektasi (Nilai Harapan)
        Ekspektasi adalah rata-rata teoritis dari suatu variabel acak.
        \nRumus:  $ E(X) = Σ x·P(x) $
        \nContoh: lempar dadu → E(X)=3.5
    
        ### Variansi
        Mengukur penyebaran nilai terhadap rata-rata.
        \n$ Var(X) = E(X²) - [E(X)]² $
        """)
        

    # =================== 2. Simulasi Ekspektasi ===================
    elif menu == "Simulasi Ekspektasi":
        st.header("🎲 Simulasi Ekspektasi Lempar Dadu")

        n = st.slider("Jumlah lemparan", 10, 10000, 1000)
        hasil = np.random.randint(1, 7, n)

        ekspektasi_empiris = np.mean(hasil)
        ekspektasi_teoritis = 3.5

        st.metric("Ekspektasi Empiris", round(ekspektasi_empiris, 3))
        st.metric("Ekspektasi Teoritis", ekspektasi_teoritis)

        fig, ax = plt.subplots()
        ax.hist(hasil, bins=np.arange(0.5, 7.5, 1), rwidth=0.8)
        ax.set_xlabel("Hasil Dadu")
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)

    # =================== 3. Permainan Nilai Harapan ===================
    elif menu == "Permainan Nilai Harapan":
        st.header("🧩 Game Nilai Harapan")

        st.write("Tebak nilai rata-rata hasil dari 100 lemparan dadu!")
        tebakan = st.number_input("Masukkan tebakan ekspektasi (antara 1 dan 6)", 1.0, 6.0, 3.0)

        if st.button("🎲 Jalankan Permainan"):
            hasil = [random.randint(1,6) for _ in range(100)]
            ekspektasi_sesungguhnya = np.mean(hasil)
            st.success(f"Nilai rata-rata hasil = {ekspektasi_sesungguhnya:.2f}")
            if abs(tebakan - ekspektasi_sesungguhnya) < 0.3:
                st.balloons()
                st.info("Hebat! Tebakanmu sangat mendekati nilai ekspektasi!")
            else:
                st.warning("Coba lagi! Perhatikan penyebaran hasil dadu.")
            st.bar_chart(pd.Series(hasil).value_counts().sort_index())

    # =================== 4. Latihan ===================
    elif menu == "Latihan":
        st.header("📝 Latihan Ekspektasi dan Variansi")

        st.markdown("""
        **1️⃣ Soal 1:**  
        Diketahui X = jumlah sisi atas dadu. Hitung:
        - E(X)
        - Var(X)
    
        **2️⃣ Soal 2:**  
        Jika X adalah jumlah sukses dalam 3 kali lempar koin (P(sukses)=0.5).  
        Hitung E(X) dan Var(X)!
    
        **3️⃣ Soal 3:**  
        Buat simulasi sendiri menggunakan random.randint untuk membuktikan nilai teoritis!
        """)
        st.code("""
    import numpy as np
    # Simulasi lempar dadu 10000 kali
    data = np.random.randint(1,7,10000)
    print("Ekspektasi =", np.mean(data))
    print("Variansi =", np.var(data))
        """, language="python")

def materi14():
    st.title("📈 Distribusi Normal dan Kurva Lonceng")
    st.markdown("""
    Belajar interaktif tentang **Distribusi Normal (Gaussian Distribution)**  
    Ubah parameter rata-rata (μ) dan simpangan baku (σ) untuk melihat bagaimana bentuk kurva berubah.
    """)

    menu = st.radio("📘 Menu", 
                        ["Materi", "Simulasi Kurva Lonceng", "Permainan Interaktif", "Latihan"])

    # ===================== 1. Materi =====================
    if menu == "Materi":
        st.header("📖 Materi Distribusi Normal")
        st.image("https://i.imgur.com/xW8nOrv.png", caption="Kurva Lonceng (Normal Distribution)", use_container_width=True)
        st.markdown("""
        **Distribusi Normal** menggambarkan data yang tersebar merata di sekitar nilai rata-rata.
        \nRumus:  
        $ f(x) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}} $
        \nDimana:
        - μ = mean (rata-rata)
        - σ = standar deviasi
        """)
        st.markdown("**Aturan Empiris:**")
        st.markdown("- 68% data berada di μ ± 1σ  \n- 95% data berada di μ ± 2σ  \n- 99.7% data berada di μ ± 3σ")

    # ===================== 2. Simulasi Kurva =====================
    elif menu == "Simulasi Kurva Lonceng":
        st.header("🎨 Simulasi Kurva Normal")

        mu = st.slider("Rata-rata (μ)", -10.0, 10.0, 0.0)
        sigma = st.slider("Simpangan Baku (σ)", 0.5, 5.0, 1.0)
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
        y = norm.pdf(x, mu, sigma)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x, y, label=f"μ={mu}, σ={sigma}", color='blue')
        ax.fill_between(x, y, 0, alpha=0.2, color='blue')
        ax.axvline(mu, color='red', linestyle='--', label='Mean (μ)')
        ax.set_title("Kurva Distribusi Normal")
        ax.legend()
        st.pyplot(fig)

        st.info("Ubah nilai μ dan σ untuk melihat perubahan bentuk kurva!")

    # ===================== 3. Permainan =====================
    elif menu == "Permainan Interaktif":
        st.header("🎯 Permainan: Kurva Lonceng Challenge")

        st.markdown("Tebak peluang data berada di antara dua batas pada distribusi normal!")

        mu = st.slider("Pilih Rata-rata (μ)", -5.0, 5.0, 0.0)
        sigma = st.slider("Pilih Simpangan Baku (σ)", 0.5, 3.0, 1.0)
        lower = st.number_input("Batas bawah (x₁)", -10.0, 10.0, mu - 1*sigma)
        upper = st.number_input("Batas atas (x₂)", -10.0, 10.0, mu + 1*sigma)

        if st.button("🎲 Hitung Peluang!"):
            p = norm.cdf(upper, mu, sigma) - norm.cdf(lower, mu, sigma)
            st.success(f"Peluang data berada antara {lower} dan {upper} adalah {p*100:.2f}%")
            if 0.67 < p < 0.69:
                st.balloons()
                st.info("Benar! Itu adalah interval 1σ (sekitar 68%)!")
            elif 0.93 < p < 0.97:
                st.info("Itu mendekati interval 2σ (95%)!")
            elif 0.99 < p < 1.0:
                st.info("Itu mendekati interval 3σ (99.7%)!")

            x = np.linspace(mu - 4*sigma, mu + 4*sigma, 400)
            y = norm.pdf(x, mu, sigma)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(x, y, color='blue')
            ax.fill_between(x, y, 0, where=(x > lower) & (x < upper), color='orange', alpha=0.5)
            st.pyplot(fig)

    # ===================== 4. Latihan =====================
    elif menu == "Latihan":
        st.header("📝 Latihan Distribusi Normal")

        st.markdown("""
        **1️⃣ Soal 1:**  
        Sebuah data nilai ujian mahasiswa berdistribusi normal dengan μ = 70 dan σ = 10.  
        - Hitung peluang mahasiswa memiliki nilai antara 60 dan 80.
    
        **2️⃣ Soal 2:**  
        Jika tinggi badan pria memiliki μ = 170 cm dan σ = 5 cm,  
        berapa peluang seseorang memiliki tinggi lebih dari 180 cm?
    
        **3️⃣ Soal 3:**  
        Gunakan Python untuk menghitung peluang tersebut dengan `scipy.stats.norm`.
        """)

        st.code("""
    from scipy.stats import norm

    # Contoh Soal 1
    mu, sigma = 70, 10
    p = norm.cdf(80, mu, sigma) - norm.cdf(60, mu, sigma)
    print("Peluang antara 60 dan 80 =", round(p*100,2), "%")
        """, language="python")

        st.info("Cobalah ubah μ dan σ untuk memahami efeknya pada distribusi normal.")

def materi15():
    st.title("📈 Z-Score dan Tabel Distribusi Normal")
    st.markdown("""
    Pelajari konsep **Z-Score**, **Tabel Distribusi Normal**, dan **cara menghitung peluang dari data berdistribusi normal**  
    dengan simulasi dan permainan interaktif 🎮.
    """)

    menu = st.radio("📘 Menu", ["Materi", "Simulasi Z-Score", "Permainan Z", "Latihan"])

    # ===================== 1. Materi =====================
    if menu == "Materi":
        st.header("📖 Pengantar Z-Score")
        st.markdown("""
        **Rumus:**
        \n
        $ Z = \\frac{X - \\mu}{\\sigma} $
        \nZ-score menunjukkan seberapa jauh nilai X dari rata-rata dalam satuan simpangan baku.
        """)
        st.image("https://i.imgur.com/xW8nOrv.png", caption="Kurva Normal dan Z-Score", use_container_width=True)

        st.subheader("Contoh:")
        st.latex(r"Z = \frac{85 - 70}{10} = 1.5")
        st.write("Artinya nilai 85 berada 1,5 simpangan baku di atas rata-rata.")

        st.markdown("""
        ### 📊 Hubungan Z-Score dengan Tabel Normal
        - **Z = 0** → area = 0.5 (50%)  
        - **Z = 1** → area ≈ 0.8413  
        - **Z = 2** → area ≈ 0.9772  
        - **Z = 3** → area ≈ 0.9987
        """)

    # ===================== 2. Simulasi =====================
    elif menu == "Simulasi Z-Score":
        st.header("🎨 Simulasi Kurva Normal dan Nilai Z")

        mu = st.slider("Rata-rata (μ)", -10.0, 10.0, 0.0)
        sigma = st.slider("Simpangan Baku (σ)", 0.5, 5.0, 1.0)
        x_value = st.number_input("Masukkan Nilai X", -20.0, 20.0, 1.0)

        z = (x_value - mu) / sigma
        st.success(f"Nilai Z = {z:.2f}")

        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
        y = norm.pdf(x, mu, sigma)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x, y, color='blue')
        ax.fill_between(x, y, 0, where=(x < x_value), color='orange', alpha=0.5)
        ax.axvline(mu, color='red', linestyle='--', label='Mean (μ)')
        ax.axvline(x_value, color='orange', linestyle='--', label=f'X = {x_value}')
        ax.set_title(f"Kurva Normal μ={mu}, σ={sigma}")
        ax.legend()
        st.pyplot(fig)

        prob = norm.cdf(x_value, mu, sigma)
        st.info(f"Peluang data ≤ {x_value} adalah {prob*100:.2f}%")

    # ===================== 3. Permainan =====================
    elif menu == "Permainan Z":
        st.header("🎯 Permainan: Tebak Peluang Z")

        st.markdown("Masukkan nilai dan tebak berapa peluangnya di bawah kurva normal!")

        mu = 0
        sigma = 1
        z_guess = st.slider("Tebak nilai Z", -3.0, 3.0, 1.0)
        st.write("Hitung peluang P(Z ≤ z)")

        if st.button("🎲 Hitung Peluang!"):
            prob = norm.cdf(z_guess, mu, sigma)
            st.success(f"P(Z ≤ {z_guess}) = {prob:.4f} atau {prob*100:.2f}%")

            x = np.linspace(-4, 4, 400)
            y = norm.pdf(x)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(x, y)
            ax.fill_between(x, y, 0, where=(x < z_guess), color='orange', alpha=0.4)
            ax.axvline(0, color='red', linestyle='--')
            ax.axvline(z_guess, color='orange', linestyle='--')
            ax.set_title("Distribusi Normal Standar")
            st.pyplot(fig)

            if 0.67 < prob < 0.69:
                st.balloons()
                st.info("🎉 Tepat! Itu sekitar area 1σ (68%)!")
            elif 0.93 < prob < 0.97:
                st.info("Itu sekitar area 2σ (95%)!")
            elif 0.99 < prob < 1.0:
                st.info("Itu area 3σ (99.7%)!")

    # ===================== 4. Latihan =====================
    elif menu == "Latihan":
        st.header("📝 Latihan Soal Z-Score dan Peluang")

        st.markdown("""
        **Soal 1:**  
        Nilai ujian mahasiswa berdistribusi normal dengan μ = 70 dan σ = 10.  
        Berapa peluang mahasiswa memiliki nilai di bawah 80?

        **Soal 2:**  
        Berapa peluang nilai berada antara 60 dan 80?

        **Soal 3:**  
        Jika nilai 85, berapa Z-scorenya?
        """)

        st.code("""
    from scipy.stats import norm

    mu, sigma = 70, 10
    # Soal 1
    p1 = norm.cdf(80, mu, sigma)
    print("P(X ≤ 80) =", round(p1*100, 2), "%")

    # Soal 2
    p2 = norm.cdf(80, mu, sigma) - norm.cdf(60, mu, sigma)
    print("P(60 ≤ X ≤ 80) =", round(p2*100, 2), "%")

    # Soal 3
    z = (85 - mu) / sigma
    print("Z-score =", round(z, 2))
        """, language="python")

        st.info("Cobalah ubah μ dan σ untuk memahami bagaimana peluang berubah!")

def materi16():
    st.title("📈 Interpretasi Area di Bawah Kurva Normal")
    st.markdown("### 🎯 Jelajahi probabilitas dan area di bawah kurva normal secara interaktif")

    # Input parameter
    mu = st.slider("Rata-rata (μ)", 40, 100, 60)
    sigma = st.slider("Simpangan baku (σ)", 1, 20, 10)
    x1 = st.number_input("Nilai batas bawah (X₁)", value=50)
    x2 = st.number_input("Nilai batas atas (X₂)", value=70)

    # Hitung probabilitas area di bawah kurva
    z1, z2 = (x1 - mu)/sigma, (x2 - mu)/sigma
    area = norm.cdf(z2) - norm.cdf(z1)

    # Plot kurva normal
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x, y, color='blue')
    ax.fill_between(x, y, where=(x >= x1) & (x <= x2), color='lightgreen')
    ax.axvline(mu, color='red', linestyle='--', label='μ (rata-rata)')
    ax.set_title("Kurva Normal dan Area di Bawahnya")
    ax.legend()
    st.pyplot(fig)

    st.success(f"📊 Area di antara {x1} dan {x2} = **{area:.4f}** atau {area*100:.2f}% dari total data")

    # Permainan interaktif
    st.markdown("## 🎮 Permainan: Tebak Area!")
    guess = st.slider("Tebak berapa persen data di antara X₁ dan X₂", 0, 100, 50)
    if st.button("Cek Jawaban"):
        diff = abs(guess - area*100)
        if diff < 5:
            st.balloons()
            st.success(f"🎉 Hebat! Tebakanmu mendekati nilai sebenarnya ({area*100:.2f}%)")
        else:
            st.warning(f"😅 Hampir! Nilai sebenarnya adalah {area*100:.2f}%")
            
def materi17():
    st.title("📊 Sampling dan Distribusi Sampling")
    st.markdown("Simulasi interaktif untuk memahami konsep distribusi sampling, standard error, dan CLT.")

    # --- Input populasi ---
    st.sidebar.header("🎯 Pengaturan Populasi & Sampel")
    pop_mean = st.sidebar.slider("Rata-rata Populasi (μ)", 50, 100, 70)
    pop_std = st.sidebar.slider("Simpangan Baku Populasi (σ)", 5, 30, 10)
    pop_size = st.sidebar.slider("Ukuran Populasi", 1000, 10000, 5000)
    sample_size = st.sidebar.slider("Ukuran Sampel (n)", 5, 200, 30)
    num_samples = st.sidebar.slider("Jumlah Sampel (k)", 10, 1000, 200)

    # --- Generate populasi ---
    np.random.seed(42)
    population = np.random.normal(pop_mean, pop_std, pop_size)

    # --- Ambil banyak sampel acak ---
    sample_means = [np.mean(np.random.choice(population, sample_size)) for _ in range(num_samples)]

    # --- Standard Error ---
    se = pop_std / np.sqrt(sample_size)

    # --- Visualisasi ---
    st.subheader("📈 Distribusi Sampling dari Mean")
    fig, ax = plt.subplots(figsize=(8,4))
    ax.hist(sample_means, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    ax.axvline(np.mean(sample_means), color='red', linestyle='--', label='Mean Sampling')
    ax.axvline(pop_mean, color='green', linestyle='--', label='Mean Populasi')
    ax.legend()
    ax.set_xlabel("Nilai Rata-rata Sampel")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

    # --- Output hasil ---
    st.success(f"📊 Mean Populasi: {pop_mean:.2f}")
    st.success(f"📊 Rata-rata Sampling: {np.mean(sample_means):.2f}")
    st.info(f"📉 Standard Error (SE): {se:.4f}")

    # --- Permainan Interaktif ---
    st.markdown("## 🎮 Permainan: Tebak Standard Error!")
    guess = st.slider("Tebak berapa nilai SE menurutmu?", 0.0, 10.0, 2.0, 0.1)
    if st.button("Cek Jawaban"):
        diff = abs(guess - se)
        if diff < 0.2:
            st.balloons()
            st.success(f"🎉 Hebat! Tebakanmu hampir tepat! Nilai SE = {se:.2f}")
        else:
            st.warning(f"😅 Coba lagi! Nilai SE sebenarnya = {se:.2f}")

    # --- Simulasi CLT ---
    st.markdown("## 🌀 Teorema Limit Pusat (Central Limit Theorem)")
    st.write("Perhatikan bagaimana distribusi mean sampel mendekati distribusi normal saat ukuran sampel membesar.")

    sample_sizes = [5, 30, 100]
    fig2, axes = plt.subplots(1, 3, figsize=(12,4))
    for i, n in enumerate(sample_sizes):
        sample_means = [np.mean(np.random.choice(population, n)) for _ in range(300)]
        axes[i].hist(sample_means, bins=20, color='lightcoral', edgecolor='black')
        axes[i].set_title(f"n = {n}")
    st.pyplot(fig2)

def materi18():
    st.title("📊 Estimasi Parameter Interaktif")
    st.markdown("""
    Simulasi untuk memahami **estimasi titik, interval kepercayaan, dan tingkat kepercayaan (confidence level)**.
    """)

    # ----------------------------
    # Input
    # ----------------------------
    st.sidebar.header("⚙️ Pengaturan Sampel")
    mean_sample = st.sidebar.slider("Rata-rata sampel (x̄)", 50.0, 100.0, 75.0, 0.1)
    std_sample = st.sidebar.slider("Simpangan baku (σ)", 1.0, 20.0, 10.0, 0.1)
    n = st.sidebar.slider("Ukuran sampel (n)", 10, 500, 50)
    confidence = st.sidebar.selectbox("Tingkat kepercayaan (%)", [90, 95, 99])

    # ----------------------------
    # Hitung CI
    # ----------------------------
    alpha = 1 - confidence/100
    z_value = round(norm.ppf(1 - alpha/2), 3)
    se = std_sample / np.sqrt(n)
    margin_error = z_value * se
    lower = mean_sample - margin_error
    upper = mean_sample + margin_error

    # ----------------------------
    # Output utama
    # ----------------------------
    st.header("📏 Estimasi Titik dan Interval Kepercayaan")
    st.success(f"**Estimasi Titik (x̄)** = {mean_sample:.2f}")
    st.info(f"**Interval Kepercayaan {confidence}%:** {lower:.2f} ≤ μ ≤ {upper:.2f}")
    st.write(f"Margin of Error = {margin_error:.2f}")
    st.write(f"z-value (α/2 = {alpha/2:.3f}) = {z_value}")

    # ----------------------------
    # Visualisasi Kurva Normal
    # ----------------------------
    x = np.linspace(mean_sample - 4*se, mean_sample + 4*se, 200)
    y = norm.pdf(x, mean_sample, se)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, color='skyblue', lw=3)
    ax.fill_between(x, 0, y, where=(x >= lower) & (x <= upper), color='lightgreen', alpha=0.6)
    ax.axvline(mean_sample, color='red', linestyle='--', label='x̄ (mean sampel)')
    ax.axvline(lower, color='green', linestyle='--', label=f'Batas bawah ({lower:.2f})')
    ax.axvline(upper, color='green', linestyle='--', label=f'Batas atas ({upper:.2f})')
    ax.legend()
    ax.set_title(f"Distribusi Sampling (Confidence Level {confidence}%)")
    st.pyplot(fig)

    # ----------------------------
    # Permainan interaktif
    # ----------------------------
    st.subheader("🎮 Permainan: Tebak Confidence Interval!")
    st.write("Coba tebak apakah **rata-rata populasi sebenarnya (μ = 75)** termasuk dalam interval yang kamu hitung.")

    mu_pop = 75  # nilai sebenarnya
    if st.button("Cek Tebakan!"):
        if lower <= mu_pop <= upper:
            st.balloons()
            st.success("🎉 Benar! μ ada di dalam interval kepercayaan.")
        else:
            st.error("😅 Salah! μ berada di luar interval.")

    # ----------------------------
    # Latihan interaktif
    # ----------------------------
    st.markdown("---")
    st.header("🧩 Latihan: Interval Kepercayaan 95% untuk Nilai Mahasiswa")

    st.markdown("""
    Misalkan 100 mahasiswa memiliki nilai rata-rata ujian 72 dengan simpangan baku 8.  
    Tentukan **interval kepercayaan 95%** untuk rata-rata populasi.
    """)

    if st.button("💡 Tampilkan Jawaban Latihan"):
        mean_ex = 72
        sd_ex = 8
        n_ex = 100
        z_ex = 1.96
        se_ex = sd_ex / np.sqrt(n_ex)
        ci_lower = mean_ex - z_ex * se_ex
        ci_upper = mean_ex + z_ex * se_ex
        st.success(f"CI 95%: {ci_lower:.2f} ≤ μ ≤ {ci_upper:.2f}")
        st.info("Artinya: Kita 95% yakin bahwa rata-rata nilai mahasiswa sebenarnya berada di antara batas tersebut.")

    # ----------------------------
    # Simulasi pengaruh tingkat kepercayaan
    # ----------------------------
    st.markdown("---")
    st.header("📈 Pengaruh Tingkat Kepercayaan terhadap Lebar Interval")

    confidence_levels = [90, 95, 99]
    ci_ranges = []
    for cl in confidence_levels:
        z = norm.ppf(1 - (1 - cl/100)/2)
        ci_range = 2 * z * se
        ci_ranges.append(ci_range)

    fig2, ax2 = plt.subplots()
    ax2.bar(confidence_levels, ci_ranges, color=['skyblue', 'lightgreen', 'salmon'])
    ax2.set_xlabel("Tingkat Kepercayaan (%)")
    ax2.set_ylabel("Lebar Interval")
    ax2.set_title("Semakin tinggi tingkat kepercayaan → Interval semakin lebar")
    st.pyplot(fig2)

def materi19():
    st.title("🎓 Uji Hipotesis Dua Sampel (Kelas A vs Kelas B)")
    st.write("Bandingkan rata-rata nilai dua kelas dan tentukan apakah perbedaannya signifikan.")

    # --- Input Data ---
    st.sidebar.header("🔧 Pengaturan Data")
    n1 = st.sidebar.slider("Jumlah sampel Kelas A", 5, 50, 20)
    n2 = st.sidebar.slider("Jumlah sampel Kelas B", 5, 50, 20)
    mean1 = st.sidebar.slider("Rata-rata Kelas A", 50, 100, 75)
    mean2 = st.sidebar.slider("Rata-rata Kelas B", 50, 100, 70)
    sd1 = st.sidebar.slider("Standar deviasi Kelas A", 1, 20, 10)
    sd2 = st.sidebar.slider("Standar deviasi Kelas B", 1, 20, 10)
    alpha = st.sidebar.selectbox("Tingkat Signifikansi (α)", [0.01, 0.05, 0.10], index=1)

    # --- Generate Data ---
    np.random.seed(42)
    kelas_A = np.random.normal(mean1, sd1, n1)
    kelas_B = np.random.normal(mean2, sd2, n2)

    # --- Tampilkan Data ---
    df = pd.DataFrame({
        'Kelas A': kelas_A,
        'Kelas B': kelas_B
    })
    st.write("### 📊 Data Nilai Mahasiswa")
    st.dataframe(df.describe())

    # --- Visualisasi ---
    fig, ax = plt.subplots()
    ax.hist(kelas_A, bins=10, alpha=0.7, label='Kelas A')
    ax.hist(kelas_B, bins=10, alpha=0.7, label='Kelas B')
    ax.legend()
    ax.set_title("Distribusi Nilai Kelas A vs B")
    st.pyplot(fig)

    # --- Uji Hipotesis ---
    st.write("### 🧪 Uji Hipotesis Dua Sampel (t-test)")
    t_stat, p_value = stats.ttest_ind(kelas_A, kelas_B)

    st.write(f"**t-statistik = {t_stat:.3f}**")
    st.write(f"**p-value = {p_value:.4f}**")

    # --- Keputusan ---
    if p_value < alpha:
        st.success(f"Tolak H₀ ✅ — Ada perbedaan signifikan antara Kelas A dan Kelas B (α = {alpha})")
    else:
        st.warning(f"Gagal menolak H₀ ❌ — Tidak ada perbedaan signifikan (α = {alpha})")

    # --- Interpretasi ---
    st.info("""
    **Interpretasi:**
    - Jika `p-value < α` → rata-rata kedua kelas berbeda secara signifikan.
    - Jika `p-value ≥ α` → tidak ada bukti cukup bahwa kedua kelas berbeda.
    """)

    # --- Permainan Mini ---
    st.write("## 🎮 Permainan Statistik: Tebak Hasil Uji!")
    st.write("Sebelum melihat hasil, coba tebak apakah **Kelas A lebih tinggi dari Kelas B**.")
    tebakan = st.radio("Tebakan kamu:", ["A lebih tinggi", "B lebih tinggi", "Sama saja"])

    if st.button("🔍 Cek Tebakan"):
        if mean1 > mean2 and p_value < alpha:
            st.success("Benar! 🎉 Kelas A secara signifikan lebih tinggi.")
        elif mean2 > mean1 and p_value < alpha:
            st.success("Benar! 🎉 Kelas B secara signifikan lebih tinggi.")
        else:
            st.info("Hasilnya tidak signifikan — tidak ada perbedaan berarti.")

    # --- Latihan Interaktif ---
    st.write("## 🧩 Latihan")
    st.write("""
    Tentukan keputusan berdasarkan hasil uji berikut:
    - t-statistik = 2.10  
    - p-value = 0.03  
    - α = 0.05  
    Apakah H₀ ditolak?
    """)
    jawaban = st.radio("Jawaban kamu:", ["Tolak H₀", "Gagal Menolak H₀"])
    if st.button("💡 Cek Jawaban"):
        if jawaban == "Tolak H₀":
            st.success("✅ Benar! Karena p-value < α, maka H₀ ditolak.")
        else:
            st.error("❌ Salah, seharusnya H₀ ditolak karena p-value = 0.03 < 0.05.")

def materi20():
    st.title("📈 Korelasi dan Regresi Linear Interaktif")
    st.write("Pelajari hubungan antar variabel dan prediksi menggunakan regresi linear sederhana.")

    # ----------------------------
    # 🔧 Pengaturan Data
    # ----------------------------
    st.sidebar.header("🔧 Pengaturan Data Simulasi")
    n = st.sidebar.slider("Jumlah data", 10, 200, 50)
    mean_x = st.sidebar.slider("Rata-rata X", 10, 100, 50)
    mean_y = st.sidebar.slider("Rata-rata Y", 10, 100, 50)
    std_x = st.sidebar.slider("Standar deviasi X", 1, 30, 10)
    std_y = st.sidebar.slider("Standar deviasi Y", 1, 30, 10)
    corr_strength = st.sidebar.slider("Kekuatan korelasi (antara -1 dan 1)", -1.0, 1.0, 0.7)

    # ----------------------------
    # 🔢 Generate Data
    # ----------------------------
    np.random.seed(42)
    x = np.random.normal(mean_x, std_x, n)
    y = mean_y + corr_strength * (x - mean_x) + np.random.normal(0, std_y, n)

    df = pd.DataFrame({'X': x, 'Y': y})

    st.write("### 📊 Data Simulasi")
    st.dataframe(df.head())

    # ----------------------------
    # 📈 Visualisasi Scatter Plot
    # ----------------------------
    fig, ax = plt.subplots()
    ax.scatter(df['X'], df['Y'], color='skyblue', edgecolor='k')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Scatter Plot X vs Y")
    st.pyplot(fig)

    # ----------------------------
    # 🔍 Korelasi Pearson & Spearman
    # ----------------------------
    st.write("### 🔗 Korelasi Pearson & Spearman")
    pearson_corr, _ = pearsonr(df['X'], df['Y'])
    spearman_corr, _ = spearmanr(df['X'], df['Y'])

    st.write(f"**Korelasi Pearson (r)** = {pearson_corr:.3f}")
    st.write(f"**Korelasi Spearman (ρ)** = {spearman_corr:.3f}")

    if abs(pearson_corr) >= 0.8:
        st.success("Hubungan **sangat kuat** antara X dan Y.")
    elif abs(pearson_corr) >= 0.6:
        st.info("Hubungan **kuat** antara X dan Y.")
    elif abs(pearson_corr) >= 0.4:
        st.warning("Hubungan **sedang** antara X dan Y.")
    else:
        st.error("Hubungan **lemah atau tidak signifikan** antara X dan Y.")

    # ----------------------------
    # 🤖 Regresi Linear Sederhana
    # ----------------------------
    st.write("### 📉 Regresi Linear Sederhana")
    model = LinearRegression()
    X = df[['X']]
    Y = df['Y']
    model.fit(X, Y)
    a = model.intercept_
    b = model.coef_[0]
    y_pred = model.predict(X)

    st.write(f"Persamaan regresi: ŷ = {a:.2f} + {b:.2f}X")

    # Tampilkan grafik regresi
    fig, ax = plt.subplots()
    ax.scatter(df['X'], df['Y'], label='Data Asli', color='lightblue')
    ax.plot(df['X'], y_pred, color='red', label='Garis Regresi')
    ax.legend()
    st.pyplot(fig)

    # ----------------------------
    # 🎮 Permainan Statistik
    # ----------------------------
    st.write("## 🎮 Permainan: Tebak Arah Hubungan!")
    st.write("Coba tebak hubungan antara X dan Y berdasarkan grafik di atas.")
    tebakan = st.radio("Tebakan kamu:", ["Positif", "Negatif", "Tidak ada hubungan"])

    if st.button("🔍 Cek Tebakan"):
        if pearson_corr > 0.2 and tebakan == "Positif":
            st.success("✅ Benar! Hubungannya positif.")
        elif pearson_corr < -0.2 and tebakan == "Negatif":
            st.success("✅ Benar! Hubungannya negatif.")
        elif abs(pearson_corr) < 0.2 and tebakan == "Tidak ada hubungan":
            st.success("✅ Benar! Tidak ada hubungan kuat antara X dan Y.")
        else:
            st.error("❌ Coba lagi! Lihat kembali arah grafiknya.")

    # ----------------------------
    # 🧩 Latihan
    # ----------------------------
    st.write("## 🧩 Latihan Interaktif")
    st.write("""
    Dari hasil regresi:  
    - ŷ = 10 + 2.5X  
    Hitung prediksi Y jika X = 20
    """)
    jawaban = st.number_input("Masukkan jawaban kamu:", step=0.1)
    if st.button("💡 Cek Jawaban"):
        y_true = 10 + 2.5 * 20
        if abs(jawaban - y_true) < 0.1:
            st.success("🎉 Benar! Nilai prediksi Y = 60.")
        else:
            st.error(f"❌ Salah, seharusnya Y = {y_true:.1f}")

    st.info("""
    **Interpretasi:**
    - Jika nilai X meningkat, nilai Y juga meningkat (hubungan positif).
    - Jika nilai X meningkat tetapi Y menurun, hubungan negatif.
    - Regresi membantu memprediksi nilai Y berdasarkan X.
    """)

def materi21():
    st.title("🧮 Analisis Chi-Square (χ²) Interaktif")
    st.write("""
    Pelajari dan uji secara interaktif:
    1. Uji Kesesuaian (Goodness of Fit)  
    2. Uji Independensi antar variabel  
    """)

    st.markdown("---")

    # Pilih jenis analisis
    menu = st.radio("Pilih jenis analisis:", ["Uji Kesesuaian", "Uji Independensi"])

    # =============================
    # 🎯 1. UJI KESESUAIAN
    # =============================
    if menu == "Uji Kesesuaian":
        st.header("📊 Uji Kesesuaian (Goodness of Fit)")
        st.write("Bandingkan data observasi dengan frekuensi yang diharapkan.")

        kategori = st.text_input("Masukkan kategori (pisahkan dengan koma):", "A,B,C,D,E")
        kategori = [k.strip() for k in kategori.split(",")]

        obs_str = st.text_input("Masukkan frekuensi observasi (pisahkan dengan koma):", "18,22,20,15,25")
        obs = np.array([float(x) for x in obs_str.split(",")])

        exp_choice = st.radio("Tentukan frekuensi harapan:", ["Sama rata", "Kustom"])
        if exp_choice == "Sama rata":
            exp = np.ones_like(obs) * np.mean(obs)
        else:
            exp_str = st.text_input("Masukkan frekuensi harapan (pisahkan dengan koma):", "20,20,20,20,20")
            exp = np.array([float(x) for x in exp_str.split(",")])

        # Hitung chi-square
        chi_stat, p_value = chisquare(f_obs=obs, f_exp=exp)

        st.write(f"**Nilai χ² hitung:** {chi_stat:.3f}")
        st.write(f"**p-value:** {p_value:.4f}")

        if p_value < 0.05:
            st.success("Tolak H₀ ✅ — Data **tidak sesuai** dengan distribusi yang diharapkan.")
        else:
            st.info("Gagal tolak H₀ — Data **sesuai** dengan distribusi yang diharapkan.")

        # Visualisasi
        fig, ax = plt.subplots()
        ax.bar(kategori, obs, color='skyblue', label='Observasi')
        ax.plot(kategori, exp, color='red', marker='o', label='Ekspektasi')
        ax.legend()
        ax.set_title("Perbandingan Frekuensi Observasi vs Ekspektasi")
        st.pyplot(fig)

    # =============================
    # 🎯 2. UJI INDEPENDENSI
    # =============================
    else:
        st.header("🔗 Uji Independensi Antar Variabel")
        st.write("Periksa apakah dua variabel kategorik saling berhubungan.")

        st.subheader("Contoh Kasus: Jenis Kelamin dan Kelulusan")
        data_default = pd.DataFrame({
            "Lulus": [40, 35],
            "Tidak Lulus": [10, 15]
        }, index=["Laki-laki", "Perempuan"])
    
        st.write("Data default:")
        st.dataframe(data_default)

        st.write("Atau masukkan data kustom (opsional):")
        c1 = st.number_input("Laki-laki Lulus:", 0, 200, 40)
        c2 = st.number_input("Laki-laki Tidak Lulus:", 0, 200, 10)
        c3 = st.number_input("Perempuan Lulus:", 0, 200, 35)
        c4 = st.number_input("Perempuan Tidak Lulus:", 0, 200, 15)

        df = pd.DataFrame({
            "Lulus": [c1, c3],
            "Tidak Lulus": [c2, c4]
        }, index=["Laki-laki", "Perempuan"])

        st.write("### 📋 Tabel Kontingensi")
        st.dataframe(df)

        chi2, p, dof, exp = chi2_contingency(df)

        st.write(f"**Nilai χ² hitung:** {chi2:.3f}")
        st.write(f"**p-value:** {p:.4f}")
        st.write(f"**Derajat kebebasan (df):** {dof}")

        if p < 0.05:
            st.success("Tolak H₀ ✅ — Ada hubungan antara kedua variabel.")
        else:
            st.info("Gagal tolak H₀ — Tidak ada hubungan yang signifikan.")

        # Visualisasi
        st.subheader("📊 Visualisasi Data")
        fig, ax = plt.subplots()
        df.plot(kind='bar', ax=ax, color=['skyblue', 'salmon'])
        ax.set_ylabel("Frekuensi")
        ax.set_title("Hubungan Jenis Kelamin dan Kelulusan")
        st.pyplot(fig)

    # =============================
    # 🎲 PERMAINAN INTERAKTIF
    # =============================
    st.markdown("---")
    st.header("🎮 Permainan: Tebak Hasil Uji Chi-Square")
    st.write("Simulasikan hasil dan tebak apakah H₀ akan diterima atau ditolak!")

    sim_choice = st.radio("Pilih jenis uji:", ["Goodness of Fit", "Independensi"])
    n = st.slider("Jumlah kategori / sel data:", 2, 6, 3)
    random_obs = np.random.randint(10, 50, size=n)
    random_exp = np.random.randint(10, 50, size=n)

    if sim_choice == "Goodness of Fit":
        random_exp = random_exp * (random_obs.sum() / random_exp.sum())
        chi_stat, p_value = chisquare(random_obs, random_exp)
    else:
        table = np.random.randint(10, 40, size=(2, n))
        chi_stat, p_value, dof, exp = chi2_contingency(table)

    st.write("### Data Simulasi:")
    if sim_choice == "Goodness of Fit":
        df_sim = pd.DataFrame({"Observasi": random_obs, "Ekspektasi": random_exp})
    else:
        df_sim = pd.DataFrame(table, index=["Grup 1", "Grup 2"])
    st.dataframe(df_sim)

    tebakan = st.radio("Menurut kamu, H₀ akan:", ["Diterima", "Ditolak"])
    if st.button("🔍 Cek Tebakan"):
        if (p_value < 0.05 and tebakan == "Ditolak") or (p_value >= 0.05 and tebakan == "Diterima"):
            st.success(f"✅ Benar! p-value = {p_value:.4f}")
        else:
            st.error(f"❌ Salah! p-value = {p_value:.4f}")

    # =============================
    # 🧩 LATIHAN
    # =============================
    st.markdown("---")
    st.header("🧩 Latihan: Jenis Kelamin vs Kelulusan")
    st.write("""
    Gunakan data berikut dan lakukan analisis uji chi-square:
    - Laki-laki: 40 lulus, 10 tidak lulus  
    - Perempuan: 35 lulus, 15 tidak lulus
    """)

    df_latihan = pd.DataFrame({
        "Lulus": [40, 35],
        "Tidak Lulus": [10, 15]
    }, index=["Laki-laki", "Perempuan"])

    chi2, p, dof, exp = chi2_contingency(df_latihan)
    st.write(f"Nilai χ² = {chi2:.3f}, p-value = {p:.4f}")

    if p < 0.05:
        st.success("✅ Ada hubungan signifikan antara jenis kelamin dan kelulusan.")
    else:
        st.info("ℹ️ Tidak ada hubungan signifikan antara jenis kelamin dan kelulusan.")

    st.info("""
    **Interpretasi:**
    - Jika p < 0.05 → Ada hubungan antar variabel.  
    - Jika p ≥ 0.05 → Tidak ada hubungan yang signifikan.
    """)
    
def materi22():
    # =============================
    # 🎓 JUDUL DAN PENDAHULUAN
    # =============================
    st.title("📊 Statistika Nonparametrik dan Penerapan Komputasi dengan Python")
    st.markdown("""
    ### 🎯 Tujuan Pembelajaran
    Mahasiswa dapat memahami konsep dasar **statistika nonparametrik**, membedakan berbagai **uji nonparametrik populer**,  
    dan menerapkan analisis menggunakan **Python + Streamlit** secara interaktif.

    ---

    ### 🧠 Konsep Dasar
    Statistika nonparametrik digunakan ketika:
    - Data **tidak berdistribusi normal**.
    - Data berskala **ordinal atau nominal**.
    - Ukuran sampel **kecil** atau **tidak memenuhi asumsi parametrik**.

    ---

    ### 🔍 Uji Nonparametrik yang Umum:
    | Uji | Tujuan | Data |
    |------|--------|------|
    | **Wilcoxon Signed-Rank Test** | Membandingkan dua sampel berpasangan | Ordinal / Interval non-normal |
    | **Mann-Whitney U Test** | Membandingkan dua sampel independen | Ordinal / Interval non-normal |
    | **Kruskal-Wallis Test** | Membandingkan lebih dari dua sampel independen | Ordinal / Interval non-normal |
    """)

    st.markdown("---")

    # =============================
    # 📘 MENU MATERI
    # =============================
    menu = st.radio("Pilih Materi atau Uji:", [
        "1️⃣ Pengantar Statistika Nonparametrik",
        "2️⃣ Uji Wilcoxon",
        "3️⃣ Uji Mann-Whitney",
        "4️⃣ Uji Kruskal-Wallis",
        "🧩 Proyek Akhir: Analisis Dataset Nyata"
    ])

    # =============================
    # 1️⃣ PENGANTAR
    # =============================
    if menu == "1️⃣ Pengantar Statistika Nonparametrik":
        st.header("📖 Pengantar Statistika Nonparametrik")
        st.write("""
        Statistika nonparametrik **tidak bergantung pada asumsi distribusi data tertentu** (seperti normalitas).
        Biasanya digunakan untuk:
        - Data berskala **ordinal (peringkat)**.
        - Data yang **tidak simetris**.
        - Situasi di mana ukuran sampel kecil.

        ⚙️ Contoh aplikasi:
        - Menilai **kepuasan mahasiswa** (1–5).
        - Membandingkan **dua metode pembelajaran**.
        - Melihat **perbedaan hasil eksperimen kecil**.
        """)

        st.info("""
        💡 Keunggulan:
        - Tidak perlu uji normalitas.
        - Lebih tahan terhadap pencilan (outlier).
        """)

    # =============================
    # 2️⃣ UJI WILCOXON
    # =============================
    elif menu == "2️⃣ Uji Wilcoxon":
        st.header("🧮 Uji Wilcoxon Signed-Rank Test (Berpasangan)")

        st.write("""
        Digunakan untuk membandingkan **dua kondisi berpasangan**, misalnya:
        - Nilai sebelum dan sesudah pelatihan.
        - Dua metode pada kelompok yang sama.

        **Hipotesis:**
        - H₀: Tidak ada perbedaan median antara dua kondisi.
        - H₁: Ada perbedaan median antara dua kondisi.
        """)

        data1 = st.text_input("Masukkan data 1 (misal sebelum pelatihan):", "50,55,60,58,65,62,70")
        data2 = st.text_input("Masukkan data 2 (misal sesudah pelatihan):", "52,57,61,60,68,64,72")

        x = np.array([float(i) for i in data1.split(",")])
        y = np.array([float(i) for i in data2.split(",")])

        stat, p = wilcoxon(x, y)
        st.write(f"**Nilai Statistik Uji (W):** {stat:.3f}")
        st.write(f"**p-value:** {p:.4f}")

        if p < 0.05:
            st.success("Tolak H₀ ✅ — Ada perbedaan signifikan antara dua kondisi.")
        else:
            st.info("Gagal tolak H₀ — Tidak ada perbedaan signifikan.")

        fig, ax = plt.subplots()
        ax.plot(["Sebelum", "Sesudah"], [np.mean(x), np.mean(y)], marker='o', color='blue')
        ax.set_title("Perbandingan Nilai Rata-rata (Wilcoxon)")
        st.pyplot(fig)

    # =============================
    # 3️⃣ UJI MANN-WHITNEY
    # =============================
    elif menu == "3️⃣ Uji Mann-Whitney":
        st.header("⚖️ Uji Mann-Whitney U (Dua Sampel Independen)")
        st.write("""
        Uji ini membandingkan dua kelompok yang **independen**, tanpa asumsi distribusi normal.
        Misal:
        - Kelompok A (metode konvensional)
        - Kelompok B (metode interaktif)
        """)

        group1 = st.text_input("Masukkan data kelompok 1:", "60,65,70,68,72,75")
        group2 = st.text_input("Masukkan data kelompok 2:", "62,67,74,70,78,80")

        g1 = np.array([float(i) for i in group1.split(",")])
        g2 = np.array([float(i) for i in group2.split(",")])

        stat, p = mannwhitneyu(g1, g2)
        st.write(f"**Nilai U hitung:** {stat:.3f}")
        st.write(f"**p-value:** {p:.4f}")

        if p < 0.05:
            st.success("Tolak H₀ ✅ — Ada perbedaan signifikan antara kedua kelompok.")
        else:
            st.info("Gagal tolak H₀ — Tidak ada perbedaan signifikan.")

        fig, ax = plt.subplots()
        sns.boxplot(data=[g1, g2], ax=ax)
        ax.set_xticklabels(["Kelompok 1", "Kelompok 2"])
        ax.set_title("Visualisasi Mann-Whitney U Test")
        st.pyplot(fig)

    # =============================
    # 4️⃣ UJI KRUSKAL-WALLIS
    # =============================
    elif menu == "4️⃣ Uji Kruskal-Wallis":
        st.header("📈 Uji Kruskal-Wallis H (Tiga atau Lebih Kelompok Independen)")
        st.write("""
        Uji ini digunakan untuk membandingkan **tiga atau lebih kelompok independen**.
        Contoh:
        - Perbandingan nilai antara tiga metode pembelajaran.
        """)

        data_str = st.text_area("Masukkan data untuk tiap kelompok (pisahkan baris):",
        "65,70,72,68,75\n60,63,65,62,67\n72,78,75,80,79")

        groups = [np.array([float(x) for x in line.split(",")]) for line in data_str.strip().split("\n")]
        stat, p = kruskal(*groups)
        st.write(f"**Nilai H hitung:** {stat:.3f}")
        st.write(f"**p-value:** {p:.4f}")

        if p < 0.05:
            st.success("Tolak H₀ ✅ — Ada perbedaan signifikan antara kelompok.")
        else:
            st.info("Gagal tolak H₀ — Tidak ada perbedaan signifikan.")

        fig, ax = plt.subplots()
        sns.boxplot(data=groups, ax=ax)
        ax.set_title("Perbandingan Nilai Antar Kelompok (Kruskal-Wallis)")
        st.pyplot(fig)

    # =============================
    # 🧩 PROYEK AKHIR
    # =============================
    else:
        st.header("📊 Proyek Akhir: Analisis Dataset Nyata")
        st.write("""
        Gunakan dataset nyata (misalnya hasil survei mahasiswa) dan lakukan analisis statistik nonparametrik.
        """)

        uploaded = st.file_uploader("Unggah file CSV (misalnya: survei_mahasiswa.csv)", type=["csv"])
        if uploaded:
            df = pd.read_csv(uploaded)
            st.dataframe(df.head())

            col1 = st.selectbox("Pilih kolom 1:", df.columns)
            col2 = st.selectbox("Pilih kolom 2:", df.columns)

            st.write("📊 Visualisasi Data")
            fig, ax = plt.subplots()
            sns.boxplot(x=df[col1], y=df[col2], ax=ax)
            st.pyplot(fig)

            # Contoh analisis otomatis
            groups = [group[col2].values for name, group in df.groupby(col1)]
            stat, p = kruskal(*groups)
            st.write(f"**Hasil Kruskal-Wallis:** H = {stat:.3f}, p = {p:.4f}")

            if p < 0.05:
                st.success("Tolak H₀ ✅ — Ada perbedaan signifikan antar kelompok.")
            else:
                st.info("Gagal tolak H₀ — Tidak ada perbedaan signifikan.")
        else:
            st.info("Unggah file CSV untuk memulai proyek akhir.")
#=========================================
if st.session_state.kondisi['kondisi1']:
    cover()
if st.session_state.kondisi['kondisi2']:
    materi1()
if st.session_state.kondisi['kondisi3']:
    materi2()
if st.session_state.kondisi['kondisi4']:
    materi3()
if st.session_state.kondisi['kondisi5']:
    materi4()
if st.session_state.kondisi['kondisi6']:
    materi5()
if st.session_state.kondisi['kondisi7']:
    materi6()
if st.session_state.kondisi['kondisi8']:
    materi7()
if st.session_state.kondisi['kondisi9']:
    materi8()
if st.session_state.kondisi['kondisi10']:
    materi9()
if st.session_state.kondisi['kondisi11']:
    materi10()
if st.session_state.kondisi['kondisi12']:
    materi11()
if st.session_state.kondisi['kondisi13']:
    materi12()
if st.session_state.kondisi['kondisi14']:
    materi13()
if st.session_state.kondisi['kondisi15']:
    materi14()
if st.session_state.kondisi['kondisi16']:
    materi15()
if st.session_state.kondisi['kondisi17']:
    materi16()
if st.session_state.kondisi['kondisi18']:
    materi17()
if st.session_state.kondisi['kondisi19']:
    materi18()
if st.session_state.kondisi['kondisi20']:
    materi19()
if st.session_state.kondisi['kondisi21']:
    materi20()
if st.session_state.kondisi['kondisi22']:
    materi21()
if st.session_state.kondisi['kondisi23']:
    materi22()
#=========================================

if st.sidebar.button("Tampilan depan"):
    st.session_state.kondisi = {'kondisi1':True,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False, 'kondisi9':False, 'kondisi10':False,'kondisi11':False,'kondisi12':False, 'kondisi13':False,'kondisi14':False,
                                'kondisi15':False, 'kondisi16':False,'kondisi17':False, 'kondisi18':False, 'kondisi19':False,'kondisi20':False, 'kondisi21':False,
                                'kondisi22':False, 'kondisi23':False}
    
if st.sidebar.button("Pengantar Statistik"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':True,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False, 'kondisi9':False, 'kondisi10':False,'kondisi11':False,'kondisi12':False, 'kondisi13':False,'kondisi14':False,
                                'kondisi15':False, 'kondisi16':False,'kondisi17':False, 'kondisi18':False, 'kondisi19':False,'kondisi20':False, 'kondisi21':False,
                                'kondisi22':False, 'kondisi23':False}
    st.rerun()
if st.sidebar.button("Pengumpulan Data"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':True, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False, 'kondisi9':False, 'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
st.sidebar.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
st.sidebar.markdown("<div id='konsep1'>Penyajian Data dalam Bentuk Tabel dan Diagram</div>",unsafe_allow_html=True)
if st.sidebar.button("Tabel Distribusi Frekuensi"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':True, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False, 'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Batas Data"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':True,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False, 'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False, 'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Gambar Diagram"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':True,'kondisi7':False,
                                'kondisi8':False, 'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
st.sidebar.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
st.sidebar.markdown("<div id='konsep1'>Statistik Deskriptif</div>",unsafe_allow_html=True)
if st.sidebar.button("Pemusatan Data"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':True,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Ukuran Letak Data"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':True,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Ukuran Penyebaran Data"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':True,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
st.sidebar.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
if st.sidebar.button("Analisis Data Kelompok"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':True,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False}
    st.rerun()
if st.sidebar.button("Teori Peluang"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':True,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
st.sidebar.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
st.sidebar.markdown("<div id='konsep1'>Distribusi Peluang Diskrit</div>",unsafe_allow_html=True)
if st.sidebar.button("Distribusi Binomial"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':True,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Distribusi Poisson"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':True,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Ekspektasi"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':True,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
st.sidebar.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
st.sidebar.markdown("<div id='konsep1'>Distribusi Peluang Kontinu</div>",unsafe_allow_html=True)
if st.sidebar.button("Distribusi Normal"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':True,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Z-Score dan Tabel Distribusi Normal"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':True,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Interpretasi Area di Bawah Kurva Normal"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':True,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
st.sidebar.markdown("<hr style='border: 2px solid #888;'>", unsafe_allow_html=True)
if st.sidebar.button("Sampling dan Distribusi Sampling"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':True,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Estimasi Parameter Interaktif"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':True,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Uji Hipotesis Dua Sampel (Kelas A vs Kelas B)"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':True,'kondisi21':False,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Korelasi dan Regresi Linear"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':True,
                                'kondisi22':False,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Analisis Chi-Square (χ²)"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':True,'kondisi23':False}
    st.rerun()
if st.sidebar.button("Statistika Nonparametrik dan Penerapan Komputasi"):
    st.session_state.kondisi = {'kondisi1':False,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False,'kondisi6':False,'kondisi7':False,
                                'kondisi8':False,'kondisi9':False,'kondisi10':False,'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False,
                                'kondisi15':False,'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,'kondisi21':False,
                                'kondisi22':False,'kondisi23':True}
    st.rerun()

