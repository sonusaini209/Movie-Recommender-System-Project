import pickle
import streamlit as st
import requests
import pandas as pd

st.title('Movie Recommender System')


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommended_movies = []
    for i in distances[1:6]:
        #movie_id=i[0]

        # fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies =pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)


if st.button('Recommend'):
    recommendedations=recommend(selected_movie_name)
    for i in recommendedations:
        st.write(i)

#st.write('You selected:', option)