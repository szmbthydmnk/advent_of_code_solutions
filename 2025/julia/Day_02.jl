# Advent of Code 2025 - Day 02 - Gift Shop
# Official website: https://adventofcode.com/2025/day/2
# Solution by Dominik Szombathy
# Date: 2025-12-02

"""
    separate_ranges(lines::AbstractVector{String})::Vector{Vector{Int64}}
"""
function separate_ranges(lines::AbstractVector{String})::Vector{Vector{Int64}}
    ranges = Vector{Vector{Int64}}()
    
    for line in lines
        line = strip(line)
        line == "" && continue
        
        range_pairs = split(line, ',')
        for pair_str in range_pairs
            pair_str = strip(pair_str)
            pair_str == "" && continue
            
            parts = split(pair_str, '-', limit=2)
            length(parts) != 2 && continue
            
            try
                start = parse(Int64, parts[1])
                finish = parse(Int64, parts[2])
                push!(ranges, [start, finish])
            catch e
                @warn "Invalid range '$pair_str': $e"
            end
        end
    end
    return ranges
end

"""
    simplify_ranges(ranges::Vector{Vector{Int64}})::Vector{Vector{Int64}}
"""
function simplify_ranges(ranges::Vector{Vector{Int64}})::Vector{Vector{Int64}}
    isempty(ranges) && return Vector{Vector{Int64}}()
    
    sort!(ranges, by = r -> r[1])
    
    merged = Vector{Vector{Int64}}()
    sizehint!(merged, length(ranges))  # Pre-allocate
    
    current = ranges[1]
    for i in 2:length(ranges)
        next_range = ranges[i]
        if current[2] >= next_range[1]
            current[2] = max(current[2], next_range[2])
        else
            push!(merged, current)
            current = next_range
        end
    end
    push!(merged, current)
    
    return merged
end

"""
    report_large_ranges(ranges::Vector{Vector{Int64}}; threshold::Int64 = 1_000_000)
"""
function report_large_ranges(ranges::Vector{Vector{Int64}}; threshold::Int64 = 1_000_000)
    for range in ranges
        size_ = range[2] - range[1] + 1
        if size_ >= threshold
            println("Large range: $(range[1])-$(range[2]) (size: $size_)")
        end
    end
end

"""
    is_id_repeated_twice(id::Int64)::Bool
"""
function is_id_repeated_twice(id::Int64)::Bool
    id_str = string(id)
    id_str[1] == '0' && return false
    n = length(id_str)
    isodd(n) && return false
    
    half = n ÷ 2
    return id_str[1:half] == id_str[half+1:end]
end

"""
    is_id_repeated_n_times(id::Int64)::Bool
"""
function is_id_repeated_n_times(id::Int64)::Bool
    id_str = string(id)
    id_str[1] == '0' && return false
    
    n = length(id_str)
    for pattern_len in 1:(n ÷ 2)
        n % pattern_len != 0 && continue
        repeats = n ÷ pattern_len
        repeats < 2 && continue
        
        pattern = id_str[1:pattern_len]
        all(id_str[(k-1)*pattern_len+1 : k*pattern_len] == pattern for k in 2:repeats) && return true
    end
    return false
end

"""
    sum_invalid_ids(ranges, is_invalid)
"""
function sum_invalid_ids(ranges::Vector{Vector{Int64}}, is_invalid::Function)::Int64
    total::Int64 = 0
    @inbounds @simd for range in ranges
        @inbounds @simd for id in range[1]:range[2]
            is_invalid(id) && (total += id)
        end
    end
    return total
end

function main()::Nothing
    input_path = joinpath("Advent_of_Code_2025", "input_files", "ID_Ranges_File.txt")
    isfile(input_path) || error("File not found: $input_path")
    
    lines = readlines(input_path)
    raw_ranges = separate_ranges([lines[1]])
    merged_ranges = simplify_ranges(raw_ranges)
    
    println("Raw: $(length(raw_ranges)), Merged: $(length(merged_ranges))")
    report_large_ranges(merged_ranges)
    
    sum1 = sum_invalid_ids(merged_ranges, is_id_repeated_twice)
    println("Part 1 (repeated twice): $sum1")
    
    sum2 = sum_invalid_ids(merged_ranges, is_id_repeated_n_times)
    println("Part 2 (N repeats): $sum2")
end

main()


