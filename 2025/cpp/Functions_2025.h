#ifndef FUNCTIONS_2025_H
#define FUNCTIONS_2025_H

#include <string>
#include <vector>

// Data structure
struct Rotation {
    char direction;
    int rotation_value;
};

// Functions
std::vector<std::string> read_lines(const std::string& path);
Rotation parse_line(const std::string& line);
int mod(int a, int b);  // Positive modulo helper
double time_ms();

#endif  // FUNCTIONS_2025_H
