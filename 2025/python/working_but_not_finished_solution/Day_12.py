import Functions as F
import numpy as np
from collections import Counter

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Christmas_gift_packing.txt")
# ahhhh

File = open("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Christmas_gift_packing.txt", 'r')
File_parts = File.read().split('\n\n')
Presents = File_parts[:-1]
Presents
# print(Presents)

Regions = File_parts[-1].strip().splitlines()
# print(Regions[0])

region_sizes = []
region_box_count = []
for region in Regions:
    parts = region.split(':')
    size_part = parts[0].strip()
    box_count_part = parts[1].strip().split()

    region_sizes.append([int(number) for number in size_part.split('x')])
    region_box_count.append([int(number) for number in box_count_part])


# Format presents
Sizes = {}
for present in Presents:
    lines = present.splitlines()
    #print(lines)
    present_id = int(lines[0][:-1])
    #print(name)
    Shape = [list(row) for row in lines[1:]]
    #print(Shape)

    size = 0 
    for row in Shape:
        for col in row:
            if col == '#':
                size += 1
    Sizes[present_id] = size



def product(list):
    result = list[0]
    return result * product(list[1:]) if len(list) > 1 else result

def get_present_area(present_count, present_sizes):
    sum = 0 
    for i in range(len(present_sizes)):
        sum += Sizes[i] * present_count[i]
    return sum

def get_region_area(size_list):
    return size_list[0] * size_list[1]

multipliers = np.linspace(0, 1.6, num=int((1.6) / 0.0001) + 1)
Regions_can_fit_geschenk = [0] * len(multipliers)
Regions_with_problematic_cases = [0] * len(multipliers)
for m in range(len(multipliers)):
    for region_index in range(len(Regions)):
        region_area = get_region_area(region_sizes[region_index])
        present_area = get_present_area(region_box_count[region_index], Sizes)

        #print(f'{region_index=} {region_area=} {present_area=}')
        if region_area > present_area * multipliers[m]:
            Regions_can_fit_geschenk[m] += 1
        elif region_area < present_area:
            pass
        else:
            Regions_with_problematic_cases[m] += 1
            #print(f'Hard problem case {region_index=} {region_area=} {present_area=}')

print(Regions_can_fit_geschenk)

import matplotlib.pyplot as plt

plt.plot(multipliers, Regions_can_fit_geschenk, color='black')
plt.plot(multipliers, Regions_with_problematic_cases, color='red')
plt.xlabel('Multiplier')
plt.ylabel('Number of Regions that can fit Presents')
plt.title('Regions fitting Presents vs Multiplier')
plt.grid()

# Define the regions and their colors
regions = [(multipliers[0], 0.999, 'lightblue'), (1, 1.35, 'lightgreen'), (1.35, 1.6, 'lightcoral')]
for start, end, color in regions:
    plt.axvspan(start, end, color=color, alpha=0.5)

    # Annotate the two most common values of the function (true "most common", not largest)
    counter = Counter(Regions_can_fit_geschenk)
    most_common = counter.most_common(2)  # two most frequent values
    for value, freq in most_common:
        # find all indices where this value occurs and pick a central one for annotation
        indices = [i for i, v in enumerate(Regions_can_fit_geschenk) if v == value]
        idx = indices[len(indices) // 2]
        plt.annotate(f'Value: {value} (count: {freq})',
                     xy=(multipliers[idx], value),
                     xytext=(multipliers[idx], value + 5),
                     ha='center',
                     arrowprops=dict(facecolor='black', shrink=0.05))

    print(most_common)

plt.savefig('Day_12_Regions_vs_Multiplier.png')
