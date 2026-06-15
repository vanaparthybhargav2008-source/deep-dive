import streamlit as st
from openai import OpenAI

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬",
    layout="wide"
)

st.title("💬 MiniStore Support Assistant")

st.write(
    "Ask questions about products, orders, delivery, "
    "returns, refunds, and payments."
)

# -----------------------------------
# OpenAI Client
# -----------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# -----------------------------------
# Product Catalog
# -----------------------------------
PRODUCT_CATALOG = """
Available Products:

1. Wireless Headphones
   Price: ₹2999
   Category: Electronics
   Description: Premium noise-cancelling wireless headphones with 30-hour battery life.

2. Smart Watch Pro
   Price: ₹4999
   Category: Electronics
   Description: Track fitness, notifications, and health metrics with style.

3. Leather Backpack
   Price: ₹2499
   Category: Fashion
   Description: Durable leather backpack suitable for work, travel, and daily use.

4. Running Shoes
   Price: ₹3499
   Category: Fashion
   Description: Comfortable lightweight shoes designed for daily training.

5. Coffee Maker
   Price: ₹1999
   Category: Home
   Description: Brew fresh coffee every morning with one-touch operation.

6. Study Desk Lamp
   Price: ₹899
   Category: Home
   Description: LED desk lamp with adjustable brightness and eye-care technology.
"""

# -----------------------------------
# System Prompt
# -----------------------------------
SYSTEM_PROMPT = f"""
You are the official customer support assistant for MiniStore.

Your responsibilities:

- Help customers with:
  - Products
  - Product details
  - Orders
  - Order status
  - Delivery and shipping
  - Refunds
  - Returns
  - Payment methods

Store Information:

{PRODUCT_CATALOG}

Store Policies:

Delivery:
- Standard delivery: 3-7 business days
- Express delivery: 1-3 business days

Returns:
- Products can be returned within 30 days of delivery.
- Products must be unused and in original condition.

Refunds:
- Refunds are processed within 5-7 business days after approval.

Payments:
- UPI
- Credit Cards
- Debit Cards
- Net Banking
- Wallets

Order Tracking:
- For demo purposes all orders are marked as "Processing".

Important Rules:

1. Only answer MiniStore-related questions.
2. Do NOT answer:
   - General knowledge
   - Programming
   - Politics
   - Medical advice
   - Personal advice
   - Science questions
   - Math questions
   - Any topic unrelated to MiniStore support.
3. If a question is unrelated, politely respond:

"I'm here to assist with MiniStore products, orders, deliveries, refunds, returns, and payment questions. Please let me know how I can help with your MiniStore shopping experience."

4. Always maintain a professional customer support tone.
5. Keep answers concise and helpful.
"""

# -----------------------------------
# Chat History
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# Display Previous Messages
# -----------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------------
# Chat Input
# -----------------------------------
user_prompt = st.chat_input(
    "Ask a MiniStore support question..."
)

if user_prompt:

    # Show User Message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Build Conversation
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(st.session_state.messages)

    # Generate Response
    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=conversation,
            temperature=0.3
        )

        assistant_reply = (
            response.choices[0]
            .message
            .content
        )

    except Exception as e:

        assistant_reply = (
            f"Support service temporarily unavailable.\n\n"
            f"Error: {str(e)}"
        )

    # Display Assistant Message
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )