import pandas as pd
import streamlit as st

def Show_Main_Stats(selected_weapon):
    st.markdown(f"<h2 style='text-align: left;'>Bar Graph of most used Abilities</h2>", unsafe_allow_html=True)
    
    all_ability_stats_df = pd.read_csv("../data/Weapon_ability_means.csv")
    ability_stats_df = all_ability_stats_df[all_ability_stats_df['Weapon_Name'] == selected_weapon]
    track_abilities_df = ability_stats_df.iloc[:, -15:-1]
    st.bar_chart(track_abilities_df.iloc[0])
    st.dataframe(track_abilities_df)