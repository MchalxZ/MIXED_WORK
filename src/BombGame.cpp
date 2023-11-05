#include <iostream>
#include <ctime>
#include <cstdlib>

int main() {
    std::srand(static_cast<unsigned>(std::time(nullptr)));

    int secretNumber = std::rand() % 100 + 1; 
    int guess;
    int attempts = 0;
    int balance = 100; 
    int bet;

    std::cout << "Welcome to the Guessing Boom Game!" << std::endl;
    std::cout << "Auto-generated random number between 1 and 100. Try to guess it." << std::endl;

    std::cout << "Your initial balance is: " << balance << std::endl;

    while (balance > 0) {
        std::cout << "Enter your bet (0 to quit): ";
        std::cin >> bet;
        
        if (bet == 0) {
            break;
        }
        
        if (bet > balance) {
            std::cout << "Your bet exceeds your current balance. Enter a smaller bet." << std::endl;
            continue;
        }

        std::cout << "Enter your guess: ";
        std::cin >> guess;
        attempts++;
        
        if (guess < secretNumber) {
            std::cout << "Incorrect, Try higher." << std::endl;
            balance -= bet;
        } else if (guess > secretNumber) {
            std::cout << "Incorrect, Try lower." << std::endl;
            balance -= bet;
        } else {
            std::cout << "Congratulations! You guessed the correct number: " << secretNumber << std::endl;
            std::cout << "You won " << bet << " in this game!" << std::endl;
            balance += bet;
            std::cout << "Latest balance: " << balance << std::endl;
            
            secretNumber = std::rand() % 100 + 1; 
            attempts = 0;
        }
    }

    std::cout << "Game over. Your final balance is: " << balance << std::endl;

    return 0;
}
