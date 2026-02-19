/*
Advent of Code 2025 - Day 02 - Gift Shop
Official website: https://adventofcode.com/2025/day/2
Solution by Dominik Szombathy
Date: 2025-12-02
*/

#include <algorithm>     // std::ranges::sort, std::max
#include <cstdint>
#include <fstream>
#include <iostream>
#include <ranges>
#include <string>
#include <string_view>
#include <vector>

using Range = std::vector<int64_t>;  // [start, end] 
using Ranges = std::vector<Range>;

Ranges separate_ranges(std::istream& input) {
    Ranges ranges;

    std::string line;
    while (std::getline(input, line)) {
        std::string_view sv{line};

        // Split by commas
        while (!sv.empty()) {
            std::size_t comma_pos = sv.find(',');
            std::string_view pair = sv.substr(0, comma_pos);

            // Remove processed pair
            if (comma_pos == std::string_view::npos) {
                sv = {};  // Clear sv
            } else {
                sv.remove_prefix(comma_pos + 1);
            }

            // Split pair by '-'
            std::size_t dash = pair.find('-');
            if (dash == std::string_view::npos) continue;

            int64_t start = std::stoll(std::string{pair.substr(0, dash)});
            int64_t end = std::stoll(std::string{pair.substr(dash + 1)});
            ranges.emplace_back(Range{start, end});
        }
    }
    return ranges;
}


Ranges simplify_ranges(Ranges ranges) {
    if (ranges.empty()) return {};

    // Sort by start
    std::sort(ranges.begin(), ranges.end(), [](const Range& a, const Range& b) {
        return a[0] < b[0];
    });

    Ranges merged;
    merged.reserve(ranges.size());

    Range current = ranges[0];  // FIXED: Take first range
    for (std::size_t i = 1; i < ranges.size(); ++i) {
        const Range& next_range = ranges[i];  // FIXED: Define 'next'

        if (current[1] >= next_range[0]) {    // FIXED: Use next_range
            current[1] = std::max(current[1], next_range[1]);
        } else {
            merged.push_back(std::move(current));
            current = next_range;             // FIXED: Update current
        }
    }
    merged.push_back(std::move(current));     // Last range

    return merged;
}


bool is_id_repeated_twice(int64_t id){
    std::string id_str = std::to_string(id);

    if (id_str.empty() || id_str[0] == '0' || id_str.size() % 2 != 0) return false;

    size_t half_size = id_str.size() / 2;
    return id_str.substr(0, half_size) == id_str.substr(half_size);
}

bool is_id_repeated_Nth(int64_t id) {
    std::string id_str = std::to_string(id);

    if (id_str.empty() || id_str[0] == '0') return false;

    size_t id_len = id_str.size();

    for (size_t pattern_length = 1; pattern_length <= id_len / 2; ++pattern_length) {
        if (id_len % pattern_length != 0) continue;

        size_t repeats = id_len / pattern_length;

        if (repeats < 2) continue;

        std::string_view pattern = std::string_view{id_str}.substr(0, pattern_length);

        bool matches = true;
        for (size_t k = 1; k < repeats; k++) {
            if (std::string_view{id_str}.substr(k * pattern_length, pattern_length) != pattern) {
                matches = false;
            }
        }
        if (matches) return true;
    }
    return false;
}

int64_t sum_invalid_ids(const Ranges& ranges, bool (*is_invalid)(int64_t)) noexcept {
    int64_t total = 0;
    
    for (const auto& r : ranges) {
        for (int64_t id = r[0]; id <= r[1]; ++id) {
            if (is_invalid(id)) {
                total += id;
            }
        }
    }
    return total;
}


int main() {
    std::ifstream file("../input_files/ID_Ranges_File.txt");
    if (!file) {
        std::cerr << "File not found!\n";
        return 1;
    }

    auto raw = separate_ranges(file);
    auto merged = simplify_ranges(raw);
    
    std::cout << "Raw: " << raw.size() << ", Merged: " << merged.size() << "\n";

    // Part 1
    auto sum1 = sum_invalid_ids(merged, is_id_repeated_twice);
    std::cout << "Part 1 (twice): " << sum1 << "\n";

    // Part 2  
    auto sum2 = sum_invalid_ids(merged, is_id_repeated_Nth);
    std::cout << "Part 2 (N times): " << sum2 << "\n";

    return 0;
}

