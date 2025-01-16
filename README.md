# Movie-Recommendation-System

![ML](https://img.shields.io/badge/ML-Recommendation_System-blue.svg) 

![logo](l.png)

## Business Objectives :

All entertainment websites or online stores have millions/billions of items. It becomes challenging for the customer to select the right one. At this place, recommender systems come into the picture and help the user to find the right item by minimizing the options.

Recommendation Systems in the world of machine learning have become very popular and are a huge advantage to tech giants like Netflix, Amazon and many more to target their content to a specific audience. These recommendation engines are so strong in their predictions that they can dynamically alter the state of what the user sees on their page based on the user’s interaction with the app.

The business objective for us is: 
1. To create a Collaborative Filtering based Movie Recommendation System
2. Predict the rating that a user would give to a movie that he has not yet rated
3. Minimize the difference between predicted and actual rating (RMSE and MAPE)

## Data Collection :

The dataset has been obtained from Kaggle.

Link : [click](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system)


## Modelling :

The following modelling approach was used in the project:

1. Loading & exploring the Movie and User ratings data
2. Creating User-Item Matrix, User-User and Item-Item similarity matrices for Movie Recommendations
3. Creating feature and applying ML models to predict the ratings for unseen movies for a user

The detailed analysis and model creation can be found in the .ipynb file. 


## Conclusions :

In this project, we learned the importance of Recommendation Systems, the types of recommender systems being implemented, and how to use matrix factorization to enhance a system. 

We then built a movie recommendation system that considers user-user similarity, movie-movie similarity, global averages and matrix factorization. These concepts can be applied to any other user-item interactions systems.

We tried generating recommendations based on similarity matrix and Collaborative Filtering techniques.

We tried to predict the ratings for movies that the user might give based on its past rating behaviours and measure the accuracy using RMSE and MAPE error metrics.

Surely, there is huge scope of improvement and tring out different techniques and ML/DL algorithms.
