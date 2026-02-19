# Advent of Code 2025
# Szombathy Dominik
# 2025.12.09

# Day 7 - Laboratories

import Functions as F

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Tachion_spliter_File.txt")

Splitter_Map = File

print(File[0])

def FindTachionSource(Line):
    return [Line.find("S")]

print(FindTachionSource(File[0]))

def FindTachionSplitters(Line):
    return [pos for pos, char in enumerate(Line) if char == "^"]

print(FindTachionSplitters(File[5]))

print(len(File))
print(len(File[0]))

def FindAllSplitters(Splitter_Map):
    n = len(Splitter_Map)
    m = len(Splitter_Map[0])

    Splitter_Positions = [0] * n

    for lines in range(1, n):
        positions = FindTachionSplitters(Splitter_Map[lines])
        if not positions == []:
            Splitter_Positions[lines]= positions

    return Splitter_Positions

print(FindAllSplitters(Splitter_Map))

def BeamSplitter(Beam_Position, Splitter_Position):
    if not Splitter_Position:
        return []
    return [x for x in Beam_Position if x in Splitter_Position]

print(BeamSplitter([70, 72, 77], [71, 78]))
# Just for meself, the tachion trajectories:
Tachion_Trajectory_Map = Splitter_Map

# Tactics - Part 1:
# We know where the beam starts from (S), have a variable that tracks the positions of the splitted (/or not splitted) beams
# Then just check whether there is a splitter in that "lane" and if so, double the beam and place it below the line

Current_Beam_Position = FindTachionSource(Splitter_Map[0])

Number_of_Beam_Splits = 0

for Splitter_positions in FindAllSplitters(Splitter_Map):

    #Beam_Splitting_Positions = [BeamSplitter(Current_Beam_Position, Splitter_positions)]
    if not Splitter_positions:
        continue
    for p in Splitter_positions:
        if p not in Current_Beam_Position:
            continue
        Current_Beam_Position.remove(p)
        Number_of_Beam_Splits += 1
        if p - 1 not in Current_Beam_Position:
            Current_Beam_Position.append(p - 1)
        if p + 1 not in Current_Beam_Position:
            Current_Beam_Position.append(p + 1)
        

print("Current beam positions")
print(sorted(Current_Beam_Position))
print(Number_of_Beam_Splits)

print("-"*100)
# Part 2:
Current_Beam_Position = FindTachionSource(Splitter_Map[0])
Beam_Position_Counter = [0] * len(Splitter_Map)
Beam_Position_Counter[Current_Beam_Position[0]] = 1
print(Beam_Position_Counter)
print("-"*100)
for Splitter_positions in FindAllSplitters(Splitter_Map):

    #Beam_Splitting_Positions = [BeamSplitter(Current_Beam_Position, Splitter_positions)]
    if not Splitter_positions:
        continue
    for p in Splitter_positions:
        if p not in Current_Beam_Position:
            continue
        
        Beam_Position_Counter[p - 1] += Beam_Position_Counter[p]
        Beam_Position_Counter[p + 1] += Beam_Position_Counter[p]
        Beam_Position_Counter[p] = 0
        Current_Beam_Position.remove(p)
        if p - 1 not in Current_Beam_Position:
            Current_Beam_Position.append(p - 1)
        if p + 1 not in Current_Beam_Position:
            Current_Beam_Position.append(p + 1)
    print(Beam_Position_Counter)

print(sum(Beam_Position_Counter))