import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_movie_poster(movie_title):
    url = f'http://www.omdbapi.com/?apikey=7b997d9e &t={movie_title}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_url = data.get('Poster')
        return poster_url
    else:
        print(f"Failed to fetch data: {response.status_code}")


def recommend(movie):
    move_index=moviess[moviess['title']==movie].index[0]
    distance=Cosine_angle[move_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    new_recommend=[]
    movie_recommend=[]
    for i in movie_list:
        
        new_recommend.append(moviess.iloc[i[0]].title)
        movie_recommend.append(fetch_movie_poster(moviess.iloc[i[0]].title))
    return new_recommend,movie_recommend





movie_list=pickle.load(open('movies_dict.pkl', 'rb'))
Cosine_angle=pickle.load(open('Cosine_angle.pkl', 'rb'))

moviess = pd.DataFrame(movie_list)
selected_movie = st.selectbox("select a movie", moviess['title'].values)

if st.button('Recommend'):
    names,poster = recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])