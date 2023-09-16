# Review mandiri adalah proses Anda memastikan semua checklist submission sudah terpenuhi. Pastikan Anda mencentang semua checklist yang tersedia.
# 1. Memastikan seluruh ketentuan pengiriman submission
# 2. Menggunakan salah satu dari dataset yang telah disediakan
# 3. Melakukan seluruh proses analisis data
# 4. Proses analisis dibuat dalam notebook yang rapi
# 5. Membuat dashboard sederhana menggunakan streamlit

# Data Balita dan Keluarga Resiko Stunting Kota Medan 📈
# Dataset ini memiliki variabel, antara lain kolom:
# 1) id
# 2) nama_kecamatan
# 3) nama_puskesmas
# 4) id_desa_bps
# 5) id_desa_dagri
# 6) nama_desa
# 7) jumlah_keluarga
# 8) jumlah_keluarga_beresiko_stunting
# 9) jumlah_balita
# 10) jumlah_balita_sangat_pendek
# 11) jumlah_balita_pendek

# Melakukan import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Dataframe awal 
data = pd.read_csv('https://raw.githubusercontent.com/darman1725/Dicoding-Project/master/Belajar_Analisis_Dengan_Python/data_stunting.csv')

# Nama Halaman
st.set_page_config(
    page_title="Dashboard Data Balita dan Keluarga Resiko Stunting Kota Medan",
    page_icon=":chart_with_upwards_trend:"
)

#Sidebar
with st.sidebar:
    # Menambahkan logo instansi
    st.image("https://raw.githubusercontent.com/darman1725/Dicoding-Project/master/Belajar_Analisis_Dengan_Python/dinas_medan.png")
    
    st.sidebar.header('Filter Data')
    # Buat opsi "Semua Kecamatan"
    selected_kecamatan = st.sidebar.selectbox('Pilih Kecamatan', ['Semua Kecamatan'] + list(data['nama_kecamatan'].unique()))
    
    # Buat opsi "Semua Puskesmas" berdasarkan pilihan kecamatan
    if selected_kecamatan == 'Semua Kecamatan':
        selected_puskesmas = st.sidebar.selectbox('Pilih Puskesmas', ['Semua Puskesmas'])
    else:
        selected_puskesmas = st.sidebar.selectbox('Pilih Puskesmas', ['Semua Puskesmas'] + list(data[data['nama_kecamatan'] == selected_kecamatan]['nama_puskesmas'].unique()))
        
    # Filter data berdasarkan pilihan pengguna
    if selected_kecamatan == 'Semua Kecamatan' and selected_puskesmas == 'Semua Puskesmas':
        filtered_data = data  # Menampilkan semua data jika keduanya dipilih
    elif selected_kecamatan == 'Semua Kecamatan':
        filtered_data = data[data['nama_puskesmas'] == selected_puskesmas]  # Filter berdasarkan puskesmas saja
    elif selected_puskesmas == 'Semua Puskesmas':
        filtered_data = data[data['nama_kecamatan'] == selected_kecamatan]  # Filter berdasarkan kecamatan saja
    else:
        filtered_data = data[(data['nama_kecamatan'] == selected_kecamatan) & (data['nama_puskesmas'] == selected_puskesmas)]  # Filter berdasarkan keduanya

# Menu di navbar
menu = st.selectbox(
    'Menu',
    ['Beranda', 'Visualisasi Data', 'Tentang Kami']
)

# Tampilkan data yang sudah difilter
if menu == 'Beranda':
    st.header('Selayang Pandang : Problematika Kasus Stunting Di Indonesia')
    # Gambar atau video
    st.video('https://youtu.be/nfOSXA1NmWw')

    st.markdown("""
    Dalam video ini, Presiden Joko Widodo menyampaikan kekecewaannya terhadap penggunaan anggaran stunting yang tidak sesuai dengan tujuannya. 
    Ia mengungkapkan bahwa anggaran stunting telah habis untuk rapat dan Perdinas (Peraturan Menteri Dalam Negeri), padahal seharusnya digunakan untuk program-program pencegahan dan penanggulangan stunting.

    Video ini menunjukkan pentingnya penggunaan data yang tepat dalam upaya pencegahan dan penanggulangan stunting. 
    Dashboard Data Balita dan Keluarga Resiko Stunting yang dikembangkan dapat menjadi contoh untuk membantu pemerintah dan masyarakat dalam menggunakan anggaran stunting secara lebih efektif.

    Data yang digunakan dalam dashboard adalah data yang sangat penting untuk memahami situasi stunting. 
    Contoh yang diambil dalam studi kasus ini adalah ibukota dari provinsi Sumatera Utara, yaitu Kota Medan. 
    Data ini dapat digunakan untuk menjawab pertanyaan-pertanyaan penting, seperti:

    * Berapa banyak balita dan keluarga berisiko stunting di Kota Medan?
    * Desa mana saja yang memiliki risiko stunting tinggi?

    Dengan menjawab pertanyaan-pertanyaan ini, pemerintah dan masyarakat dapat menyusun program-program pencegahan dan penanggulangan stunting yang lebih tepat sasaran.""")

