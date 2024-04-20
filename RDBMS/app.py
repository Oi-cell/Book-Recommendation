from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

app = Flask(__name__)

# Generate synthetic user data
users = pd.DataFrame({'user_id': range(1, 101)})  # Assuming 100 users

# Generate synthetic book data
books = pd.DataFrame({'book_id': range(1, 101)})  # Assuming 100 books

# Generate synthetic borrowing history (randomly assign books to users)
borrowing_history = pd.DataFrame({
    'user_id': np.random.choice(users['user_id'], size=500),
    'book_id': np.random.choice(books['book_id'], size=500),
    'borrow_date': pd.date_range('2022-01-01', periods=500),
    'return_date': pd.date_range('2022-01-01', periods=500) + pd.to_timedelta(np.random.randint(1, 30, size=500), unit='D')
})

# Function to get book recommendations for a given user
def get_recommendations(user_id, top_n=5):
    # Placeholder implementation - replace with actual recommendation logic
    recommendations = ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5']
    return recommendations[:top_n]

# Define route to render main page
@app.route('/')
def index():
    return render_template('index.html')

# Define route to handle recommendation request
@app.route('/recommendations', methods=['POST'])
def recommendations():
    user_id = int(request.form['user_id'])
    recommendations = get_recommendations(user_id)
    return render_template('recommendations.html', user_id=user_id, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
