import streamlit as st
import pandas as pd
import datetime
import urllib.parse


st.set_page_config(
    page_title=" Personal Listening Intelligence",
    layout="wide",
)

st.title("Personal Listening Intelligence System")
st.markdown("AI-powered behavioral music insights")


@st.cache_data
def load_data():
    df = pd.read_csv("spotify_master_dataset.csv")
    df = df[df["minutes_played"] > 0]
    df["Hour"] = df["Hour"].astype(int)
    return df

df = load_data()


hourly_genre = (
    df.groupby(["Hour", "genre"])["minutes_played"]
    .sum()
    .reset_index()
)

hourly_top_genre = (
    hourly_genre.sort_values(["Hour", "minutes_played"], ascending=[True, False])
    .groupby("Hour")
    .first()
    .reset_index()
)

hour_genre_map = dict(zip(hourly_top_genre["Hour"], hourly_top_genre["genre"]))


session_hour = (
    df.groupby("Hour")["session_id"]
    .nunique()
    .sort_values(ascending=False)
)

peak_hour = session_hour.index[0]


current_hour = datetime.datetime.now().hour

if current_hour in hour_genre_map:
    current_genre = hour_genre_map[current_hour]
else:
    current_genre = hour_genre_map[peak_hour]

filtered_df = df[
    (df["Hour"] == current_hour) &
    (df["genre"] == current_genre)
]

if filtered_df.empty:
    filtered_df = df[df["genre"] == current_genre]


top_artists = (
    filtered_df.groupby("artist")["minutes_played"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)


st.subheader("Behavioral Insight")

col1, col2, col3 = st.columns(3)

col1.metric("Current Hour", current_hour)
col2.metric("Peak Listening Hour", peak_hour)
col3.metric("Suggested Genre", current_genre)

st.divider()

st.subheader("Recommended Artists For You")

if top_artists.empty:
    st.warning("No listening data for this hour.")
else:
    for artist in top_artists.index:

        artist_df = df[df["artist"] == artist]

        top_songs = (
            artist_df.groupby("track")["minutes_played"]
            .sum()
            .sort_values(ascending=False)
            .head(3)
        )

        spotify_artist_url = "https://open.spotify.com/search/" + urllib.parse.quote(artist)

        with st.container():
            st.markdown("---")
            colA, colB = st.columns([3, 1])

            with colA:
                st.markdown(f"###  {artist}")

                st.markdown("**Your Most Played Songs:**")
                for song in top_songs.index:
                    spotify_song_url = "https://open.spotify.com/search/" + urllib.parse.quote(f"{artist} {song}")
                    st.markdown(f"- [{song}]({spotify_song_url})")

            with colB:
                st.link_button(" Open Artist", spotify_artist_url)
