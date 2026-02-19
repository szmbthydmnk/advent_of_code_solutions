using BenchmarkTools

include("Day_01.jl")

# Absolute path
BASE_DIR = dirname(@__DIR__)
INPUT = joinpath(BASE_DIR, "input_files", "Password_File.txt")

println("=== AoC 2025 Day 01 Benchmark ===")
println("Input: $INPUT ($(length(readlines(INPUT))) lines)")

# Load data
lines = read_lines(INPUT)
rotations = parse_line.(lines)

println("\n1. Parse benchmark:")
@btime parse_line.($lines);  # Semicolon = no output

println("\n2. Part 1 benchmark:")
@btime part1($rotations);

println("\n3. Part 2 benchmark:") 
@btime part2($rotations);
