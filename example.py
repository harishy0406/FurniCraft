# main.py (simplified)
style_choice = st.sidebar.selectbox("Select Style", ["Modern", "Victorian"]) # type: ignore
factory = ModernFurnitureFactory() if style_choice == "Modern" else VictorianFurnitureFactory() # type: ignore

# Get selected items
chair = factory.create_chair(products_data[style_choice]["Chair"][0]) # type: ignore
st.image(chair.image) # type: ignore
if st.button("Add Chair to Cart"): # type: ignore
    st.session_state.cart.add(chair.to_dict()) # type: ignore

# Apply Strategy
strategy = FestiveDiscount(10) # type: ignore
total = strategy.calculate(st.session_state.cart.items) # type: ignore
st.write(f"Final Total: ${total:.2f}") # type: ignore
