# Advent of Code 2025 - Day 01 - Secret Entrance
#     Julia solution

# Official website: https://adventofcode.com/2025/day/1
# Solution by Dominik Szombathy
# Date: 2025-12-01

include("Functions_2025.jl")
using .Functions_2025

"""
    part1(rotations::Vector{NamedTuple}) -> Int

Count dial position == 50 (mod 100).
# Arguments
- `password_lines::Vector{String}`:
- `dial_position::Int = 50`: 
"""
function part1(rotations::Vector{NamedTuple}, dial_position::Int=50)::Int
    count = 0
    current_dial = dial_position
    
    for r in rotations
        angle = r.dir == 'R' ? r.val : -r.val  # ✓ Use val!
        current_dial = mod(current_dial + angle, 100)
        current_dial == 0 && (count += 1)
    end
    return count
end


"""
    part2(password_lines::Vector{String}, starting_position::Int) -> Int

Solve Part 2: Count all passwords including those during multiple wraparounds.

# Algorithm
1. Track cumulative position without wrapping
2. Count how many complete cycles (0, 100, 200, ...) we pass through
3. Each crossing generates a password

# Arguments  
- `password_lines::Vector{String}`: Lines containing movement instructions
- `starting_position::Int`: Initial dial position (default: 50)

# Returns
- `Int`: Total number of passwords including wraparound cycles
"""
function part2(rotations::Vector{NamedTuple}, starting_position::Int=50)::Int
    dial = starting_position  # Use param
    count = 0
    for r in rotations
        angle = r.dir == 'R' ? r.val : -r.val
        dial += angle
        if dial < 0
            count += (dial % 100 == 0) ? abs(dial) ÷ 100 : abs(dial) ÷ 100 + 1
        elseif dial >= 100
            count += dial ÷ 100
        end
        dial = mod(dial, 100)
    end
    return count
end


# ============================================================================
# Main execution
# ============================================================================


filepath = "Advent_of_Code_2025/input_files/Password_File.txt"

lines = read_lines(filepath)
rotations = parse_line.(lines)

p1 = part1(rotations, 50)
p2 = part2(rotations, 50)

println("Part 1: $p1")  
println("Part 2: $p2")
