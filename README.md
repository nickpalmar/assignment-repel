# Repel
This will be a sketch that is more about sprite interactivity than a game.
## The Goal
Your program will feature two non-player sprites and one player sprite. The player sprite will be controlled by the mouse. When the player sprite gets close (not touching yet) the non-player sprites will move away from the player. As though they were trying to avoid it. If the player catches the sprite, the player gets a point.

You will do this in assigned groups of three. It will require you to fully understand the visual space and as such, I will require each group to come up with a visual plan of how they will achieve this functionality.

Some useful concepts that can help you achieve this functionality are:
- [`PVector`](https://processing.org/reference/PVector.html)
  - [`v1.add(v2)`]() - Add one vector to another (For increasing speed, applying friction, or gravity)
  - [`PVector.sub(v1, v2)`](https://processing.org/reference/PVector_sub_.html) - Get the difference between two vectors
  - [`vector.heading()`](https://processing.org/reference/PVector_heading_.html) - Gives you the angle (direction) of a vector
  - [`vector.mag()`](https://processing.org/reference/PVector_mag_.html) - Gives you the distance or magnitude of a vector
  
