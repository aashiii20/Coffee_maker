import streamlit as st

st.title("Getting Your Coffee Just Right")

col1, col2 = st.columns(2)

with col1:
    st.header("Favorite Coffee Type")
    st.image(
   "https://images.pexels.com/photos/374852/pexels-photo-374852.jpeg", 
    width=140 
)
    coffee_type = st.radio("Select your favorite coffee type:", 
                           ["Espresso", "Latte", "Cappuccino", "Americano", "Mocha"])
    st.write(f"You selected: {coffee_type}")
    
    with col2:
        st.header("Preferred Coffee Size")
        st.image("https://images.pexels.com/photos/32391688/pexels-photo-32391688.jpeg", width=140)
        coffee_size = st.selectbox("Choose your preferred coffee cup size:", 
                                   ["Small", "Medium", "Large", "Extra Large"])
st.write(f"You selected: {coffee_size}")

name = st.text_input("Enter your name to personalize your coffee experience:")
coffee = st.sidebar.selectbox("Select Coffee Type", ["Espresso", "Latte", "Cappuccino", "Americano", "Mocha"])
st.sidebar.write(f"Welcome, {name}! Enjoy your {coffee} ☕")

import streamlit as st

st.header("Master the Brew")

st.markdown("""
### 📖 Instructions:
1. **Grind:** Aim for a medium-coarse texture.
2. **Temperature:** Use water around 93°C.
3. **Bloom:** Wet the grounds and wait 30 seconds.
4. **Pour:** Finish pouring in slow, circular motions.
""")
    
if st.button("Complete Order"):
    st.balloons()
    st.success(f"Excellent choice! Your {coffee_type} is being prepared.")