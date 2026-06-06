import streamlit as st
import pandas as pd

df = pd.read_csv("outputs/final_clustered_data.csv")

restaurant_indices = pd.Series(
    df.index,
    index=df['name']
).drop_duplicates()

def recommend_restaurants(restaurant_name, n=5):

    if restaurant_name not in restaurant_indices:
        return "Restaurant not found"

    idx = restaurant_indices[restaurant_name]

    cluster = df.loc[idx, 'cluster']

    recommendations = df[
        (df['cluster'] == cluster) &
        (df.index != idx)
    ]

    return recommendations[
        ['name', 'city', 'cuisine', 'rating']
    ].head(n)

st.title("🍽️ Swiggy Restaurant Recommendation System")

restaurant = st.selectbox(
    "Choose Restaurant",
    sorted(df['name'].unique())
)

if st.button("Get Recommendations"):
    result = recommend_restaurants(restaurant)
    st.dataframe(result)