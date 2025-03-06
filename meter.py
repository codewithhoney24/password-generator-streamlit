import re
import streamlit as st

# Streamlit page styles
st.set_page_config(
    page_title="Password Strength Generator 🔐✅",
    page_icon="🆗 ❎ ✔️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark mode, gradient button, and white text
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: white;
        }
        .stApp {
            background-color: black;
            color: white;
        }
        .stTextInput, .stButton > button {
            color: white;
        }
        .stTextInput input {
            background-color: #222;
            color: white;
            border: 2px solid #ff0080;
        }
        .stButton > button {
            background: linear-gradient(45deg, #ff0080, #8000ff);
            color: white;
            border-radius: 8px;
            border: 2px solid white;
            font-size: 18px;
            padding: 10px;
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, #8000ff, #ff0080);
            color: white;
        }
        .stExpander {
            background-color: #222;
            border: 2px solid #ff0080;
            color: white;
        }
        .stSidebar {
            background-color: #111;
            color: white;
        }

        label {
            color: white !important;
            font-size: 18px;
            font-weight: bold;
        }
        .stTextInput input {
            background-color: #222;
            color: white;
            border: 2px solid #ff0080;
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar for How to Use Password Section
st.sidebar.header("How to Use Password 🔑")
st.sidebar.write("""
1. **Length Matters**: Make sure your password is at least 8 characters long.
2. **Uppercase & Lowercase**: Use a combination of both uppercase and lowercase letters.
3. **Include Numbers**: Add at least one number to increase the strength.
4. **Use Special Characters**: Incorporate symbols like !, @, #, $, etc.
5. **Avoid Common Words**: Don’t use easily guessable words like your name or 'password123'.
6. **Password Uniqueness**: Avoid reusing passwords across different accounts.
7. **Use a Password Manager**: Consider using a password manager for better security and convenience.
""")

# Sidebar for Password Safety & Protection
st.sidebar.header("HOW TO STAY SAFE & PROTECT YOUR PASSWORD 🔒")
st.sidebar.write("""
1. **Use Two-Factor Authentication (2FA)**: Enable 2FA for extra security.
2. **Never Share Your Password**: Keep your password private.
3. **Update Passwords Regularly**: Change your passwords every few months.
4. **Avoid Public Wi-Fi**: Don’t enter passwords on public networks.
5. **Check for Data Breaches**: Use tools like Have I Been Pwned.
6. **Use Unique Passwords**: Never reuse passwords.
7. **Store Passwords Securely**: Use a trusted password manager.
""")

st.title("🔐 Password Strength  Generator")
st.write("Enter your password below to check its security level 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long!**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **uppercase and lowercase letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*(),.?':{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*(),.?':{}|<>)**.")

    if score == 4:
        st.success("✅ **Strong Password** Your password is secure.")
    elif score == 3:
        st.warning("⚠️ **Moderate Password** Your password is okay but could be better.")
    else:
        st.error("❌ **Weak Password** Follow the suggestions below.")

    if feedback:
        with st.expander("🔢 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# User Input
password = st.text_input("Enter your password :", type="password", help="Ensure your password is strong 🔐")

if st.button("Check Password"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter your password first!")
