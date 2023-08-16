import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open('movies.pkl','rb'))
movies_name = movies_list['title'].values

def recommend(movie):
      movie_index = movies_list[movies_list['title'] == movie].index[0]
      distances = similarity[movie_index]
      movies = sorted(list(enumerate(distances)), reverse = True, key =lambda x: x[1])[1:6]
      
      recommended_movies = []
      for i in movies:
            recommended_movies.append(movies_list.iloc[i[0]].title)
      return recommended_movies

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Enter the Movie Name?',
    movies_name)

if st.button('Recommend'):
      recommendations = recommend(selected_movie_name)
      for i in recommendations:
            st.write(i)
