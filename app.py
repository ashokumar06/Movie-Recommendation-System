import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import requests


tfidf = pickle.load(open("vectorizer.pkl", "rb"))
cosine_sim = pickle.load(open("cosine_sim.pkl", "rb"))
indices = pickle.load(open("indices.pkl", "rb"))
df2 = pd.read_csv("data_movies.csv")[['original_title', 'overview','id']].dropna().reset_index(drop=True)
movie_titles = list(indices.index)


def get_movie_posters(movie_id, retries=5, delay=5):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3f0f2cdffa48725e4d15d8a037ec3e9b"
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()
            return "https://image.tmdb.org/t/p/w500"+data['poster_path'] 
        except requests.exceptions.ConnectionError as e:
            # st.write(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)  
            else:
                raise


def get_recommendations(title, cosine_sim=cosine_sim):
    title = title.strip().lower()
    try:
        idx = indices[title]  
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]  
        movie_indices = [i[0] for i in sim_scores]
        return df2['original_title'].iloc[movie_indices]
    except KeyError:
        return ["Movie not found. Please check the title."]

# Streamlit app
st.title("🎥 Movie Recommendation System")
st.write("Find similar movies based on your favorite movie!")

select_movie = st.selectbox("Select a movie:", movie_titles, index=0)

def get_movie_id(title):
    title = title.strip().lower()
    try:
        for gtitle in df2['original_title']:
            if gtitle.lower() == title:
                idx = df2[df2['original_title'] == gtitle].index[0]
                return df2.iloc[idx].id
    except KeyError:
        return None

if st.button("Get Recommendations"):
    if select_movie:
        recommendations = get_recommendations(select_movie)
        st.subheader("Top Recommendations:")
        cols = st.columns(5)
        for idx, movie in enumerate(recommendations, 1):
            col = cols[idx % 5]

            with col:
                st.write(f"{idx}. { movie}")
                try:
                    movie_id = get_movie_id(movie)
                    movie_poster_url = get_movie_posters(movie_id)
                    st.image(movie_poster_url)
                except Exception as e:
                    st.warning(f"Error fetching movie data: {e}")
    
    else:
        st.warning("Please enter a movie title!")


st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        position: fixed;
        bottom: 20px;
        width: 100%;
    }
    .button-container a {
        font-size: 18px;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        border-radius: 5px;
        text-decoration: none;
    }
    .button-container a:hover {
        background-color: #45a049;
    }
    </style>
    <div class="button-container">
        <a href="https://ashokumar.in/" target="_blank">About Me</a>
    </div>
    """,
    unsafe_allow_html=True,
)
