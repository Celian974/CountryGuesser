# CountryGuesser

Description:

This is a simple terminal-based game where players try to guess the names of all 196 countries of the world. The game is interactive, and players can enter country names one by one, with the goal of finding all the countries.

The game uses the colorama module to add colors to the text for a more engaging experience.

Features:
 - Guess the Country: Type the name of a country and see if it's correct.
 - Case Insensitive Input: You can type countries name in any case wether it is lowercase, uppercase, or even a mix of both.
 - Progress Tracker: The game shows how many countries have been correctly guessed and how many are still left.
 - Exit Option: Type 'exit' at any time to quit the game.
 - Found Countries Display: Type 'found' to see a list of all the countries you've correctly guessed.

Installation:
- Install Python: Make sure Python is installed on your system. If not, download and install it from python.org.

- Install the colorama package: The game uses the colorama package to colorize text in the terminal.

  To install it, run the following command:

  ```
  pip install colorama
  ```

How to Play:
- Clone or download this repository.

- Run the Python script using Make:
  ```
  make
  ```

The game will prompt you to enter a country. Type the name of a country and press Enter.

The game will inform you if the guess is correct or not. If correct, it will update the number of remaining countries to guess.

If you wish to see the countries you have already found, type 'found'.

To exit the game at any time, type 'exit'.
