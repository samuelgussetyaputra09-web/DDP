import streamlit as st
from utils import add_transaction, get_balance, get_total_income, get_total_expense
import plotly.graph_objects as go
import random  # Untuk tips acak

# mode gelap
def apply_theme(is_dark):
    if is_dark:
        st.markdown("""
        <style>
        /* Background utama - pastikan tidak menyembunyikan konten */
        body, .main, .stApp { background-color: #121212 !important; color: #ffffff !important; }
        
        /* Sidebar */
        .stSidebar { background-color: #1e1e1e !important; color: #ffffff !important; }
        .stSidebar .stSelectbox label, .stSidebar .stToggle label { color: #ffffff !important; }
        .stSidebar .stSelectbox div[data-baseweb="select"], .stSidebar .stToggle div { background-color: #333 !important; color: #ffffff !important; }
        
        /* Input dan form - pastikan input terlihat */
        .stTextInput input, .stNumberInput input, .stTextArea textarea { background-color: #333 !important; color: #ffffff !important; border: 1px solid #555 !important; }
        .stTextInput label, .stNumberInput label, .stTextArea label { color: #ffffff !important; }
        
        /* Button */
        .stButton button { background-color: #4CAF50 !important; color: #ffffff !important; border: none !important; }
        .stButton button:hover { background-color: #45a049 !important; }
        
        /* Metric dan kartu */
        .metric-card { background: linear-gradient(135deg, #333, #555) !important; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.3); transition: transform 0.2s; color: #ffffff !important; }
        .metric-card:hover { transform: scale(1.05); }
        .metric-card h4, .metric-card p { color: #ffffff !important; }  /* Pastikan teks kartu terlihat */
        
        /* Tab dan konten */
        .tab-content { background: #1e1e1e !important; padding: 20px; border-radius: 10px; color: #ffffff !important; }
        .stTabs [data-baseweb="tab-list"] { background-color: #1e1e1e !important; }
        .stTabs [data-baseweb="tab"] { color: #ffffff !important; }
        .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #333 !important; color: #ffffff !important; }
        
        /* Progress bar dan slider */
        .stProgress .st-bo { background-color: #4CAF50 !important; }
        .stSlider .st-bs { background-color: #333 !important; color: #ffffff !important; }
        .stSlider label { color: #ffffff !important; }
        
        /* Alert dan info - pastikan teks terlihat */
        .stAlert, .stInfo, .stError, .stSuccess { background-color: #333 !important; color: #ffffff !important; border-left: 5px solid #4CAF50 !important; }
        
        /* Header, subheader, dan teks umum - kunci agar tidak hilang */
        h1, h2, h3, h4, h5, h6, p, .stMarkdown, .stHeader, .stSubheader, .stCaption { color: #ffffff !important; }
        .stMarkdown div, .stHeader div, .stSubheader div { color: #ffffff !important; }  /* Fallback untuk nested elements */
        
        /* Elemen lain yang mungkin hilang */
        .stContainer, .stColumns, .stExpander { color: #ffffff !important; }
        .stExpander summary { color: #ffffff !important; }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        /* Reset ke mode terang - pastikan semua kembali normal */
        body, .main, .stApp { background-color: #f5f5f5 !important; color: #000000 !important; }
        .stSidebar { background-color: #ffffff !important; color: #000000 !important; }
        .stTextInput input, .stNumberInput input, .stTextArea textarea { background-color: #ffffff !important; color: #000000 !important; border: 1px solid #ccc !important; }
        .stButton button { background-color: #4CAF50 !important; color: #ffffff !important; }
        .metric-card { background: linear-gradient(135deg, #ffffff, #e0e0e0) !important; color: #000000 !important; }
        .metric-card h4, .metric-card p { color: #000000 !important; }
        .tab-content { background: #ffffff !important; color: #000000 !important; }
        .stAlert, .stInfo, .stError, .stSuccess { background-color: #ffffff !important; color: #000000 !important; }
        h1, h2, h3, h4, h5, h6, p, .stMarkdown, .stHeader, .stSubheader, .stCaption { color: #000000 !important; }
        .stMarkdown div, .stHeader div, .stSubheader div { color: #000000 !important; }
        .stContainer, .stColumns, .stExpander { color: #000000 !important; }
        .stExpander summary { color: #000000 !important; }
        </style>
        """, unsafe_allow_html=True)

# Toggle tema di sidebar
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
dark_mode = st.sidebar.toggle("🌙 Mode Gelap", value=st.session_state.dark_mode)
st.session_state.dark_mode = dark_mode
apply_theme(dark_mode)

# Judul aplikasi
st.title("💰 Catatan Keuangan Harian")

# Navigasi sidebar untuk 4 halaman
pages = ["Dashboard", "Tambah Pemasukan", "Tambah Pengeluaran", "Riwayat Transaksi"]
page = st.sidebar.selectbox("Pilih Halaman", pages)

