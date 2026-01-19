import streamlit as st

st.title("Brew Bean Diaries ☕")
st.subheader("Brewed to Perfection")
st.text("Your one-stop app for all things coffee!")
st.write("Choose your favorite coffee type.")
coffee = st.selectbox("Select Coffee Type", ["Espresso", "Latte", 
                                    "Cappuccino", "Americano", "Mocha"])
st.write(f"Enjoy your {coffee}. Excellent choice ☕")


