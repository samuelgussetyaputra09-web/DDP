import streamlit as st
from datetime import datetime

# menambah transaksi
def add_transaction(amount, description, transaction_type):
    if amount <= 0:
        st.error("Jumlah harus lebih besar dari 0!")
        return False
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount,
        "description": description,
        "type": transaction_type  # "income" atau "expense"
    }
    if "transactions" not in st.session_state:
        st.session_state.transactions = []
    st.session_state.transactions.append(transaction)
    return True

# Hitung saldo total
def get_balance():
    if "transactions" not in st.session_state:
        return 0
    balance = 0
    for t in st.session_state.transactions:  # Looping 
        if t["type"] == "income":
            balance += t["amount"]
        elif t["type"] == "expense":
            balance -= t["amount"]
    return balance

# total pemasukan
def get_total_income():
    if "transactions" not in st.session_state:
        return 0
    total = 0
    for t in st.session_state.transactions:  # Looping
        if t["type"] == "income":
            total += t["amount"]
    return total

# total pengeluaran
def get_total_expense():
    if "transactions" not in st.session_state:
        return 0
    total = 0
    for t in st.session_state.transactions:  # Looping
        if t["type"] == "expense":
            total += t["amount"]
    return total