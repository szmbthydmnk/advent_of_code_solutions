import Functions as F
from collections import Counter

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Device_connections_File.txt")

def parse_graph_lines(lines: list[str]) -> dict[str, list[str]]:
    graph = {}
    for line in lines:
        line = line.strip()
        if not line or ':' not in line:
            continue
        device, outputs_str = line.split(':', 1)
        device = device.strip()
        outputs = [out.strip() for out in outputs_str.split() if out.strip()]
        graph[device] = outputs
    graph.setdefault('out', [])
    return graph

def find_all_paths_with_progress(graph: dict[str, list[str]], start: str, end: str, name: str = "") -> list[list[str]]:
    """Find all paths with progress printing."""
    def dfs(current: str, path: list[str], visited: set[str], all_paths: list[list[str]]):
        path.append(current)
        visited.add(current)
        
        if current == end:
            all_paths.append(path[:])
            #print(f"  ✅ Found path {len(all_paths)}: {' → '.join(path[-5:])}")  # Last 5 nodes
        else:
            #print(f"  📍 Exploring {current} (depth {len(path)}, paths so far: {len(all_paths)})")
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    dfs(neighbor, path, visited, all_paths)
        
        path.pop()
        visited.remove(current)
    
    #print(f"\n🚀 Starting {name}: {start} → {end}")
    all_paths = []
    dfs(start, [], set(), all_paths)
    print(f"✅ {name} COMPLETE: {len(all_paths)} paths found")
    return all_paths

def count_part2_multiplication_with_progress(graph: dict[str, list[str]]) -> int:
    """Part 2 with detailed progress."""
    print("\n🔢 PART 2: Computing sub-path counts...")
    
    # Order 1: svr → dac → fft → out
    print("\n📊 Order 1: svr → dac → fft → out")
    svr_dac = find_all_paths_with_progress(graph, "svr", "dac", "svr→dac")
    print(f"   📈 Paths svr→dac: {len(svr_dac)}")
    dac_fft = find_all_paths_with_progress(graph, "dac", "fft", "dac→fft")
    print(f"   📈 Paths dac→fft: {len(dac_fft)}")
    fft_out = find_all_paths_with_progress(graph, "fft", "out", "fft→out")
    print(f"   📈 Paths fft→out: {len(fft_out)}")
    order1 = len(svr_dac) * len(dac_fft) * len(fft_out)
    print(f"   📈 Order 1 total: {order1}")
    
    # Order 2: svr → fft → dac → out
    print("\n📊 Order 2: svr → fft → dac → out")
    svr_fft = find_all_paths_with_progress(graph, "svr", "fft", "svr→fft")
    print(f"   📈 Paths svr→fft: {len(svr_fft)}")
    fft_dac = find_all_paths_with_progress(graph, "fft", "dac", "fft→dac")
    print(f"   📈 Paths fft→dac: {len(fft_dac)}")
    dac_out = find_all_paths_with_progress(graph, "dac", "out", "dac→out")
    print(f"   📈 Paths dac→out: {len(dac_out)}")
    order2 = len(svr_fft) * len(fft_dac) * len(dac_out)
    print(f"   📈 Order 2 total: {order2}")
    
    total = order1 + order2
    print(f"\n🎯 FINAL PART 2: {total}")
    return total

# MAIN EXECUTION WITH PROGRESS
print("📂 Parsing graph...")
graph = parse_graph_lines(File)
print(f"✅ Graph parsed: {len(graph)} nodes")

print("\n⭐ PART 1:")
part1_paths = find_all_paths_with_progress(graph, "you", "out", "you→out")
part1 = len(part1_paths)
print(f"🎉 Part 1: {part1}")

print("\n🔥 PART 2:")
part2 = count_part2_multiplication_with_progress(graph)
print(f"🎉 Part 2: {part2}")
