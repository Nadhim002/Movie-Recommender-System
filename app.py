import streamlit as st
import pickle
import  requests

def fetch_poster(movie_id):
    #api_key = '8265bd1679663a7ea12ac168da84d2e8'  # key1
    api_key = '60f63a51728377d2f9660540cf8c0fba' # key2

    # Use our own api key
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id,api_key)
    data = requests.get(url)
    data = data.json()
    img_path = data['poster_path']
    full_img_path =  'https://image.tmdb.org/t/p/w185/' + img_path
    return full_img_path

def recommend(selected_movie_name):
     movie_index = movies[movies['title'] == selected_movie_name].index[0]
     distances = similarity[movie_index]
     movies_ind = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
     lst = []
     ind = []
     for i in movies_ind:
         lst.append(movies['title'].loc[i[0]])
         ind.append(movies[movies['title'] == movies['title'].loc[i[0]]]['id'].values[0])
     return lst, ind


similarity = pickle.load(open('similarity.pkl','rb'))
movies = pickle.load(open('movie_list.pkl','rb'))
movies_list  =  movies['title'].values

st.title('Movie Recommendor')


selected_movie_name  = st.selectbox(
    'Please select your Fav Movie',
     movies_list)

if st.button('Recommend') :
  recommended_movie_names , recommended_movie_id = recommend(selected_movie_name)
  col1, col2, col3, col4, col5 = st.columns(5)

  with col1:
      st.text(recommended_movie_names[0])
      st.image(fetch_poster(recommended_movie_id[0]))

  with col2:
      st.text(recommended_movie_names[1])
      st.image(fetch_poster(recommended_movie_id[1]))

  with col3:
      st.text(recommended_movie_names[2])
      st.image(fetch_poster(recommended_movie_id[2]))

  with col4 :
      st.text(recommended_movie_names[3])
      st.image(fetch_poster(recommended_movie_id[3]))

  with col5:
      st.text(recommended_movie_names[4])
      st.image(fetch_poster(recommended_movie_id[4]))
