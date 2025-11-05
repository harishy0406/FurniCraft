import streamlit as st
from products.product_registry import load_products, save_products
from factories.modern_factory import ModernFurnitureFactory
from factories.victorian_factory import VictorianFurnitureFactory
from patterns.singleton_cart import ShoppingCart
from patterns.strategy_pricing import NoDiscount, FestiveDiscount, FlatCoupon
from patterns.decorator_features import add_warranty, add_cushion
from patterns.prototype_set import FurnitureSet
from utils import show_product_card

# --- Page config ---
st.set_page_config(page_title="FurniCraft", layout="wide")

# --- session state ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

if 'cart' not in st.session_state:
    st.session_state.cart = ShoppingCart.get_instance()

# Load data
products_data = load_products()

import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- Landing Page ---
if st.session_state.page == 'landing':
    # Load background image as base64
    bg_image = get_base64_image("assets/bg/landing_bg.png")

    st.markdown(
        f"""
        <style>
        .landing {{
            background-image: url("data:image/png;base64,{bg_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            color: white;
        }}
        .center {{
            text-align: center;
            padding-top: 180px;
        }}
        .title {{
            font-size: 56px;
            font-weight: 700;
            text-shadow: 2px 2px 8px #000;
        }}
        .subtitle {{
            font-size: 22px;
            margin-top: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="landing"><div class="center">', unsafe_allow_html=True)

    # Centered title
    st.markdown('<div class="title">🪑 FurniCraft</div>', unsafe_allow_html=True)

    # Short tagline / subtitle
    st.markdown(
        '<div class="subtitle">Smart Furniture Management System using Software Reuse & Design Patterns</div>',
        unsafe_allow_html=True
    )

    # Short project description (centered paragraph)
    st.markdown(
        """
        <p style="font-size:18px; max-width:700px; margin:20px auto; line-height:1.6; color:#f0f0f0;">
        FurniCraft is a <b>Streamlit-based</b> interactive system that lets users explore, customize, 
        and purchase furniture from different design families like <b>Modern</b> and <b>Victorian</b>. 
        The system demonstrates multiple <b>software design patterns</b> — Abstract Factory, Singleton, 
        Strategy, Decorator, and Prototype — to promote <b>code reuse</b> and scalability.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Start Exploring button
    if st.button("✨ Start Exploring"):
        st.session_state.page = "main"

    st.markdown("</div></div>", unsafe_allow_html=True)



# --- Main Page ---
elif st.session_state.page == 'main':
    st.sidebar.title('Controls')
    st.sidebar.markdown('Navigation')
    if st.sidebar.button('Home'):
        st.session_state.page = 'landing'
        st.rerun()


    st.title('🪑 FurniCraft — Furniture Management')

    # Admin section
    with st.expander('Admin: Add Product (persisted to data/products.json)'):
        style = st.selectbox('Style', options=list(products_data.keys()))
        category = st.selectbox('Category', ['Chair', 'Sofa', 'Table'])
        name = st.text_input('Product Name')
        price = st.number_input('Price', min_value=0)
        desc = st.text_area('Description')
        if st.button('Add Product'):
            # create id
            new_id = f"{style.lower()}_{category.lower()}_{len(products_data.get(style,{}).get(category,[]))+1}"
            new_item = {"id": new_id, "name": name, "price": price, "desc": desc, "image": ""}
            products_data.setdefault(style, {}).setdefault(category, []).append(new_item)
            save_products(products_data)
            st.success(f"Added {name} to {style} -> {category}")

    st.sidebar.markdown('---')
    style_choice = st.sidebar.selectbox('Select Furniture Style', options=list(products_data.keys()))
    st.sidebar.markdown('')

    # factories selection
    factory = ModernFurnitureFactory() if style_choice == 'Modern' else VictorianFurnitureFactory()

    # Select items from registry (allow picking different items)
    st.header(f'{style_choice} Collection')
    cols = st.columns(3)
    categories = ['Chair', 'Sofa', 'Table']
    selected_items = {}
    for col, cat in zip(cols, categories):
        with col:
            st.subheader(cat)
            options = products_data.get(style_choice, {}).get(cat, [])
            if not options:
                st.info('No items in this category. Add via Admin section.')
            else:
                choices = {opt['name']: opt for opt in options}
                chosen_name = st.selectbox(f'Select {cat}', options=list(choices.keys()), key=f'{cat}_sel')
                chosen = choices[chosen_name]
                show_product_card(chosen)
                if st.button(f'Add {chosen.get("name")} to Cart', key=f'add_{chosen.get("id")}'):
                    st.session_state.cart.add(chosen)
                    st.success(f"{chosen.get('name')} added to cart")
                # extras
                if st.checkbox(f'Add 2-year warranty to {chosen.get("name")}', key=f'w_{chosen.get("id")}'):
                    decorated = add_warranty(chosen, years=2, cost=20)
                    st.session_state.cart.add(decorated)
                    st.success('Warranty added and item added to cart')

    # Show cart
    # --- Sidebar Cart ---
    st.sidebar.header('🛒 Cart')
    cart = st.session_state.cart

    if st.sidebar.button("🧹 Clear Cart"):
        cart.clear()
        st.sidebar.success("Cart cleared successfully!")
        st.rerun()

    if cart.items_count() == 0:
        st.sidebar.info("Your cart is empty.")
    else:
        for i, item in enumerate(cart.items):
            st.sidebar.write(f"{i+1}. {item.get('name')} — ${item.get('price')}")
        st.sidebar.markdown(f"**Total items:** {cart.items_count()}")

    # pricing strategy selection
    st.sidebar.header('Pricing')
    strat = st.sidebar.selectbox('Choose pricing strategy', ['No Discount', 'Festive (10%)', 'Flat Coupon $20'])
    strategy = NoDiscount()
    if strat == 'Festive (10%)':
        strategy = FestiveDiscount(10)
    elif strat == 'Flat Coupon $20':
        strategy = FlatCoupon(20)

    total = strategy.calculate(cart.items)
    st.sidebar.markdown(f"## Total: ${total:.2f}")

    if st.sidebar.button('Checkout'):
        if cart.items_count() == 0:
            st.warning("Your cart is empty! Please add items before checkout.")
        else:
            st.balloons()
            st.success("🎉 Checkout successful!")
            st.markdown("## 🧾 Order Summary")
            
            # Show each item in a clean table
            summary_data = [
                {"Item": item.get("name"), "Price ($)": item.get("price"), "Description": item.get("desc")}
                for item in cart.items
            ]
            st.table(summary_data)

            st.markdown(f"💰 Applied Pricing Strategy: `{strat}`")
            st.markdown(f"🏷️ Final Total: **${total:.2f}**")

            st.info("🪑 Thank you for shopping with FurniCraft! Your order has been placed successfully.")

        # Optionally clear cart after checkout
        if st.button("🧹 Clear Cart"):
            cart.clear()
            st.success("Cart cleared successfully!")
            st.session_state["total"] = 0
            st.rerun()


    # Compare mode (Prototype)
    st.markdown('---')
    if st.button('Clone current set for comparison'):
        # build current set from selected choices
        try:
            chair_choice = st.session_state.get('Chair_sel')
            sofa_choice = st.session_state.get('Sofa_sel')
            table_choice = st.session_state.get('Table_sel')
        except Exception:
            chair_choice = sofa_choice = table_choice = None
        # we'll just clone cart items as a demonstration
        current_set = FurnitureSet(style_choice, {}, {}, {})
        clone = current_set.clone()
        st.info('Cloned current configuration (prototype pattern demo).')

    st.markdown('---')
    if st.button('Back to Landing'):
        st.session_state.page = 'landing'
        st.rerun()
