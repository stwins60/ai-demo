import app
import streamlit as st


# st.title("Kubernetes Lab Generator")
# st.write("Generate a kubernetes lab with AI assistance")

# with st.form("lab_form"):
#     query = st.text_input("Enter your request for the kubernetes lab:", "Generate a kubernetes lab")
#     submit_button = st.form_submit_button("Generate")

# if submit_button:
#     st.write("Generating your kubernetes lab...")
#     result = app.ai(query)

#     if isinstance(result, dict) and "error" in result:
#         st.error(result["error"])
#     else:
#         st.success("Kubernetes lab generated successfully!")
#         st.text_area("Generate Lab", result, height=300)

st.title("Product Suggestion Generator")
st.write("Get AI-powered suggestions for products based on your query.")

# Form to input the user's query
with st.form("product_form"):
    query = st.text_input("Enter your request for product suggestions:", "Suggest some products")
    submit_button = st.form_submit_button("Get Suggestions")

# Handling the form submission
if submit_button:
    st.write("Fetching product suggestions...")
    result = app.ai(query)

    # Handling errors and results
    if isinstance(result, dict) and "error" in result:
        st.error(result["error"])
    else:
        st.success("Product suggestions generated successfully!")
        st.text_area("Product Suggestions", result, height=300)