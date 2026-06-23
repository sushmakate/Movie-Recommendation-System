import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")

similarity_matrix = joblib.load("similarity.joblib","rb")

with open("movie_list.pickle","rb") as m:
    movies = pickle.load(m)


movies_list = movies['clean_title'].values

m_name=st.selectbox("Select Movie Name:",movies_list)

recommend_list = []
def recommend(m_name,top_n =5):
    #find index of selected item
    item_index = movies[movies['clean_title']==m_name].index[0]

    #compute similarity score
    recomedation = similarity_matrix[item_index]

    #sort
    list = sorted(enumerate(recomedation),reverse=True,key=lambda x:x[1])
    top_movies = list[1:top_n+1]

    
    for idx, score in top_movies:
        recommend_list.append(movies.iloc[idx]['title'])
        
    return recommend_list

if st.button("Recommend"):
    st.write("Recommended movies are:")
    r = recommend(m_name)
    
    for i in r:
        st.write(i)