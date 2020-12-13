import streamlit as st
from streamlit.components.v1 import html

with open("movie_review/frontend/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Header
st.title("Movie Review")
st.write("Analisador Inteligente de reviews de filmes")

# Get from the database a random image file, below the example
img = {
    "source": "https://m.media-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg",
    "alt": "Harry Potter",
}

height = 400

# Show the image on screen so users can see
image_template = f'''
<div style="display: flex; justify-content: center;">
    <img  
        src="{img.get("source")}" 
        alt="{img.get("alt")}" 
        height="{height}"
    />
</div>
'''
html(image_template, height=height)

# Forms to get the review from users
review = st.text_area(label="Escreva aqui seu review sobre o filme acima!")
if st.button(label="Analisar"):
    # run the prediction on what user wrote. Return the answer accordigly!
    st.write("Mas que review ein!!")