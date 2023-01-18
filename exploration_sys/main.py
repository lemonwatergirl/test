import streamlit as st

st.title('Dish Exploration System')

# if 'count' not in st.button:
#   st.session_state["count"] = 0

if st.button('Say hello'):
  genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

  # if genre == 'Comedy':
  #     st.write('You selected comedy.')