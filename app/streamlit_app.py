import streamlit as st
import requests

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")
st.write("Enter your User ID to get your personalized movie recommendations.")

user_id = st.number_input(
    "User ID",
    min_value=1,
    step=1
)

if st.button("Recommend Movies"):

    try:
        with st.spinner("Getting your recommendations..."):

            response = requests.get(
                f"http://127.0.0.1:8000/recommendations/{user_id}",
                timeout=5
            )

            response.raise_for_status()

            recommendations = response.json()["recommendations"]

        st.subheader("Your Top 10 Recommendations")

        for i, movie in enumerate(recommendations, start=1):
            st.write(f"**{i}.** {movie}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the recommendation server.")

    except requests.exceptions.Timeout:
        st.error("The recommendation server took too long to respond.")

    except requests.exceptions.HTTPError:
        st.error("The recommendation server returned an error.")