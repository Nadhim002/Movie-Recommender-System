# Movie-Recommender-System using TMDB Ratings

Overview

The Movie Recommender System is a machine learning project that provides personalized movie recommendations to users based on their preferences. It utilizes  content-based filtering techniques to suggest movies that users are likely to enjoy.

![image](https://github.com/user-attachments/assets/045d705c-4c76-4176-89e3-c5073c8744ca)

Dataset :

The dataset used for training and evaluation is sourced from the [Tmdb Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) . It includes information about movies, user ratings, and user demographics.

Data preprocessing :

I have done preprocessing by adding all the useful features to create a single columns and I have Used various techniques like stemming and stop words removal

Feature Extration :

I have used CountVectorizer to convert text data into vectors and vector is a best way to calculate Cosine similarity

Model Training : 

The base technique used for model training is cosine similarity and we have found the  soine similarity between the all movies with each other .This model is similar to Knn model because it Does not use any loss function . 

Prediction : 

The Given movie's cosine similarity is retreived from cosine similarity matrix and the top five movie recommendation given based on the cosine similarity . Using the tmbd api we are retreiving the movies Poster from tmbd database . 
