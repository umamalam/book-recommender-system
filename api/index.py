from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

popular_df = pickle.load(open('popular.pkl','rb'))

@app.route('/')
def home():
    return "Book Recommender Running 🚀"

# Vercel handler
def handler(request, context):
    return app(request.environ, start_response)