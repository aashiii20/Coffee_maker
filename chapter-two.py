import streamlit as st

st.title("Choose your mood. We'll brew the magic ☕")
if st.button("Make Coffee"):
    st.success("Your coffee is being brewed!")

add_coffee = st.checkbox("Add Coffee")
if add_coffee:
    st.write("Extra coffee added to your brew!")
    
    coffee_type = st.radio("Select Coffee Type", ["Espresso", "Latte", 
                                               "Cappuccino", "Americano", "Mocha"])
    st.write(f"You selected: {coffee_type}")
    flavour = st.selectbox("Choose a flavour", ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Irish Cream"])
    st.write(f"Flavour added: {flavour}")
    
    sugar = st.slider("Select sugar level (spoons)", 0, 5, 1)
    st.write(f"Sugar level: {sugar} spoon(s)") 
    
    cups = st.number_input("Number of cups", min_value=1, max_value=10, value=1)
    st.write(f"Number of cups: {cups}")
    
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! Your coffee will be ready soon.")

  