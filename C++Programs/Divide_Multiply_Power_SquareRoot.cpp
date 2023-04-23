#include <iostream>
#include <cmath>
#include<iomanip>

int main() {
    int first_input;
    double second_input;
    double third_input;
    std::cout << "MENU" << std::endl;
    std::cout << "     1.Divide, a/b" << std::endl;
    std::cout << "     2.Multiply, a*b" << std::endl;
    std::cout << "     3.Power, a^b" << std::endl;
    std::cout << "     4.Square root, sqrt(a)" << std::endl;
    std::cout << "Enter your choice:" << std::endl;
    std::cin>>first_input;

    switch (first_input) {
        case 1:
            std::cout << "Enter two numbers:" << std::endl;
            std::cin >> second_input >> third_input;
            std::cout << second_input << "/" << third_input << "=" << std::fixed << std::setprecision(3) << second_input / third_input << std::endl;
            break;

        case 2:
            std::cout << "Enter two numbers:" << std::endl;
            std::cin >> second_input >> third_input;
            std::cout << second_input << "*" << third_input << "=" << std::fixed << std::setprecision(3) << second_input * third_input << std::endl;
            break;

        case 3:
            std::cout << "Enter two numbers:" << std::endl;
            std::cin >> second_input >> third_input;
            std::cout << second_input << "^" << third_input << "=" << std::fixed << std::setprecision(3) << pow(second_input , third_input) << std::endl;
            break;

        case 4:
            std::cout << "Enter a number:" << std::endl;
            std::cin >> second_input;
            std::cout << "sqrt(" << second_input << ")" << "=" << std::fixed << std::setprecision(3) << sqrt(second_input) << std::endl;
            break;

    }


    return 0;
}


// Input 1 2 3 4 to choice the function
