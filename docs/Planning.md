# Project Planning (Draft)

## The Project

I have chosen to base my capstone project on analyzing the strategies used by competitive players in **Splatoon 3**.  
As someone who plays the game casually, I have a very limited knowledge of the game's competitive scene.  
One area I am curious about is **gear builds**, which is what I will be focusing my analysis on.

<img src="S3_art_3D_teams_yellow_vs_blue.png" alt="Teams Yellow vs Blue" width="600"/>

## What is Splatoon?

<img src="S3_first_twitter_preview_-_spawners.jpg" alt="Spawners" width="400"/>

**Splatoon** is an online multiplayer shooter developed by Nintendo.  
In this game, you play as either an Inkling or an Octoling in online 4v4 battles.  
There are multiple modes with the main casual mode being **Turf War** and the more competitive modes being **Splat Zones**, **Rainmaker**, **Tower Control**, and **Clam Blitz**.

<img src="2.png" alt="Weapons" width="400"/>

The game has **11 weapon classes** and a total of **143 weapon kits** to choose from.  
Each main weapon comes with a predefined **sub weapon** and **special weapon**.  
There are **14 different sub weapons** and **19 different special weapons** in the game.

<img src="1.png" alt="Gear" width="400"/>

Along with choosing a weapon, players can also choose their **gear**, which includes headgear, clothing, and shoes.  
Each piece of gear comes with abilities that apply effects to help the player in battle, for example *"Run Speed Up"* increases a player's speed when running.

A majority of these abilities can be **stacked** to increase their effect.  
The effect of a stackable ability is tracked using **Ability Points (AP)**:  
- **Main ability** = 10 AP  
- **Sub ability** = 3 AP  

Non-stackable abilities usually have unique effects and only appear as the **main ability** on a specific gear piece (e.g., *Stealth Jump* only appears on shoes).

---

<p align="center">
  <img src="S3_Splatfest_World_Premiere_Weapon_promo.jpg" alt="Weapon Promo" width="45%" style="display: inline-block; margin-right: 10px;">
  <img src="S3_Gear_Abilities_promo.jpg" alt="Gear Abilities Promo" width="45%" style="display: inline-block;">
</p>




## Analysis

My goal of this project is to perform analysis based on gear builds made by players. Gear builds are the set of gear a player designs with abilities suited for a specific weapon (with some also designed with certain game modes in mind). Different weapons have different strengths and weaknesses thus encouraging different play styles, this leads competitive players to create builds accordingly. For example having more ink saver main for weapons that run out of ink quickly. 

I will be focusing on analyzing the difference between gear builds used for different weapons (as well as between classes, subs and specials). I will be using the website sendou.ink as competitive players often use it to share their personal gear builds alongside what modes and weapons they use them for. I will also be using data from inkepedia to further enrich the build data collected from sendou. 



## Data sources:

[**sendou.ink**](https://sendou.ink)  
> "sendou.ink is a Splatoon resource website created by Sendou and others, and features tiering for higher-level competitive players, upcoming events, rotations, Splatoon gear builds and analysis, and more."  
> — [splatoonwiki.org](https://splatoonwiki.org/wiki/Competitive:Sendou#:~:text=ink,builds%20and%20analysis%2C%20and%20more.)

[**Inkepedia**](https://splatoonwiki.org/wiki/Main_Page)  
> A wiki made by fans which contains resources such as images and further information on individual weapons.




## User stories:
As a user,
I want the app to gracefully handle network errors,
so that it does not crash when loading images for example

As a user,
I want the extracted data which describes each weapon to be up-to-date,
so that I can ensure that with future game updates the information shown is accurate

As a user,
I want the data to not include any repeats (such as weapon reskins),
so that the data is concise

As a user,
I want the data to not include any builds that are all of the same ability,
so that the data is not skewed by impractical builds

As a user,
I want the to be able to filter builds by weapon, weapon class, sub and special
so that I can see what abilities are commonly recommended for each

As a user,
I want the to be able to filter builds by game mode
so that I can see what abilities are commonly recommended for each

As a user,
I want to be able to view visualizations for each weapon,
so that I can easily see correlations between the weapon and the most used abilities



