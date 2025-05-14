import pandas as pd
import streamlit as st
import plotly.express as px


def Show_Main_Stats(selected_weapon, colour1, colour2):
    Show_Ability_Stats(selected_weapon, colour1, colour2)
    Show_Modes_Stats(selected_weapon)


def Show_Ability_Stats(selected_weapon, colour1, colour2):
    all_ability_stats_df = pd.read_csv("../data/Weapon_ability_means.csv")
    ability_stats_df = all_ability_stats_df[all_ability_stats_df['Weapon_Name'] == selected_weapon]
    
    Builds_count = ability_stats_df.iloc[0]
    Builds_count = Builds_count.iloc[-1]
    
    track_abilities_df = ability_stats_df.iloc[:, -15:-1]
    track_abilities_df = track_abilities_df.iloc[0].reset_index()
    track_abilities_df.columns = ['Abilities', 'Ability Points (AP)']#
    track_abilities_df['Ability Points (AP)'] = (track_abilities_df['Ability Points (AP)']).round(4)
    
    st.markdown(f"<h2 style='text-align: left;'>Anaylsis based on {Builds_count} Builds</h2>", unsafe_allow_html=True)
    
    fig = px.bar(track_abilities_df, x='Abilities', y='Ability Points (AP)', title=f"Average ability points for {selected_weapon} builds",
                  color='Ability Points (AP)', color_continuous_scale=[colour1, colour2])
    # fig.update_traces(marker_color=colour2)
    fig.update_layout(
        title_font=dict(size=20),
    )
    st.plotly_chart(fig)
    
    non_track_abilities_df = ability_stats_df.iloc[:, 9:20]
    non_track_abilities_df = non_track_abilities_df.iloc[0].reset_index()
    non_track_abilities_df.columns = ['Abilities', 'Percentage of Builds Using (%)']
    non_track_abilities_df['Percentage of Builds Using (%)'] = (non_track_abilities_df['Percentage of Builds Using (%)'] * 100).round(4)
    
    fig2 = px.bar(non_track_abilities_df, x='Abilities', y='Percentage of Builds Using (%)', title=f"Usage of primary only abilities for {selected_weapon} builds",
                  color='Percentage of Builds Using (%)', color_continuous_scale=[colour1, colour2])
    # fig2.update_traces(marker_color=colour2)
    fig2.update_layout(
        title_font=dict(size=20),
    )
    st.plotly_chart(fig2)   
    

def Show_Modes_Stats(selected_weapon):
    all_mode_stats_df = pd.read_csv("../data/Game_mode_by_Weapon.csv")
    st.dataframe(all_mode_stats_df)