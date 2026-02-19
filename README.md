Spotify Personal Listening Intelligence System
Overview
--Time-aware behavioral music analytics system that analyzes Spotify listening history to:
-Detect peak listening hours
-Learn time based genre preferences
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

System Architecture:
Spotify JSON Export
        ↓
Data Cleaning (Python)
        ↓
Feature Engineering
        ↓
Master Dataset
        ↓
1️)Tableau Behavioral Dashboard
2️)Time-Aware Recommendation Logic
3️)Streamlit Interactive App


--Features:
1️)Tableau Behavioral Dashboard:
-Listening distribution by hour
-Artist × Time heatmaps
-Genre evolution by time of day
-Language segmentation
-Session pattern analysis

2)Streamlit  App
 Interactive dashboard with:
-Current hour detection
-Peak listening hour insight
-Time-based genre recommendation
-Top artists for that hour
-Most played songs per artist
-Direct Spotify redirect links

 
--Tech Stack:
Data Processing:
Python
Pandas
NumPy

Visualization:
Tableau
Streamlit

Behavioral Logic:
Time-based aggregation
Session modeling
Genre segmentation
Hourly dominance mapping


--Data Privacy Notice
Due to privacy concerns, the full Spotify dataset is not included in this repository.
To run locally:
1)Request Spotify Extended Streaming History
2)Run preprocessing script
3)Generate spotify_master_dataset.csv
4)Launch the Streamlit app

No personal data is stored in this repository.

--Future Improvements
1)Future work includes:
2)ML-based predictive modeling for next-genre prediction
3)Session duration forecasting
4)Time-aware probabilistic recommendation engine
4)Deployment as a hosted web application
5)Real-time Spotify API integration

--Key Learnings
1)Handling messy real-world JSON data
2)Feature engineering for behavioral modeling
3)Time-series segmentation
4)Building reproducible analytics pipelines
5)Designing user-facing data products
