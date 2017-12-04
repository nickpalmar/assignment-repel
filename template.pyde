# Repel Program
# Create functionality that will have sprites move away from the mouse.

# GLOBAL VARIABLES
# Get your color scheme from https://coolors.co/
player_color = "#A4B0F5"
npc_color = "#F58F29"
bg_color = "#4464AD"


def setup():
    size(400, 400)

    
def draw():
    background(bg_color)
    
    # Draw Player
    noStroke()
    fill(player_color)
    ellipse(50, 50, 50, 50)
    
    # Draw NPC Sprite
    fill(npc_color)
    ellipse(100, 100, 30, 30)
    
