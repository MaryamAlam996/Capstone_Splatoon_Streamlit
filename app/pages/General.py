import pandas as pd
import streamlit as st
import plotly.express as px


# function to show the stats for abilities for all weapons
def Show_Ability_Stats(selected_Sub, colour1, colour2):
    # load the data
    ability_stats_df = selected_Sub
    # count of the number of builds
    Builds_count = ability_stats_df.iloc[0]
    Builds_count = Builds_count.iloc[-1]
    # obtaining values from all the trackable ability columns
    track_abilities_df = ability_stats_df.iloc[:, -15:-1]
    track_abilities_df = track_abilities_df.iloc[0].reset_index()
    # Defining new columns for Abilities and Ability Points
    # The column names act as categories for the bar chart
    track_abilities_df.columns = ['Abilities', 'Ability Points (AP)']
    # rounding
    track_abilities_df['Ability Points (AP)'] = (
        track_abilities_df['Ability Points (AP)']).round(4)
    st.divider()
    # Message showing how many builds this weapon Sub has
    message = f"Analysis based on {Builds_count} Builds"
    st.markdown(
        f"<h2 style='text-align: left;'>{message}</h2>",
        unsafe_allow_html=True
    )
    st.divider()
    # bar chart 1
    # for showing ability points for trackable abilities
    fig = px.bar(track_abilities_df,
                 x='Abilities', y='Ability Points (AP)',
                 title="Average ability points for all weapons",
                 color='Ability Points (AP)',
                 color_continuous_scale=[colour1, colour2])
    # fig.update_traces(marker_color=colour2)
    fig.update_layout(
        title_font=dict(size=20),
    )
    # show the bar chart
    st.plotly_chart(fig)
    # next do non trackable abilities
    non_track_abilities_df = ability_stats_df.iloc[:, 1:12]
    non_track_abilities_df = non_track_abilities_df.iloc[0].reset_index()
    non_track_abilities_df.columns = ['Abilities',
                                      'Percentage of Builds Using (%)']
    # do *100 to decimal values to get percentages
    non_track_abilities_df['Percentage of Builds Using (%)'] = (
        non_track_abilities_df['Percentage of Builds Using (%)']
        * 100).round(4)
    # bar chart 2
    fig2 = px.bar(
        non_track_abilities_df,
        x='Abilities',
        y='Percentage of Builds Using (%)',
        title=(
            "Usage of primary only abilities for on all weapons"
        ),
        color='Percentage of Builds Using (%)',
        color_continuous_scale=[colour1, colour2]
    )
    fig2.update_layout(
        title_font=dict(size=20),
    )
    # show bar chart
    st.plotly_chart(fig2)


df = pd.read_csv("../data/All_ability_means.csv")

c1 = "#EB7724"
c2 = "#1D92FD"

Show_Ability_Stats(df, c1, c2)
