import streamlit as st
import os
from openai import OpenAI

# Set up OpenAI API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Title and Description
st.title("📝 Marketing Copy Generator 🌟")
st.markdown("Create compelling marketing copy for your business needs, including ads, emails, and social media posts. 🚀")

# Sidebar for content options
with st.sidebar:
    st.header("Copy Options 🎨")
    copy_type = st.selectbox("Choose the type of copy to generate", ["Ad Copy", "Email Copy", "Social Media Post"])
    tone = st.selectbox("Tone of Voice 🗣️", ["Casual", "Professional", "Persuasive", "Friendly"])

# User Input for product/service details
product_name = st.text_input("Enter the product/service name", placeholder="e.g., Eco-Friendly Water Bottle")
product_description = st.text_area("Describe your product/service", placeholder="e.g., A reusable water bottle that keeps drinks cold for 24 hours...")

# Generate and Display Response
if st.button("Generate ✨"):
    if product_name and product_description:
        prompt = f"Generate {copy_type} for the following product in a {tone} tone:\n\nProduct Name: {product_name}\nDescription: {product_description}\n\nMarketing Copy:"
        
        # Generate response from OpenAI API
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": prompt}
                ],
                model="gpt-3.5-turbo"
            )
            marketing_copy = chat_completion.choices[0].message.content
            
            st.subheader("🎉 Generated Marketing Copy 🎉")
            st.write(marketing_copy)
            
            # Add Copy/Download Button for convenience
            st.download_button(label="Download Copy 📥", data=marketing_copy, file_name="marketing_copy.txt")
        except Exception as e:
            st.error(f"⚠️ Failed to generate content. Error: {str(e)}")
    else:
        st.warning("⚠️ Please provide both the product name and description to generate copy.")

# Display User Instructions
st.info(""" 
### How to Use:
1. 🏷️ Enter the name of your product or service.
2. 📝 Provide a brief description of what it does.
3. 🎤 Choose the type of copy and the tone.
4. ✨ Click 'Generate' to create your marketing copy!
""")
