import streamlit as st

def show_product_card(product, key_prefix=""):
    cols = st.columns([1])
    with cols[0]:
        if product.get('image'):
            st.image(product.get('image'), use_container_width=True)
        else:
            st.image('https://via.placeholder.com/250x180', use_container_width=True)


        st.markdown(f"**{product.get('name')}**")
        st.markdown(product.get('desc'))
        st.markdown(f"**Price:** ${product.get('price')}")
