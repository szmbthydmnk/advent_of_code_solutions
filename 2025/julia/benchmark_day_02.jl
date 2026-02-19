using BenchmarkTools

include("Day_02.jl")

# Absolute path
BASE_DIR = dirname(@__DIR__)
INPUT = joinpath(BASE_DIR, "input_files", "ID_Ranges_File.txt")
isfile(INPUT) || error("File not found: $input_path")
println("=== AoC 2025 Day 02 Benchmark ===")

lines = readlines(INPUT)
raw_ranges = separate_ranges([lines[1]])
merged_ranges = simplify_ranges(raw_ranges)

println("\nPart 1 benchmark:")
@btime sum_invalid_ids(merged_ranges, is_id_repeated_twice)

println("\nPart 2 benchmark:")
@btime sum_invalid_ids(merged_ranges, is_id_repeated_n_times)

# oh boy, this is eating away the memory :(.