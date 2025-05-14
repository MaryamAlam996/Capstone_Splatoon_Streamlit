

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