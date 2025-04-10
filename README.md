# 🛒 Smart Shopping: Data and AI for Personalized E-Commerce

Smart Shopping is a personalized e-commerce platform that uses data and AI to recommend products to users based on their browsing behavior, purchase history, and demographics. The system is powered by a multi-agent architecture with on-premise language models and a custom recommendation engine.

---

## 💡 Features

- 🧠 **AI-Based Recommendations** using embedding models and TinyLlama.
- 👥 **Multi-Agent Architecture** to handle different recommendation and customer support tasks.
- 🌐 **Web Scraper** to collect product data.
- 📊 **Data Visualization** and Analytics via Streamlit.
- 📁 **Data Storage** using SQLite.
- 🤖 **Custom ML Models** for product similarity.
- 🔍 **User Behavior Analysis** for personalization.

---

## 🗂️ Project Structure

smart_shopping/ │ ├── agents/ │ ├── customer.py │ ├── product.py │ └── recommender.py │ ├── app/ │ └── streamlit_app.py │ ├── datasets/ │ ├── customer_data_collection.csv │ └── product_recommendation_data.csv │ ├── embeddings/ │ └── embedding_generator.py │ ├── tools/ │ ├── ml_tool.py │ └── scrapper_tool.py │ ├── .gitignore ├── check_db.py ├── database.py ├── load_data.py └── main.py

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smart_shopping.git
   cd smart_shopping
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit App:

bash
Copy
Edit
streamlit run app/streamlit_app.py
🧠 AI Models Used
TinyLlama: For lightweight, fast, and on-prem inference.

Custom Embedding Generator: Converts product text into vectors.

ML-based Similarity Engine: Finds related products.

🛠️ Technologies Used
Python

Streamlit

SQLite

pandas

 Ollama /tinyllama

