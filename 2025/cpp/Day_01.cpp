/*
Advent of Code 2025 - Day 01 - Secret Entrance
Official website: https://adventofcode.com/2025/day/1
Solution by Dominik Szombathy
Date: 2025-12-01
*/

#include "Functions_2025.h"
#include <iostream>


int part1(const std::vector<Rotation>& rotations){

    int dial_position = 50;
    int count = 0;

    for (const auto& r: rotations){
        int rotation_angle = (r.direction == 'R') ? r.rotation_value : -r.rotation_value;
        // trenary operator: condition ? true_value: false_value
        dial_position = (dial_position + rotation_angle ) % 100;
        if (dial_position == 0){
            count++;
        }
    }
    return count;
}


int part2(const std::vector<Rotation>& rotations) {
    int dial_position = 50;
    int count = 0;
    
    for (const auto& r : rotations) {
        int rotation_angle = (r.direction == 'R') ? r.rotation_value : -r.rotation_value;
        dial_position += rotation_angle;
        
        if (dial_position < 0) {
            if (dial_position % 100 == 0) {
                count += std::abs(dial_position) / 100;
            } else {
                count += std::abs(dial_position) / 100 + 1;
            }
        } else if (dial_position >= 100) {
            count += dial_position / 100;
        }
        dial_position = mod(dial_position, 100);
    }
    return count;
}


int main() {
    // Read input
    std::string input_path = "../input_files/Password_File.txt";
    std::vector<std::string> lines = read_lines(input_path);
    std::cout << "Total lines read: " << lines.size() << "\n";
    
    // Parse rotations
    std::vector<Rotation> rotations;
    for (const auto& line : lines) {
        rotations.push_back(parse_line(line));
    }
    
    // Solve
    int ans1 = part1(rotations);
    int ans2 = part2(rotations);

    std::cout << "Part 1: " << ans1 << "\n";
    std::cout << "Part 2: " << ans2 << "\n";

    return 0;
}
