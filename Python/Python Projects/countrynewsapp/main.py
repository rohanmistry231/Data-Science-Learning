import streamlit as st
import requests
import pycountry

api_key = "f4**********************76"

st.title("Country News App")

col1, col2 = st.columns([3,1])
with col1:
    user_input = st.text_input("Enter the country name")

with col2:
    news_category = st.radio('Choose your news', ('Tech','Sports','Business','health','entertainment','general'))
    btn = st.button("Enter")

if btn:
    # changing country to a country code
    country = pycountry.countries.get(name=user_input).alpha_2
    print(country)
    # calling api
    url = f"https://newsapi.org//v2/top-headlines?country={country}&category={news_category}&apiKey={api_key}"
    res = requests.get(url)
    res = res.json()
    
    # loopind over data 
    data = res['articles']
    for d in data:
        st.header(d['title'])
        st.markdown(f"<span style='color:blue'>Published At: {d['publishedAt']}</span>", unsafe_allow_html=True)
        st.write('Source :', d['source']['name'])
        if d['urlToImage']:
            st.image(d['urlToImage'])
        if d['author']:
            st.write('Author: ', d['author'])
        if d['description']:
            st.write('Description :', d['description'])
        if d['content']:
            st.write(d['content'])
        st.write('Read More :', d['url'])
        st.markdown("----------------------")
