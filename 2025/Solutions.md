# AoC 2025 Benchmarks

## Day 1: Secret Entrance

| Solution Part 1 | Solution Part 2 | Part 1 (avg 10k runs, ms) | Part 2 (avg 10k runs, ms) |
|-----------------|-----------------|---------------------------|---------------------------|
| 1,154            | 6,819            | Py: **0.7961** - MacBook Air M4<br>C++: **0.011** - MacBook Air M4<br>Julia: **0.027791** - MacBook Air M4 | Py: **0.88553** - MacBook Air M4<br>C++: **0.03** - MacBook Air M4<br> Julia: **0.038917** - MacBook Air M4 |

**Py**: Ratio **P1/P2**: **0.899** (Air M4) | Notes: Python 3.14.2 | 
**C++**: Ratio **P1/P2**: **0.366** (Air M4) | Notes: - |
**julia**: Ratio **P1/P2**: **0.7313** (Air M4) | Notes: julia 1.12.3 |

|$L_1 / L_2$ | Python | C++ | julia |
|--|--|--|--|
|Python | 1 | 41.015 | 25.208 |
|C++ | 0.0243 | 1 | 0.6146 |
|julia | 0.0396 | 1.627 | 1 |

## Day 2: Secure Dial Lock

| Solution Part 1 | Solution Part 2 | Part 1 (10k, ms) | Part 2 (10k, ms) |
|-----------------|-----------------|--------------------|-------------------|
| 12,850,231,731  | 24,774,350,322  | Py: **298.5447** - MacBook Air M4 <br>C++: **74.031** - MacBook Air M4<br>julia: **81.393** - MacBook Air M4  | Py: **717.0450** - MacBook Air M4<br>C++: **814.164** - MacBook Air M4<br>julia: **188.353** - MacBook Air M4 |

**Py**: Ratio **P1/P2**: **0.4164** | Notes: Python 3.14.2  
**C++**: Ratio **P1/P2**: **0.0909** | Notes: clang++ -O2  
**Julia**: Ratio **P1/P2**: **0.4321** | Notes: Julia 1.12.3  

| L₁ / L₂    | Python | C++    | Julia  |
|------------|--------|--------|--------|
| **Python** | 1      | 1.143  | 3.765  |
| **C++**    | 0.874  | 1      | 3.293  |
| **Julia**  | 0.265  | 0.304  | 1      |

**note**: My brute force alarm didn't go off. So I bruteforced it. It definately seems from the timings.
