Spotify Personal Listening Intelligence System
Overview
--An AI-powered behavioral music analytics system that analyzes Spotify listening history to:
-Detect peak listening hours
-Learn time-based genre preferences
-Recommend artists dynamically
-Build predictive ML models
-Provide an interactive Streamlit dashboard
-Visualize behavioral patterns in Tableau

--Data Acquisition & Processing
1️)Data Source
The dataset was obtained from Spotify’s official data export tool:
Requested extended streaming history from Spotify account
Received JSON files containing:
-Track metadata
-Listening timestamps
-Session data
-Device/platform usage
-Play duration (ms_played)

--2️)Data Cleaning
Steps performed:
-Removed entries with 0 minutes played
-Converted ms_played → minutes_played
-Converted timestamps to DateTime format
-Extracted:
-Hour
-Time of Day (Morning/Afternoon/Night)
-Removed sensitive fields (IP address)
-Filtered null tracks and corrupted rows

3️)Feature Engineering
Created:
-session_id using time gap threshold
-gap_minutes between plays
-new_session flag
-Hourly genre mapping
-Peak session hour detection
-Master dataset: spotify_master_dataset.csv

--Features:
1️)Tableau Behavioral Dashboard:
-Listening distribution by hour
-Artist × Time heatmaps
-Genre evolution by time of day
-Language segmentation
-Session pattern analysis

2️)Time-Aware Recommendation Engine
-Detects dominant genre per hour
-Suggests artists based on behavioral history
-Personalized Spotify redirect links

3️)Machine Learning Models
-Genre classification model
-Peak listening hour model
-Session duration prediction

4️)Streamlit AI App
 Interactive dashboard with:
-Real-time hour detection
-Recommended artists
-Clickable Spotify links
-Most played songs per artist

 
--Tech Stack:
Python
Pandas
Scikit-learn
XGBoost
TensorFlow (LSTM)
Streamlit
Tableau
