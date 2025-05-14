

# function that returns a unique colour
# for each weapon class
# to be used in visuals
def class_to_colour(w_class):
    if w_class == "Shooter":
        block_colour = "#EB7724"
    elif w_class == 'Blaster':
        block_colour = "#F74B38"
    elif w_class == "Splatana":
        block_colour = "#E5C215"
    elif w_class == "Charger":
        block_colour = "#A0C63A"
    elif w_class == "Splatling":
        block_colour = "#1AB93D"
    elif w_class == "Brella":
        block_colour = "#48E39E"
    elif w_class == "Stringer":
        block_colour = "#1D92FD"
    elif w_class == "Roller":
        block_colour = "#0E45C7"
    elif w_class == "Slosher":
        block_colour = "#6823F5"
    elif w_class == "Brush":
        block_colour = "#A94CC7"
    elif w_class == "Dualie":
        block_colour = "#DB216F"
    else:
        block_colour = "#242424"
    return block_colour


# function that returns a unique image
# for each class
# large splat visuals
def class_to_big_splat(w_class):
    if w_class == "Shooter":
        big_splat = "Shooter.png"
    elif w_class == 'Blaster':
        big_splat = "Blaster.png"
    elif w_class == "Splatana":
        big_splat = "Splatana.png"
    elif w_class == "Charger":
        big_splat = "Charger.png"
    elif w_class == "Splatling":
        big_splat = "Splatling.png"
    elif w_class == "Brella":
        big_splat = "Brella.png"
    elif w_class == "Stringer":
        big_splat = "Stringer.png"
    elif w_class == "Roller":
        big_splat = "Roller.png"
    elif w_class == "Slosher":
        big_splat = "Slosher.png"
    elif w_class == "Brush":
        big_splat = "Brush.png"
    elif w_class == "Dualie":
        big_splat = "Dualie.png"
    else:
        big_splat = "Shooter.png"
    return big_splat


# Another function to return a unique image
# for each class
# small splat visuals
def class_to_small_splat(w_class):
    if w_class == "Shooter":
        big_splat = "Shooter_1.png"
    elif w_class == 'Blaster':
        big_splat = "Blaster_1.png"
    elif w_class == "Splatana":
        big_splat = "Splatana_1.png"
    elif w_class == "Charger":
        big_splat = "Charger_1.png"
    elif w_class == "Splatling":
        big_splat = "Splatling_1.png"
    elif w_class == "Brella":
        big_splat = "Brella_1.png"
    elif w_class == "Stringer":
        big_splat = "Stringer_1.png"
    elif w_class == "Roller":
        big_splat = "Roller_1.png"
    elif w_class == "Slosher":
        big_splat = "Slosher_1.png"
    elif w_class == "Brush":
        big_splat = "Brush_1.png"
    elif w_class == "Dualie":
        big_splat = "Dualie_1.png"
    else:
        big_splat = "Shooter_1.png"
    return big_splat
