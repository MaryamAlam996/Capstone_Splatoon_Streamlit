import pandas as pd
import streamlit as st
import plotly.express as px
from app.Utils.ability_image import Show_Ability_Image


# function to show the stats for abilities
def Show_Ability_Stats(df):
    # finding the column names of the dataframe
    col_names = list(df.columns.values)
    # name of abilities
    ability_list = col_names[9:-1]
    # selecting an ability from the list
    selected_ability = st.selectbox("Choose an ability", ability_list)
    st.divider()
    # st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center;'>{selected_ability}</h1>",
                unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
    # loading the ability image dataframe
    ability_img_df = pd.read_csv("../data/ability_img.csv")
    # image of the selected ability
    selected_img_df = ability_img_df[
        ability_img_df['Abilities'] == selected_ability]
    selected_img = selected_img_df.iloc[0, 1]
    # showing the image of the selected ability
    Show_Ability_Image(selected_img)
    # showing the stats of the selected ability
    show_weapon_stats(selected_ability)
    show_class_stats(selected_ability)
    show_sub_stats(selected_ability)
    show_special_stats(selected_ability)
    number_of_AP_2(selected_ability)
    return None


# function to show the the top 15 weapons that use the selected ability
def show_weapon_stats(selected_ability):
    # sort the dataframe by the selected ability
    df_A = df.sort_values(by=[selected_ability], ascending=False)
    # get the top 15 rows of the sorted dataframe
    top_df = df_A.head(15)
    # create a bar chart using Plotly Express
    fig = px.bar(
        top_df,
        x='Weapon_Name',
        y=selected_ability,
        title=(
            f"Top 15 weapons that use the most "
            f"{selected_ability} in their builds"
        ),
        color=selected_ability,
        color_continuous_scale=['#232323', "#B3F73D"]
    )
    fig.update_layout(
        title_font=dict(size=20),
    )
    # show the bar chart in Streamlit
    st.plotly_chart(fig)


# function to show the top 11 classes that use the selected ability
def show_class_stats(selected_ability):
    df_class = pd.read_csv("../data/Weapon_Class_ability_means.csv")
    df_A = df_class.sort_values(by=[selected_ability], ascending=False)
    top_df = df_A.head(11)
    fig = px.bar(
        top_df,
        x='Class', y=selected_ability,
        title=(
            "Weapon classes sorted by how much "
            f"{selected_ability} in their builds"
        ),
        color=selected_ability,
        color_continuous_scale=['#232323', "#FACA37"]
    )
    # fig.update_traces(marker_color=colour2)
    fig.update_layout(
        title_font=dict(size=20),
    )
    st.plotly_chart(fig)


# function to show the top 14 sub weapons that use the selected ability
def show_sub_stats(selected_ability):
    df_class = pd.read_csv("../data/Sub_Weapon_ability_means.csv")
    df_A = df_class.sort_values(by=[selected_ability], ascending=False)
    top_df = df_A.head(14)
    fig = px.bar(
        top_df,
        x='Sub_Weapon', y=selected_ability,
        title=(
            "Sub Weapons sorted by how much "
            f"{selected_ability} in their builds"
        ),
        color=selected_ability,
        color_continuous_scale=['#232323', "#EC471E"]
    )
    # fig.update_traces(marker_color=colour2)
    fig.update_layout(
        title_font=dict(size=20),
    )
    st.plotly_chart(fig)


# function to show the top 19 special weapons that use the selected ability
def show_special_stats(selected_ability):
    df_class = pd.read_csv("../data/Special_Weapon_ability_means.csv")
    df_A = df_class.sort_values(by=[selected_ability], ascending=False)
    top_df = df_A.head(19)
    fig = px.bar(
        top_df,
        x='Special_Weapon', y=selected_ability,
        title=(
            f"Special Weapons sorted by how much "
            f"{selected_ability} in their builds"
        ),
        color=selected_ability,
        color_continuous_scale=['#232323', "#F3338C"]
    )
    # fig.update_traces(marker_color=colour2)
    fig.update_layout(
        title_font=dict(size=20),
    )
    st.plotly_chart(fig)


# function to show how many AP points are used for the selected ability
def number_of_AP(selected_ability):
    df_builds = pd.read_csv("../data/Ability_Point_builds.csv")
    count = df_builds[selected_ability].value_counts()
    # Create a DataFrame from the value counts
    count_df = count.reset_index()
    count_df.columns = ['Ability', 'Count']
    # Plotly pie chart
    fig = px.pie(
        count_df, names='Ability', values='Count',
        title=f'Distribution of {selected_ability} Abilities'
    )
    # Display the chart in Streamlit
    st.plotly_chart(fig)


# function to show how many AP points are used for the selected ability
def number_of_AP_2(selected_ability):
    df_builds = pd.read_csv("../data/Ability_Point_builds.csv")
    # st.dataframe(df_builds)
    # Count occurrences
    count = df_builds[selected_ability].value_counts()
    # Convert to DataFrame and rename columns
    count_df = count.reset_index()
    count_df.columns = ['Ability', 'Count']

    # Group ability points into bins
    # Bin edges
    bins = [-1, 0, 1, 3, 6, 9, 10, 13, 16, 19, float('inf')]
    # Group labels
    labels = ['0', '1', '3', '6', '9', '10', '13', '16', '19', '20+']
    # Create a new column with binned values
    count_df['Group'] = pd.cut(count_df['Ability'], bins=bins, labels=labels)
    # Aggregate counts by group
    grouped_df = count_df.groupby('Group')['Count'].sum().reset_index()

    # Plotly pie chart
    fig2 = px.pie(
        grouped_df, names='Group', values='Count',
        title=f'Grouped Distribution of {selected_ability} Abilities'
    )
    # Display the chart in Streamlit
    st.plotly_chart(fig2)


# Load the data
df = pd.read_csv("../data/Weapon_ability_means.csv")

# Call the function to show ability stats
Show_Ability_Stats(df)