elif menu == 'Visualisasi Data':
    st.header('Dashboard Data Balita dan Keluarga Resiko Stunting Kota Medan📈')

    # Kolom 1
    col1, col2, col3 = st.columns(3)

    with col1:
        # Hitung jumlah keluarga
        total_keluarga = filtered_data['jumlah_keluarga'].sum()
        st.write(f"Kecamatan: {selected_kecamatan}")
        st.metric("Total keluarga", value=total_keluarga)

    with col2:
        # Hitung jumlah keluarga berisiko stunting
        total_desa = filtered_data['nama_desa'].nunique()
        st.write("Jumlah desa:", total_desa)
        total_keluarga_beresiko_stunting = filtered_data['jumlah_keluarga_beresiko_stunting'].sum()
        st.metric("Jumlah keluarga berisiko stunting", value=total_keluarga_beresiko_stunting)

    with col3:
        # Hitung jumlah bayi
        total_bayi = filtered_data['jumlah_balita'].sum()
        st.write(f"Puskesmas: {selected_puskesmas}")
        st.metric("Total bayi", value=total_bayi)
        
    # Visualisasi 1: Grafik Batang (Bar Chart) jumlah keluarga berisiko stunting per kecamatan atau desa (vertikal)
    fig1, ax1 = plt.subplots()

    if selected_kecamatan == 'Semua Kecamatan' and selected_puskesmas == 'Semua Puskesmas':
        # Saat memilih "Semua Kecamatan" dan "Semua Puskesmas", tampilkan per kecamatan
        sns.barplot(x='jumlah_keluarga_beresiko_stunting', y='nama_kecamatan', data=filtered_data, estimator=sum, ci=None)
        plt.xlabel('Jumlah Keluarga Berisiko Stunting')
        plt.ylabel('Kecamatan')
        plt.title('Jumlah Keluarga Berisiko Stunting per Kecamatan')
    else:
        # Saat memilih kecamatan dan puskesmas tertentu, tampilkan per desa
        sns.barplot(x='jumlah_keluarga_beresiko_stunting', y='nama_desa', data=filtered_data)
        plt.xlabel('Jumlah Keluarga Berisiko Stunting')
        plt.ylabel('Desa')
        plt.title('Jumlah Keluarga Berisiko Stunting per Desa')

    # Tambahkan jumlah di sebelah kanan batang
    for i in ax1.patches:
        # Ubah angka desimal menjadi bilangan bulat
        value = int(i.get_width())
        ax1.annotate(str(value), (i.get_width(), i.get_y() + i.get_height() / 2), va='center', ha='left')

    st.pyplot(fig1)

    # Visualisasi 2 : kecamatan, puskesmas, atau desa terbanyak dan terdikit pengidap stunting
    st.subheader("Informasi Geografis Pengidap Stunting Di Kota Medan")
    st.write(f"Data Kecamatan: {selected_kecamatan} dan Puskesmas: {selected_puskesmas}")

    # Buat palet warna untuk 5 terbanyak (biru) dan 5 terdikit (abu-abu)
    colors_top = ["#90CAF9"] * 5
    colors_bottom = ["#D3D3D3"] * 5

    # Buat plot bar untuk 5 terbanyak dan 5 terdikit dalam satu frame
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))

    if selected_kecamatan == 'Semua Kecamatan' and selected_puskesmas == 'Semua Puskesmas':
        # Saat memilih semua kecamatan dan semua puskesmas, tampilkan data 5 kecamatan teratas dan terbawah
        top5_data = data.groupby('nama_kecamatan')['jumlah_keluarga_beresiko_stunting'].sum().sort_values(ascending=False).head(5)
        bottom5_data = data.groupby('nama_kecamatan')['jumlah_keluarga_beresiko_stunting'].sum().sort_values().head(5)
        title_top = "Kecamatan Jumlah Pengidap Stunting Terbesar"
        title_bottom = "Kecamatan Jumlah Pengidap Stunting Terkecil"
    elif selected_kecamatan != 'Semua Kecamatan' and selected_puskesmas == 'Semua Puskesmas':
        # Saat memilih salah satu kecamatan, tampilkan data 5 puskesmas teratas dan terbawah dalam kecamatan tersebut
        top5_data = filtered_data.groupby('nama_puskesmas')['jumlah_keluarga_beresiko_stunting'].sum().sort_values(ascending=False).head(5)
        bottom5_data = filtered_data.groupby('nama_puskesmas')['jumlah_keluarga_beresiko_stunting'].sum().sort_values().head(5)
        title_top = "Puskesmas Jumlah Pengidap Stunting Terbesar"
        title_bottom = "Puskesmas Jumlah Pengidap Stunting Terkecil"
    elif selected_kecamatan != 'Semua Kecamatan' and selected_puskesmas != 'Semua Puskesmas':
        # Saat memilih salah satu kecamatan dan salah satu puskesmas, tampilkan data 5 desa teratas dan terbawah dalam puskesmas tersebut
        top5_data = filtered_data.groupby('nama_desa')['jumlah_keluarga_beresiko_stunting'].sum().sort_values(ascending=False).head(5)
        bottom5_data = filtered_data.groupby('nama_desa')['jumlah_keluarga_beresiko_stunting'].sum().sort_values().head(5)
        title_top = "Desa Jumlah Pengidap Stunting Terbesar"
        title_bottom = "Desa Jumlah Pengidap Stunting Terkecil"

    sns.barplot(x=top5_data.values, y=top5_data.index, palette=colors_top, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Jumlah Kasus Stunting", fontsize=12)
    ax[0].set_title(title_top, loc="center", fontsize=15)
    ax[0].tick_params(axis='y', labelsize=12)
    ax[0].tick_params(axis='x', labelsize=12)

    sns.barplot(x=bottom5_data.values, y=bottom5_data.index, palette=colors_bottom, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Jumlah Kasus Stunting", fontsize=12)
    ax[1].set_title(title_bottom, loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)
    ax[1].tick_params(axis='x', labelsize=12)

    # Tampilkan plot dalam satu container
    st.pyplot(fig)
    
    # Visualisasi 3
    st.subheader('Persentase Jumlah Keluarga Berisiko Stunting vs Tidak Berisiko Stunting')
    st.write(f"Data Kecamatan: {selected_kecamatan} dan Puskesmas: {selected_puskesmas}")

    # Hitung jumlah keluarga yang berisiko stunting dan tidak
    total_keluarga_beresiko_stunting = filtered_data['jumlah_keluarga_beresiko_stunting'].sum()
    total_keluarga_tidak_beresiko_stunting = total_keluarga - total_keluarga_beresiko_stunting
     
    # Data untuk pie chart
    pie_data = [total_keluarga_beresiko_stunting, total_keluarga_tidak_beresiko_stunting]
    labels = ['Berisiko Stunting', 'Tidak Berisiko Stunting']

    # Hitung presentase keluarga berisiko stunting terhadap tingkat nasional
    presentase_berisiko_stunting = (total_keluarga_beresiko_stunting / total_keluarga) * 100
    tingkat_nasional = 19.1  # Tingkat nasional yang sudah ditentukan

    # Buat pie chart
    fig2, ax2 = plt.subplots()
    ax2.pie(pie_data, labels=labels, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Mengatur aspek rasio menjadi sama

    # Tampilkan pie chart
    st.pyplot(fig2)

    # Tambahkan peringatan berdasarkan perbandingan dengan tingkat nasional
    st.markdown("""  
    Berdasarkan hasil Pemutakhiran Data Keluarga Indonesia tahun 2022, terdapat 13.511.649 keluarga berisiko stunting. Jumlah ini merupakan bagian dari 71.334.664 total jumlah seluruh keluarga di Indonesia.
    Jadi, sekitar 19,1% keluarga di Indonesia berisiko stunting. Dan sekitar sekitar 79,9% keluarga di Indonesia tidak berisiko stunting.
    Sumber data diperoleh dari Website Keluarga Indonesia. 
    """)

    if presentase_berisiko_stunting > tingkat_nasional:
        st.warning("Dari informasi data diatas, Presentase keluarga berisiko stunting lebih tinggi dari tingkat nasional. Status : Perlu tindakan penanganan khusus.")
    else:
        st.info("Dari informasi data diatas, Presentase keluarga berisiko stunting lebih rendah dari tingkat nasional. Status : Tetap dalam pemantauan.")

    # Histogram untuk balita pendek
    plt.hist(data['jumlah_balita_pendek'], bins=20, color='blue', alpha=0.7, label='Balita Pendek')
    plt.hist(data['jumlah_balita_sangat_pendek'], bins=20, color='red', alpha=0.7, label='Balita Sangat Pendek')
    plt.xlabel('Jumlah Balita')
    plt.ylabel('Frekuensi')
    plt.legend()
    plt.title('Distribusi Balita Pendek dan Sangat Pendek')
    plt.show()

    # Box plot untuk balita pendek dan sangat pendek
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data[['jumlah_balita_pendek', 'jumlah_balita_sangat_pendek']], palette=['blue', 'red'])
    plt.ylabel('Jumlah Balita')
    plt.title('Box Plot Balita Pendek dan Sangat Pendek')
    plt.show()

    # Bar plot per kecamatan atau puskesmas
    plt.figure(figsize=(12, 6))
    sns.barplot(x='nama_kecamatan', y='jumlah_balita_pendek', data=data, color='blue', alpha=0.7, label='Balita Pendek')
    sns.barplot(x='nama_kecamatan', y='jumlah_balita_sangat_pendek', data=data, color='red', alpha=0.7, label='Balita Sangat Pendek')
    plt.xlabel('Kecamatan')
    plt.ylabel('Jumlah Balita')
    plt.xticks(rotation=90)
    plt.legend()
    plt.title('Perbandingan Balita Pendek dan Sangat Pendek per Kecamatan')
    plt.show()

    # Scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(data['jumlah_balita_pendek'], data['jumlah_balita_sangat_pendek'], alpha=0.5)
    plt.xlabel('Balita Pendek')
    plt.ylabel('Balita Sangat Pendek')
    plt.title('Scatter Plot Balita Pendek vs Balita Sangat Pendek')
    plt.show()

    # Hitung jumlah balita pendek dan balita sangat pendek
    total_balita_pendek = filtered_data['jumlah_balita_pendek'].sum()
    total_balita_sangat_pendek = filtered_data['jumlah_balita_sangat_pendek'].sum()

    # Data untuk bar chart
    data_balita = {
        'Jenis Balita': ['Balita Pendek', 'Balita Sangat Pendek'],
        'Jumlah': [total_balita_pendek, total_balita_sangat_pendek]
    }

    # Konversi data menjadi DataFrame
    df_balita = pd.DataFrame(data_balita)

    # Buat bar chart menggunakan Seaborn
    fig3, ax3 = plt.subplots()
    sns.barplot(x='Jenis Balita', y='Jumlah', data=df_balita, ax=ax3)

    # Tambahkan label sumbu dan judul
    ax3.set_ylabel('Jumlah Balita')
    ax3.set_title('Jumlah Balita Pendek dan Balita Sangat Pendek')

    # Annotate jumlah di atas batang
    for i in ax3.patches:
        value = int(i.get_height())
        ax3.annotate(str(value), (i.get_x() + i.get_width() / 2, i.get_height()), ha='center', va='bottom')

    # Tampilkan bar chart
    st.pyplot(fig3)

elif menu == 'Tentang Kami':
    st.header('Tentang Kami')
    
    st.markdown("""
    **Dashboard Data Balita dan Keluarga Resiko Stunting Kota Medan**

    Dashboard ini dibuat oleh saya, Darman Saputra Saragih. Saya memiliki minat dan bakat dalam dunia menganalisis data serta menyajikannya ke publik.
    
    **Tujuan Dashboard Ini:**
    - Menyediakan informasi yang berguna tentang stunting di Kota Medan.
    - Membantu pemahaman situasi stunting di wilayah ini.
    - Memberikan status terkini terkait penanganan.

    **Sumber Data:**
    Data yang digunakan dalam dashboard ini diperoleh dari Dinas Pemberdayaan Perempuan, Perlindungan Anak dan Pemberdayaan Masyarakat dan Pengendalian Penduduk dan Keluarga Berencana.
    Alamat : Jl. Jenderal Besar A.H. Nasution No.17 Kel. Pangkalan Masyhur Kec. Medan Johor 20143 Sumatera Utara. Data terakhir diupdate : January 10, 2023, 9:54 AM (UTC+07:00).

    **Kontak Saya:**
    Jika Anda memiliki pertanyaan atau umpan balik, silakan hubungi saya melalui kontak berikut:
    - WhatsApp: 082196360193
    - Instagram: @darman_saragih1701
    - Linkedin: https://www.linkedin.com/in/darman-saputra-saragih/
    """)

