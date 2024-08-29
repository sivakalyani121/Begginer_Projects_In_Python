
# **Higher or Lower Game**

This Python program is a fun and interactive game where the player guesses which of two social media personalities has more followers. The game continues as long as the player guesses correctly, and the score increases with each correct answer.

## **Features**

- **Compare Two Accounts**: The player is presented with two random social media accounts, each with its name, description, and country of origin.
- **Guess the Higher Follower Count**: The player guesses which account has more followers.
- **Score Tracking**: The player's score increases with each correct guess. The game continues until the player makes a wrong guess, after which the final score is displayed.
- **User Interaction**: The game interacts with the player through text-based inputs and outputs, making it easy and engaging to play.

## **Dependencies**

- **game_art**: This module contains the ASCII art used in the game for visual appeal.
- **game_database**: This module contains the data of the social media personalities (like names, follower counts, descriptions, and countries).

## **How to Play**

1. **Start the Game**: When you run the program, it will display the game art and initiate the first comparison between two accounts.

2. **Make a Guess**: You will see two accounts with some details. Guess which account has more followers by typing '1' for the first account or '2' for the second account.

3. **Check Your Answer**: After you make your guess, the program will reveal the follower counts and tell you if you are correct. If you are correct, your score increases, and the game continues with a new account to compare against the previous winner.

4. **Continue or End**: The game continues until you make a wrong guess. Your final score will be displayed, and the game will end.

## **Example Usage**

```plaintext
Welcome to the Higher or Lower Game!
Compare 1: John Doe, a popular musician, from the USA
VS
Compare 2: Jane Smith, a famous actress, from the UK
1. Who has more followers? Type '1' or '2': 1
Correct! Your score is 1.

Next Round:
Compare 1: Jane Smith, a famous actress, from the UK
VS
Compare 2: Alice Johnson, a top model, from Australia
2. Who has more followers? Type '1' or '2': 2
Sorry, that's incorrect. Your final score is 1.
```

