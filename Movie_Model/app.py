import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0fd2bba2ad7468b1caa4820e4bdda5f9'.format(movie_id))
    data = response.json()
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=0fd2bba2ad7468b1caa4820e4bdda5f9'.format(movie_id))
    # st.text('https://image.tmdb.org/t/p/original'+ data['poster_path'])
    return ('https://image.tmdb.org/t/p/original'+ data["poster_path"])



def recommend(movie):

    movie_index = movies_list[movies_list.original_title == movie].index[0]
    movies = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x:x[1])[1:8]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies:

        movie_id = movies_list.iloc[i[0]].id #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

        recommended_movies.append(movies_list.iloc[i[0]].original_title)
    return recommended_movies,recommended_movies_posters

movies_list = pickle.load(open('movies.pkl','rb'))

movie_list = movies_list.original_title.values
similarity = pickle.load(open('similarity.pkl','rb'))


st.title("Movie Recommender")


selected_movie_name = st.selectbox(
    'Which movie would you like to watch?',movie_list)

if st.button('Recommend'):
    st.write('Similar Movies To: ', selected_movie_name)
    names , posters = recommend(selected_movie_name)
    if names == None:
        st.write("NO MOVIES FOUND! :(")

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col = [col1, col2, col3, col4, col5, col6, col7]
    c = 0
    for i in col:
        with i:
            st.text(names[c])
            st.image(posters[c])
            c = c + 1
    # with col1:
    #     st.header(names[0])
    #     st.image(posters[0])
    #
    # with col2:
    #     st.header(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.header(names[2])
    #     st.image(posters[2])
    #
    # with col4:
    #     st.header(names[3])
    #     st.image(posters[3])
    #
    # with col5:
    #     st.header(names[4])
    #     st.image(posters[4])
    #
    # with col6:
    #     st.header(names[5])
    #     st.image(posters[5])
    #
    # with col7:
    #     st.header(names[6])
    #     st.image(posters[6])


