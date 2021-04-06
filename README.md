# NumberGame
This is a game, which is described in README, and an ai bot to play the game against you.

In the beginning of the game you need to think of a 4 digit number which has different digits and does not start with a 0.
For each turn, the bot will make a guess and the you will return (row after row) you two numbers (+p and -n) which means:
  +p => there are p numbers which are in the same positions and have the same values with digits of your opponent's number.
  -n => there are n numbers which are in the different positions and have the same values with digits of your opponent's number.
  
For example bot's guess is 4012 and your number is 3028, then your response will be +1 -1 (for the digits 0 and 2).

After you write the answer the same thing will happen but this time you will make a guess and bot will return the answer.

The first one finds the number of their opponent is the one who wins the game.

This game seems like it is easy to play and making guesses is not that hard but when you play you will realize that this is not that easy, believe me.

I learned this game from my father and he was good at it. So I built this bot for him first and relised this bot is quite fine for this game and so I decided to publish it.
I hope you'll enjoy it too :)
