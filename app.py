import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# -----------------------------
# Product Database
# -----------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "category": "Electronics",
        "description": "Premium noise-cancelling wireless headphones with 30-hour battery life."
    },
    {
        "name": "Smart Watch Pro",
        "price": 4999,
        "category": "Electronics",
        "description": "Track fitness, notifications, and health metrics with style."
    },
    {
        "name": "Leather Backpack",
        "price": 2499,
        "category": "Fashion",
        "description": "Durable leather backpack suitable for work, travel, and daily use."
    },
    {
        "name": "Running Shoes",
        "price": 3499,
        "category": "Fashion",
        "description": "Comfortable lightweight shoes designed for daily training."
    },
    {
        "name": "Coffee Maker",
        "price": 1999,
        "category": "Home",
        "description": "Brew fresh coffee every morning with one-touch operation."
    },
    {
        "name": "Study Desk Lamp",
        "price": 899,
        "category": "Home",
        "description": "LED desk lamp with adjustable brightness and eye-care technology."
    }
]

# -----------------------------
# Session State
# -----------------------------
if "cart_count" not in st.session_state:
    st.session_state.cart_count = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0

# -----------------------------
# CSS Styling
# -----------------------------
st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg,#1e3c72,#2a5298);
    padding:2rem;
    border-radius:15px;
    color:white;
    text-align:center;
    margin-bottom:2rem;
}

.product-card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.product-name {
    font-size:20px;
    font-weight:bold;
}

.product-price {
    font-size:24px;
    color:green;
    font-weight:bold;
}

/* Floating Support Button */
.support-button {
    position: fixed;
    bottom: 30px;
    right: 25px;
    background-color: #2a5298;
    color: white;
    padding: 15px 22px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 9999;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

.support-button:hover {
    background-color: #1e3c72;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set([p["category"] for p in products]))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("Shopping Cart")

st.sidebar.metric(
    "Items",
    st.session_state.cart_count
)

st.sidebar.metric(
    "Total",
    f"₹{st.session_state.cart_total}"
)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero">
<h1>MiniStore</h1>
<p>Your One-Stop Shop for Electronics, Fashion & Home Essentials</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Welcome Section
# -----------------------------
st.header("Welcome to MiniStore")

st.write("""
Browse our featured products and discover quality items at affordable prices.
""")

# -----------------------------
# Filter Products
# -----------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# -----------------------------
# Product Grid
# -----------------------------
st.subheader("Featured Products")

cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown(f"""
        <div class="product-card">
            <div class="product-name">{product['name']}</div>
            <p>{product['category']}</p>
            <p>{product['description']}</p>
            <div class="product-price">₹{product['price']}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Add to Cart",
            key=f"product_{index}"
        ):
            st.session_state.cart_count += 1
            st.session_state.cart_total += product["price"]
            st.success("Added to cart!")

# -----------------------------
# Floating Support Button
# -----------------------------
st.markdown("""
<a href="/Support_Chatbot" target="_self" class="support-button">
💬 Support
</a>
""", unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("MiniStore Demo Store")