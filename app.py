#import streamlit as st

# Page title
#st.title("🛒 Smart Grocery List")

# Create storage if it doesn't exist
#if "items" not in st.session_state:
#    st.session_state["items"] = []
#
# Input box
#item = st.text_input("Enter grocery item")

# Add button
#if st.button("Add Item"):
#    if item.strip():
#        st.session_state["items"].append(item)

# Display items
#st.subheader("Current List")

#for grocery_item in st.session_state["items"]:
#    st.write("✅", grocery_item)



import streamlit as st

st.title("🛒 Smart Grocery List")

if "items" not in st.session_state:
    st.session_state["items"] = []

item = st.text_input("Enter grocery item")

if st.button("Add Item"):
    if item.strip():
        st.session_state["items"].append(item)

st.subheader("My Grocery List")

for index, grocery_item in enumerate(st.session_state["items"]):

    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(f"✅ {grocery_item}")

    with col2:
        if st.button("❌", key=index):
            st.session_state["items"].pop(index)
            st.rerun()