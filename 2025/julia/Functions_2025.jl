module Functions_2025

export read_lines, parse_line
"""
    read_lines(filepath::String) -> Vector{String}

Reads all lines from a file and returns them as a vector of strings.
"""

function read_lines(filepath::String)::Vector{String}
    if !isfile(filepath)
        error("File not found: $filepath")
    end

    return readlines(filepath)
end

"""
    parse_line(line::String) -> NamedTuple{(:dir, :val), Tuple{Char, Int}}

Parse rotation: "R45" → (dir='R', val=45)
"""
function parse_line(line::String)
    dir = line[1]
    angle = parse(Int, line[2:end])
    (dir, angle)
end


end

