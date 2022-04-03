import pickle
import streamlit as st
import pandas as pd

def recommend(title):
    indices = pd.Series(df1.index).drop_duplicates()
    index= indices[indices==title].index[0]
    similarity_scores = pd.Series(similarity[index]).sort_values(ascending=False)
    top_3_videos = list(similarity_scores.iloc[1:4].index)
    recommended_video_names=[]
    for i in top_3_videos:
        recommended_video_names.append(list(df1.index)[i])
    return recommended_video_names
page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://youthincmag.com/wp-content/uploads/2018/08/E-Learning.jpg");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown('# Pratham e-learning Content Recommendation')
df1 = pickle.load(open('videolist.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

videolist = df1.index.unique()
selected_video = st.selectbox(
    "Type or select a video from the dropdown",
    videolist
)


if st.button('Show Recommendation'):
    recommended_video_names = recommend(selected_video)
    for i in recommended_video_names:
        st.subheader(i)




    