# Halaman 1: Dashboard (Ringkasan) - Diperbarui untuk lebih menarik
if page == "Dashboard":
    st.header("📊 Dashboard Keuangan Anda")
    st.markdown("Pantau dan kelola keuangan harian Anda dengan visual yang menarik dan interaktif!")
    
    balance = get_balance()
    income = get_total_income()
    expense = get_total_expense()
    total_transactions = len(st.session_state.get("transactions", []))
    
    # Tab untuk membagi konten
    tab1, tab2, tab3 = st.tabs(["📈 Ringkasan", "📊 Grafik & Analisis", "💡 Tips Keuangan"])
    
    with tab1:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.subheader("Ringkasan Keuangan")
        
        # Layout kolom untuk kartu metrik
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h4>💰 Saldo Total</h4>
                <p>Rp {balance:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h4>📈 Total Pemasukan</h4>
                <p>Rp {income:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h4>📉 Total Pengeluaran</h4>
                <p>Rp {expense:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h4>📝 Jumlah Transaksi</h4>
                <p>{total_transactions}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Input target tabungan dengan slider
        st.subheader("🎯 Target Tabungan Bulanan")
        target = st.slider("Atur Target (Rp)", min_value=0, max_value=10000000, value=1000000, step=50000)
        progress = min(balance / target, 1.0) if target > 0 else 0
        st.progress(progress)
        st.write(f"Progress: {progress*100:.1f}% tercapai.")
        if progress >= 1.0:
            st.success("🎉 Selamat! Target tercapai!")
            st.balloons()
        elif progress > 0.5:
            st.info("🔥 Hampir tercapai! Terus jaga!")
        
        # Status keuangan dengan logika if dan animasi
        if balance < 0:
            st.error("⚠️ Saldo negatif! Waktunya review pengeluaran. 💸")
        elif balance == 0:
            st.info("😐 Saldo nol. Mulai tambah pemasukan! 🚀")
        else:
            st.success("🎉 Keuangan sehat! Jaga pola ini. 👍")
            if dark_mode:
                st.snow()  # Efek salju untuk tema gelap saat positif
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.subheader("Grafik & Analisis")
        if income > 0 or expense > 0:
            # Pie chart dengan donut style
            fig_pie = go.Figure(data=[go.Pie(
                labels=['Pemasukan', 'Pengeluaran'],
                values=[income, expense],
                hole=0.4,  # Donut style
                marker_colors=['#4CAF50', '#F44336']
            )])
            fig_pie.update_layout(title="Distribusi Keuangan (Donut)", showlegend=True)
            st.plotly_chart(fig_pie)
            
            # Bar chart untuk tren (dummy data; bisa diperluas)
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
            income_trend = [income * random.uniform(0.8, 1.2) for _ in months]  # Dummy
            expense_trend = [expense * random.uniform(0.8, 1.2) for _ in months]
            fig_bar = go.Figure()
            fig_bar.add_trace(go.Bar(x=months, y=income_trend, name='Pemasukan', marker_color='#4CAF50'))
            fig_bar.add_trace(go.Bar(x=months, y=expense_trend, name='Pengeluaran', marker_color='#F44336'))
            fig_bar.update_layout(title="Tren Bulanan (Dummy)", barmode='group')
            st.plotly_chart(fig_bar)
        else:
            st.info("Belum ada data. Tambahkan transaksi untuk grafik! 📈")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.subheader("Tips Keuangan Personalized")
        tips = {
            "negative": ["Kurangi pengeluaran impulsif!", "Buat anggaran mingguan.", "Cari sumber pemasukan tambahan."],
            "zero": ["Mulai catat semua pengeluaran.", "Set target kecil dulu.", "Pelajari investasi dasar."],
            "positive": ["Simpan 20% dari pemasukan.", "Investasikan surplus.", "Rayakan pencapaian kecil!"]
        }
        if balance < 0:
            tip_category = "negative"
        elif balance == 0:
            tip_category = "zero"
        else:
            tip_category = "positive"
        random_tip = random.choice(tips[tip_category])
        st.info(f"💡 Tip: {random_tip}")
        st.markdown('</div>', unsafe_allow_html=True)

# Halaman 2: Tambah Pemasukan
elif page == "Tambah Pemasukan":
    st.header("Tambah Pemasukan")
    with st.form("income_form"):
        amount = st.number_input("Jumlah (Rp)", min_value=0.0, step=1000.0)
        description = st.text_input("Deskripsi")
        submitted = st.form_submit_button("Tambah Pemasukan")
        if submitted:
            if add_transaction(amount, description, "income"):  # Panggil function
                st.success("Pemasukan berhasil ditambahkan!")

# Halaman 3: Tambah Pengeluaran
elif page == "Tambah Pengeluaran":
    st.header("Tambah Pengeluaran")
    with st.form("expense_form"):
        amount = st.number_input("Jumlah (Rp)", min_value=0.0, step=1000.0)
        description = st.text_input("Deskripsi")
        submitted = st.form_submit_button("Tambah Pengeluaran")
        if submitted:
            if add_transaction(amount, description, "expense"):  # Panggil function
                st.success("Pengeluaran berhasil ditambahkan!")

# Halaman 4: Riwayat Transaksi
elif page == "Riwayat Transaksi":
    st.header("Riwayat Transaksi")
    if "transactions" in st.session_state and st.session_state.transactions:
        st.subheader("Daftar Transaksi")
        for i, t in enumerate(st.session_state.transactions):  # Looping untuk menampilkan daftar
            st.write(f"{i+1}. {t['date']} - {t['type'].capitalize()}: Rp {t['amount']:,.0f} - {t['description']}")
    else:
        st.info("Belum ada transaksi.")
    
    # Opsi untuk menghapus semua transaksi (opsional)
    if st.button("Hapus Semua Transaksi"):
        if "transactions" in st.session_state:
            st.session_state.transactions = []
            st.success("Semua transaksi dihapus!")
