#include "complexe.h"
#include <iostream>

int main() {
    complexe z1(2.0, 3.0);
    complexe z2;
    bool a;
    a = z1.Identical(z2);
    std::cout << "a: " << a << std::endl;
    return 0;
}
