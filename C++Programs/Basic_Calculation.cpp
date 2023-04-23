#include <iostream>
#include <cmath>

int main() {
    int List1[1000];
    int n = 0;
    int sum = 0;
    int x{};
    while (x != -999) {
        std::cin >> x;
        if (x != -999) {
            List1[n] = x;
            sum = sum + List1[n] * (int)std::pow(-1, n);
            n++;
        }
    }
    std::cout << sum << std::endl;
    return 0;
}

//calculate a list of numbers
//1 2 3 4 5 = 1 - 2 + 3 - 4 + 5
