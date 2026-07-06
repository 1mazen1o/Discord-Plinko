# Discord Plinko

A Plinko simulation that uses Discord users' profile pictures as the falling pieces. Users can join the game by sending `!join` in Discord, and their avatar will automatically appear in the simulation.

Before running the project, make sure you have:

- An empty folder named `DiscordImages`
- The following sound files in the project directory


Players can join the game by typing:

```
!join
```

Their Discord avatar will automatically be downloaded and added to the Plinko simulation.

## Notes

- You must have a `DiscordImages` folder to recive avatar pngs.
- `avatar.py` handles downloading Discord avatars.
- `main.py` runs the Plinko simulation and automatically loads new avatars as they appear.
