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

double benchmark(int N, auto&& func) {
    double total = 0;
    for (int i = 0; i < N; ++i) {
        auto start = std::chrono::high_resolution_clock::now();
        func();
        auto end = std::chrono::high_resolution_clock::now();
        total += std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() / 1000.0;
    }
    return total / N;
}

int main() {
    auto lines = read_lines("../input_files/Password_File.txt");
    std::vector<Rotation> rotations;
    for (const auto& line : lines) {
        rotations.push_back(parse_line(line));
    }
    
    const int N = 10000;  // 10k runs
    std::cout << "Benchmarking " << N << " runs (average):\n";
    
    double parse_avg = benchmark(N, [&]() {
        std::vector<Rotation> rotations;
        for (const auto& line : lines) rotations.push_back(parse_line(line));
    });
    
    double p1_avg = benchmark(N, [&]() { part1(rotations); });
    double p2_avg = benchmark(N, [&]() { part2(rotations); });
    
    std::cout << "Parse: " << parse_avg << " ms (x" << N << ")\n";
    std::cout << "Part 1: " << part1(rotations) << " (" << p1_avg << " ms)\n";
    std::cout << "Part 2: " << part2(rotations) << " (" << p2_avg << " ms)\n";
}

