import streamlit as st
import pyotp

def generate_totp_token(secret):
    # Create a TOTP object with the given secret
    totp = pyotp.TOTP(secret)

    # Generate the current TOTP token
    token = totp.now()

    return token

# Judul aplikasi
st.title('Generate TOTP Token  Sederhana Saja')

# Input untuk memasukkan secret key
secret_key = st.text_input('Masukkan Secret Key')

# Tombol untuk menghasilkan token TOTP
if st.button('Generate TOTP'):
    if secret_key:
        # Memanggil fungsi generate_totp_token dengan secret_key yang dimasukkan pengguna
        token = generate_totp_token(secret_key)
        st.success(f'Generated TOTP token: {token}')
    else:
        st.error('Masukkan secret key dengan benar')

