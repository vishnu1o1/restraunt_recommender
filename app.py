import streamlit as st
import joblib

zomatofinal = joblib.load(open('zomatofinal1.pkl','rb'))
zomatofinal1 = zomatofinal.columns[6:]

st.title('Zomato Recommendation System for Banglore')

def recom(dish):
    dish_recom = zomatofinal[zomatofinal[dish]==1][['approx_cost(for two people)','name','address','rate','dish_liked']].sort_values(by='rate',ascending=False).drop_duplicates(subset=['name']).head(10)
    return dish_recom

selected_dish = st.selectbox('What would you like to eat?',zomatofinal1)

if st.button('Recommend'):
    result = recom(selected_dish)
    st.table(result.reset_index(drop=True))
