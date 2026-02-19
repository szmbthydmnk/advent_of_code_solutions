#include "Functions_2025.h"
#include <fstream>
#include <iostream>
#include <cstdlib>  // std::abs
#include <chrono>

std::vector<std::string> read_lines(const std::string& path) {
    std::ifstream file(path);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open " << path << "\n";
        return {};
    }
    
    std::string line;
    std::vector<std::string> lines;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    return lines;
}

Rotation parse_line(const std::string& line) {
    Rotation rotation;
    rotation.direction = line[0];
    rotation.rotation_value = std::stoi(line.substr(1));
    return rotation;
}

int mod(int a, int b) {
    return ((a % b) + b) % b;  // Python-style positive modulo
}


double time_ms() {
    return std::chrono::duration_cast<std::chrono::microseconds>(
        std::chrono::high_resolution_clock::now().time_since_epoch()
    ).count() / 1000.0;
}

