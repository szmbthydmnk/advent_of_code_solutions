


import Functions as F
import numpy as np
from scipy.optimize import milp, LinearConstraint  # SciPy >= 1.9 [web:60]

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Machine_lights_File.txt")
print(File[132])
machines_raw = File


def parse_machine(line: str):
    # indicator pattern
    ind_start = line.index('[') + 1
    ind_end = line.index(']')
    pattern = line[ind_start:ind_end]
    n = len(pattern)
    target = np.array([1 if c == '#' else 0 for c in pattern], dtype=int)

    # buttons: all (...) before '{'
    before_curly = line.split('{')[0]
    buttons = []
    tmp = before_curly
    while '(' in tmp:
        s = tmp.index('(')
        e = tmp.index(')', s)
        inside = tmp[s+1:e].strip()
        if inside:
            indices = [int(x) for x in inside.split(',')]
            buttons.append(indices)
        tmp = tmp[e+1:]

    m = len(buttons)
    A = np.zeros((n, m), dtype=int)
    for j, idxs in enumerate(buttons):
        for i in idxs:
            A[i, j] = 1

    return A, target


def min_presses_scipy(A: np.ndarray, b: np.ndarray):
    # A shape: (n_lights, n_buttons), b shape: (n_lights,)
    A = A.astype(float)
    b = b.astype(float)
    n_lights, n_buttons = A.shape

    num_x = n_buttons         # button press variables
    num_k = n_lights          # parity slack variables
    total = num_x + num_k

    # Objective: minimize sum_j x_j
    c = np.zeros(total)
    c[:num_x] = 1.0

    # Constraints: A x - 2 k = b
    A_con = np.zeros((n_lights, total))
    A_con[:, :num_x] = A
    A_con[:, num_x:] = -2 * np.eye(n_lights)

    constraints = LinearConstraint(A_con, b, b)

    # Bounds: all vars >= 0
    lb = np.zeros(total)
    ub = np.full(total, 5)

    # Integer variables
    integrality = np.ones(total, dtype=int)

    res = milp(c=c,
               constraints=constraints,
               integrality=integrality,
               bounds=(lb, ub))

    if not res.success:
        print("oh oh")
        return None, None

    x = np.rint(res.x[:num_x]).astype(int)
    return x, int(x.sum())


total_presses = 0
kkkk = 0
for line in machines_raw:
    kkkk += 1
    print("Machine", kkkk)
    print(line)

    A, target = parse_machine(line)
    x, presses = min_presses_scipy(A, target)
    
    print("button presses:", x, "total:", presses)
    total_presses += presses



print("Total presses across machines:", total_presses)

# part 2


import numpy as np
from scipy.optimize import milp, LinearConstraint  # SciPy >= 1.9 [web:60]

def parse_machine_jolts(line: str):
    # Extract joltage vector from {...}
    import re
    jolts_str = re.search(r"\{([^}]*)\}", line).group(1)
    b = np.array([int(x) for x in jolts_str.split(',')], dtype=float)

    # Buttons: same as before, but now rows correspond to counters
    before_curly = line.split('{')[0]
    buttons = []
    tmp = before_curly
    while '(' in tmp:
        s = tmp.index('(')
        e = tmp.index(')', s)
        inside = tmp[s+1:e].strip()
        if inside:
            indices = [int(x) for x in inside.split(',')]
            buttons.append(indices)
        tmp = tmp[e+1:]

    m = len(b)          # number of counters
    n = len(buttons)    # number of buttons
    A = np.zeros((m, n), dtype=float)
    for j, idxs in enumerate(buttons):
        for i in idxs:
            A[i, j] = 1.0

    return A, b

def min_presses_jolts_scipy(A: np.ndarray, b: np.ndarray):
    m, n = A.shape  # m counters, n buttons

    # Decision vars: x_j >= 0 integer
    num_x = n
    c = np.ones(num_x)  # minimize sum_j x_j

    # Equality constraints: A x = b
    constraints = LinearConstraint(A, b, b)

    # Bounds: x_j >= 0, no upper bound
    lb = np.zeros(num_x)
    ub = np.full(num_x, np.inf)

    # All integer
    integrality = np.ones(num_x, dtype=int)

    res = milp(c=c,
               constraints=constraints,
               integrality=integrality,
               bounds=(lb, ub))

    if not res.success:
        return None, None

    x = np.rint(res.x).astype(int)
    return x, int(x.sum())


total_presses_jolts = 0
kkkk = 0
for line in machines_raw:
    kkkk += 1
    print("Machine", kkkk)
    print(line)

    A, b = parse_machine_jolts(line)
    x, presses = min_presses_jolts_scipy(A, b)
    
    print("button presses:", x, "total:", presses)
    total_presses_jolts += presses

print("Total presses across machines (jolts):", total_presses_jolts)