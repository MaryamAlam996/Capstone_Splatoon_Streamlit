import pandas as pd
import streamlit as st
import plotly.express as px
# from app.Utils.ability_image import Show_Ability_Image
# from app.Utils.ability_image import Show_2_Ability_Image
import ast


# function to calculate means of numeric columns
def calculate_numeric_means(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate mean values for all numeric columns in the DataFrame."""
    means = df.select_dtypes(include='number').mean()
    return means.to_frame(name='Mean').T


# function to show the stats for modes
def Show_Mode_Stats(df: pd.DataFrame):
    # Convert string representations to actual lists
    df['Game_Modes'] = df['Game_Modes'].apply(lambda x: ast.literal_eval(x))
    st.title("Filter Builds by Game Mode")
    # Extract all unique game modes
    unique_items = sorted(
        {item for sublist in df['Game_Modes'] for item in sublist})
    st.write("### Select the set of game modes")
    # select game modes using checkboxes
    selected_items = [item for item in unique_items if st.checkbox(item)]
    # if statement to check if any items are selected
    if selected_items:
        # Filter rows where Game_Modes exactly matches selected_items
        filtered_df = df[df['Game_Modes'].apply(
            lambda x: sorted(x) == sorted(selected_items))]
        count = len(filtered_df)
        st.write(f"### Number of Builds: {count}")
        st.write("### Filtered Rows")
        st.dataframe(filtered_df)
        # if there are any builds, calculate means
        if count > 0:
            numeric_means = calculate_numeric_means(filtered_df)
        else:
            st.write("No builds to calculate means for.")
    # if no items are selected, show all data
    else:
        st.write("No items selected. Showing all data.")
        count = len(df)
        st.write(f"### Number of Builds: {count}")
        st.write("### All Rows")
        st.dataframe(df)
        numeric_means = calculate_numeric_means(df)
    # Show the ability stats for the selected modes
    Show_Ability_Stats(numeric_means)


# function to show the stats for abilities
def Show_Ability_Stats(selected_weapon):
    # selected_weapon is supposed to be a the selected mode (copied code)
    # load the data
    # all_ability_stats_df = pd.read_csv("../data/Weapon_ability_means.csv")
    # Only get data of the chosen weapon
    ability_stats_df = selected_weapon
    # count of the number of builds
    Builds_count = ability_stats_df.iloc[0]
    Builds_count = Builds_count.iloc[-1]
    # obtaining values from all the trackable ability columns
    track_abilities_df = ability_stats_df.iloc[:, -14:]
    track_abilities_df = track_abilities_df.iloc[0].reset_index()
    # Defining new columns for Abilities and Ability Points
    # The column names act as categories for the bar chart
    track_abilities_df.columns = ['Abilities', 'Ability Points (AP)']
    # rounding
    track_abilities_df['Ability Points (AP)'] = (
        track_abilities_df['Ability Points (AP)']).round(4)
    # bar chart 1
    # for showing ability points for trackable abilities
    fig = px.bar(track_abilities_df,
                 x='Abilities', y='Ability Points (AP)',
                 title="Average ability points for selected mode(s) builds",
                 color='Ability Points (AP)',
                 color_continuous_scale=["#FF0000", "#3700FF"])
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
            "Usage of primary only abilities for selected mode(s) builds"
        ),
        color='Percentage of Builds Using (%)',
        color_continuous_scale=["#FF0000", "#3700FF"])
    fig2.update_layout(
        title_font=dict(size=20),
    )
    # show bar chart
    st.plotly_chart(fig2)


df = pd.read_csv("../data/Ability_Point_Builds.csv")

Show_Mode_Stats(df)
