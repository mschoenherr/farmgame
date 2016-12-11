#Farmgame

This is a simple farmgame I made with kivy. The code reflects the fact that I used this project to learn the kivy platform und is probably not very aesthetic. This game is not yet playable, since the game model is still in pre-alpha.

I tried to seperate the model from the rest, but found kivys way of updating nested properties cumbersome. To facilitate development, the app holds the game in an ObjectProperty. Updates are propagated by copying the whole GameState, which is rather hackish.

All images included are public domain.
