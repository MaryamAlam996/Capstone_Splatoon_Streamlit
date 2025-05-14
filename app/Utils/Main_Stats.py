import pandas as pd
import streamlit as st
import plotly.express as px


# function to show all stats on the main weapon page
def Show_Main_Stats(selected_weapon, colour1, colour2):
    Show_Ability_Stats(selected_weapon, colour1, colour2)
    Show_Modes_Stats(selected_weapon, colour1, colour2)


# function to show the stats for abilities for a main weapon
def Show_Ability_Stats(selected_weapon, colour1, colour2):
    # load the data
    all_ability_stats_df = pd.read_csv("../data/Weapon_ability_means.csv")
    # Only get data of the chosen weapon
    ability_stats_df = all_ability_stats_df[
        all_ability_stats_df['Weapon_Name'] == selected_weapon
        ]
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
    # Message showing how many builds this main weapon has
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
                 title=f"Average ability points for {selected_weapon} builds",
                 color='Ability Points (AP)',
                 color_continuous_scale=[colour1, colour2])
    # fig.update_traces(marker_color=colour2)
    fig.update_layout(
        title_font=dict(size=20),
    )
    # show the bar chart
    st.plotly_chart(fig)
    # next do non trackable abilities
    non_track_abilities_df = ability_stats_df.iloc[:, 9:20]
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
            f"Usage of primary only abilities for {selected_weapon} builds"
        ),
        color='Percentage of Builds Using (%)',
        color_continuous_scale=[colour1, colour2]
    )
    fig2.update_layout(
        title_font=dict(size=20),
    )
    # show bar chart
    st.plotly_chart(fig2)


# function to show mode stats for the main weapon
def Show_Modes_Stats(selected_weapon, colour1, colour2):
    st.divider()
    # load the data
    all_mode_stats_df = pd.read_csv("../data/Game_mode_by_Weapon.csv")
    # filter by weapon name
    mode_stats_df = all_mode_stats_df[
        all_mode_stats_df['Weapon_Name'] == selected_weapon]
    # set up custom colours
    custom_colors_A = [colour1, colour2]
    custom_colors_B = ["#EB7724", "#0C1EBF", "#DB216F", "#31C11F", "#E5C215"]
    custom_colors_C = ["#0E45C7", "#2AF0D6", "#1D92FD", "#F74B38",
                       "#8C1CCD", "#31333E"]
    # columns for counting number of modes
    mode_count_df = mode_stats_df.iloc[:, -6:-1]
    mode_count_df = mode_count_df.iloc[0].reset_index()
    mode_count_df.columns = ['Number of modes', 'Number of Builds']
    # pie chart
    fig3 = px.pie(mode_count_df,
                  values='Number of Builds',
                  names='Number of modes',
                  title='Number of modes for each build',
                  color='Number of modes',
                  color_discrete_sequence=custom_colors_B)
    # columns for mode specific builds
    mode_only_df = mode_stats_df.iloc[:, 1:7]
    mode_only_df = mode_only_df.iloc[0].reset_index()
    mode_only_df.columns = ['One Mode Specific builds', 'Number of Builds']
    # pie chart
    fig4 = px.pie(mode_only_df,
                  values='Number of Builds',
                  names='One Mode Specific builds',
                  title='Mode specific builds',
                  color='One Mode Specific builds',
                  color_discrete_sequence=custom_colors_C)
    # columns for turf war
    mode_turf_df = mode_stats_df.iloc[:, 7:9]
    mode_turf_df = mode_turf_df.iloc[0].reset_index()
    mode_turf_df.columns = ['Turf War Inclusion', 'Number of Builds']
    # pie chart
    fig5 = px.pie(mode_turf_df,
                  values='Number of Builds',
                  names='Turf War Inclusion',
                  title='Turf War builds',
                  color='Turf War Inclusion',
                  color_discrete_sequence=custom_colors_A)
    # columns for zones
    mode_zones_df = mode_stats_df.iloc[:, 9:11]
    mode_zones_df = mode_zones_df.iloc[0].reset_index()
    mode_zones_df.columns = ['Splat Zones Inclusion', 'Number of Builds']
    # pie chart
    fig6 = px.pie(mode_zones_df,
                  values='Number of Builds',
                  names='Splat Zones Inclusion',
                  title='Splat Zones War builds',
                  color='Splat Zones Inclusion',
                  color_discrete_sequence=custom_colors_A)
    # columns for rainmaker
    mode_rain_df = mode_stats_df.iloc[:, 11:13]
    mode_rain_df = mode_rain_df.iloc[0].reset_index()
    mode_rain_df.columns = ['Rainmaker Inclusion', 'Number of Builds']
    # pie chart
    fig7 = px.pie(mode_rain_df,
                  values='Number of Builds',
                  names='Rainmaker Inclusion',
                  title='Rainmaker War builds',
                  color='Rainmaker Inclusion',
                  color_discrete_sequence=custom_colors_A)
    # columns for tower control
    mode_tower_df = mode_stats_df.iloc[:, 13:15]
    mode_tower_df = mode_tower_df.iloc[0].reset_index()
    mode_tower_df.columns = ['Tower Control Inclusion', 'Number of Builds']
    # pie chart
    fig8 = px.pie(mode_tower_df,
                  values='Number of Builds',
                  names='Tower Control Inclusion',
                  title='Tower Control builds',
                  color='Tower Control Inclusion',
                  color_discrete_sequence=custom_colors_A)
    # columns for clam blitz
    mode_clam_df = mode_stats_df.iloc[:, 15:17]
    mode_clam_df = mode_clam_df.iloc[0].reset_index()
    mode_clam_df.columns = ['Clam Blitz Inclusion', 'Number of Builds']
    # pie chart
    fig9 = px.pie(mode_clam_df,
                  values='Number of Builds',
                  names='Clam Blitz Inclusion',
                  title='Clam Blitz builds',
                  color='Clam Blitz Inclusion',
                  color_discrete_sequence=custom_colors_A)
    # updating the look of each
    fig3.update_layout(
        title_font=dict(size=25),
        title_x=0.025
    )
    fig4.update_layout(
        title_font=dict(size=25)
    )
    fig5.update_layout(
        title_font=dict(size=20),
        title_x=0.05
    )
    fig6.update_layout(
        title_font=dict(size=20)
    )
    fig7.update_layout(
        title_font=dict(size=20)
    )
    fig8.update_layout(
        title_font=dict(size=20)
    )
    fig9.update_layout(
        title_font=dict(size=20)
    )
    # set up column layout
    mode_col_A, mode_col_B, mode_col_C = st.columns(3)
    # display pie charts
    with mode_col_A:
        st.plotly_chart(fig5)
    with mode_col_B:
        st.plotly_chart(fig6)
    with mode_col_C:
        st.plotly_chart(fig7)
    # set up column layout
    a, mode_col_D, mode_col_E, b = st.columns([1, 3, 3, 1])
    # display pie charts
    with mode_col_D:
        st.plotly_chart(fig8)
    with mode_col_E:
        st.plotly_chart(fig9)
        # set up column layout
    st.divider()
    mode_col_1, mode_col_2 = st.columns(2)
    # display pie charts
    with mode_col_1:
        st.plotly_chart(fig3)
        fig3.update_layout(
            title_font=dict(size=20),
            title_x=0.1
        )
    with mode_col_2:
        st.plotly_chart(fig4)
