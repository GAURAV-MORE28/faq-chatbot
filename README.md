# 🤖 FAQ Chatbot using NLP & Streamlit

An intelligent FAQ Chatbot built using **Natural Language Processing (NLP)** techniques.  
This chatbot answers user queries by matching them with predefined Frequently Asked Questions (FAQs) using **TF-IDF vectorization** and **Cosine Similarity**, and provides an interactive **Streamlit-based chat interface**.

---

## 📌 Features

- Interactive chat-style web interface
- NLP-based text preprocessing
- TF-IDF for text vectorization
- Cosine Similarity for matching user queries with FAQs
- Maintains chat history during the session
- Simple, clean, and beginner-friendly implementation

---

## 🛠️ Technologies Used

- **Python**
- **NLTK** – for text preprocessing
- **Scikit-learn** – for TF-IDF and similarity calculation
- **Streamlit** – for building the web-based chat UI

---

## 🧠 How the Chatbot Works

1. User enters a question in the chat interface
2. The input text is preprocessed:
   - Lowercasing
   - Removing punctuation
   - Tokenization
   - Stopword removal
3. FAQ questions and user input are converted into numerical vectors using **TF-IDF**
4. **Cosine Similarity** is used to compare the user question with all FAQs
5. The most similar FAQ is selected
6. The corresponding answer is displayed in the chat UI

---

## 📂 Project Structure

faq-chatbot/
│
├── app.py # Streamlit chat interface
├── faq_chatbot.py # NLP logic and FAQ matching
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

git clone https://github.com/GAURAV-MORE28/faq-chatbot.git
cd faq-chatbot
pip install -r requirements.txt
python -m streamlit run app.py


###  🎓 Academic Relevance

This project demonstrates:

Practical use of NLP concepts

Text preprocessing techniques

Feature extraction using TF-IDF

Similarity-based information retrieval

Integration of backend logic with a frontend UI

It is suitable for college projects, viva examinations, and beginner NLP demonstrations.

###  🚀 Future Enhancements

Add confidence score for answers

Handle unknown questions with fallback responses

Expand FAQ database

Add database support instead of static FAQs

###  👤 Author

Gaurav More


