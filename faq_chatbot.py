# ==============================
# FAQ CHATBOT USING NLP (NLTK)
# ==============================

# ---------- IMPORT LIBRARIES ----------
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------- DOWNLOAD REQUIRED NLTK DATA ----------
# (Run once, it will not download again)
nltk.download('punkt')
nltk.download('stopwords')


# ---------- STEP 1: CREATE FAQ DATA ----------
# Questions and their answers
faqs = {
    "What is your return policy?": "You can return the product within 7 days of delivery.",
    "How can I contact customer support?": "You can contact customer support via email or phone.",
    "What payment methods do you accept?": "We accept UPI, debit card, credit card, and net banking.",
    "Do you provide home delivery?": "Yes, we provide home delivery all over India.",
    "How long does delivery take?": "Delivery usually takes 3 to 5 working days."
}


# ---------- STEP 2: TEXT PREPROCESSING FUNCTION ----------
def preprocess_text(text):
    """
    This function:
    1. Converts text to lowercase
    2. Removes punctuation
    3. Tokenizes words
    4. Removes stopwords
    """

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize text into words
    tokens = word_tokenize(text)

    # Remove stopwords (is, the, and, etc.)
    stop_words = stopwords.words('english')
    cleaned_tokens = [word for word in tokens if word not in stop_words]

    # Join tokens back into sentence
    return " ".join(cleaned_tokens)


# ---------- STEP 3: PREPROCESS ALL FAQ QUESTIONS ----------
questions = list(faqs.keys())
processed_questions = [preprocess_text(q) for q in questions]


# ---------- STEP 4: CONVERT TEXT INTO NUMERICAL FORM ----------
# TF-IDF converts text into vectors (numbers)
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)


# ---------- STEP 5: FUNCTION TO FIND BEST ANSWER ----------
def get_best_answer(user_question):

    # Preprocess user question
    processed_user_question = preprocess_text(user_question)

    # Convert user question into vector
    user_vector = vectorizer.transform([processed_user_question])

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(user_vector, faq_vectors)

    # Find index of best matching question
    best_match_index = similarity_scores.argmax()

    # Return the corresponding answer
    return faqs[questions[best_match_index]]


