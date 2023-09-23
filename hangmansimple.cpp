#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>

// Function to check if a character is present in the word
bool isCharPresent(const std::string& word, char guess) {
    for (char c : word) {
        if (c == guess) {
            return true;
        }
    }
    return false;
}

// Function to update the hidden word with correctly guessed characters
void updateHiddenWord(const std::string& word, std::string& hiddenWord, char guess) {
    for (int i = 0; i < word.length(); ++i) {
        if (word[i] == guess) {
            hiddenWord[i] = guess;
        }
    }
}

// Function to print the hangman ASCII art
void printHangman(int attempts) {
    std::vector<std::string> hangmanArt = {
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    };

    if (attempts >= 1) {
        hangmanArt[2] = "  O   |";
    }
    if (attempts >= 2) {
        hangmanArt[3] = "  |   |";
    }
    if (attempts >= 3) {
        hangmanArt[3] = " \\|   |";
    }
    if (attempts >= 4) {
        hangmanArt[3] = " \\|/  |";
    }
    if (attempts >= 5) {
        hangmanArt[4] = "  |   |";
    }
    if (attempts >= 6) {
        hangmanArt[5] = " /    |";
    }
    if (attempts >= 7) {
        hangmanArt[5] = " / \\  |";
    }

    for (const std::string& line : hangmanArt) {
        std::cout << line << std::endl;
    }
}

int main() {
    // Set up random seed
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    // Word bank
    std::vector<std::string> words = {
        "hangman",
        "computer",
        "programming",
        "game",
        "player",
        "guess"
    };

    // Select a random word from the word bank
    std::string word = words[std::rand() % words.size()];

    std::string hiddenWord(word.length(), '_');
    int attempts = 0;
    std::string guessedChars;

    // Game loop
    while (hiddenWord != word && attempts < 7) {
        std::cout << "Guess the word: " << hiddenWord << std::endl;
        std::cout << "Attempts left: " << 7 - attempts << std::endl;
        std::cout << "Guessed characters: " << guessedChars << std::endl;

        char guess;
        std::cout << "Enter your guess: ";
        std::cin >> guess;

        // Check if the character has already been guessed
        if (guessedChars.find(guess) != std::string::npos) {
            std::cout << "You've already guessed that character. Try again." << std::endl;
            continue;
        }

        // Add the guessed character to the guessedChars string
        guessedChars += guess;

        // Check if the character is present in the word
        if (isCharPresent(word, guess)) {
            updateHiddenWord(word, hiddenWord, guess);
        } else {
            attempts++;
        }

        // Print the hangman
        printHangman(attempts);
    }

    // Game over
    if (hiddenWord == word) {
        std::cout << "Congratulations! You guessed the word: " << word << std::endl;
    } else {
        std::cout << "Game over! The word was: " << word << std::endl;
        printHangman(attempts);
    }

    return 0;
}
