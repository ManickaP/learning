#include <iostream>

int main(int argc, char** argv) {
    if (argc > 1) {
        std::cout << "Hello " << argv[1] << std::endl;
        return 0;
    } else {
        return 1;
    }
}