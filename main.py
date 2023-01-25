import pickle
import streamlit as stardom
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = url.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    poster = []
    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        poster.append(fetch_poster(movie_id))

    return recommended_movies,poster


movies_dict = pickle.load(open('m_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

stardom.title('Movie Recommender System')

selected_movie = stardom.selectbox(
    "Type or select a movie from the dropdown",
movies['title'].values

)

if stardom.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = stardom.beta_columns(5)
    with col1:
        stardom.text(recommended_movie_names[0])
        stardom.image(recommended_movie_posters[0])
    with col2:
        stardom.text(recommended_movie_names[1])
        stardom.image(recommended_movie_posters[1])

    with col3:
        stardom.text(recommended_movie_names[2])
        stardom.image(recommended_movie_posters[2])
    with col4:
        stardom.text(recommended_movie_names[3])
        stardom.image(recommended_movie_posters[3])
    with col5:
        stardom.text(recommended_movie_names[4])
        stardom.image(recommended_movie_posters[4])




