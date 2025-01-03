import requests as r
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# def ai(query):
#     url = "https://api.groq.com/openai/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "llama3-8b-8192",
#         "messages": [
#             {"role": "system", "content": "You are a helpful Devops professor."},
#             {"role": "user", "content": f"{query}"}
#         ]
#     }
#     response = r.post(url, headers=headers, json=data)
#     # print(response)
#     if response.status_code == 200:
#         # print(response.json())
#         content = response.json()["choices"][0]["message"]["content"]
#         return content
#     else:
#         return {
#             "error": "failed to get data from ai"
#         }
    
# print(ai("generate a kubernetes lab"))

def fetch_knowledge_base():
    try:
        conn = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
        )
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM products ORDER BY RAND() LIMIT 20")
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as e:
        return {
            "error": f"Failed to fetch knowledge base: {e}"
        }
    
def ai(query):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    products = fetch_knowledge_base()
    product_context = "\n".join([f"{product['product_name']}: {product['category']}: {product['reviews']}" for product in products])

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a product expert and specialize in men and women's fashion. Here are some products you can suggest:\n" + product_context},
            {"role": "user", "content": f"{query}"}
        ]
    }
    response = r.post(url, headers=headers, json=data)
    # print(response)
    if response.status_code == 200:
        # print(response.json())
        content = response.json()["choices"][0]["message"]["content"]
        return content
    else:
        return {
            "error": "failed to get data from ai"
        }