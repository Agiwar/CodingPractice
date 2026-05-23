# CodingPractice

Personal practice repo for coding interview prep — primarily **LeetCode DSA** (Python) and **SQL**.

## Structure

```
.
├── LeetCode/DSA/   # Primary focus — Python solutions by pattern
├── SQL/            # LeetCode SQL + interview problems (TikTok, Google, Spotify, Twitter)
├── HackerRank/     # Secondary practice — algorithms by category
├── KQL/            # Kusto Query Language notebooks
└── Python/         # Codewars, InterviewQuery, misc Python implementations
```

## LeetCode DSA

Solutions organized by algorithmic pattern:

- `array-hashing/` — two pointers, sliding window, hashmap counting
- `string/` — anagrams, palindromes, parsing
- `linked_list/` — fast/slow pointers, reversal
- `stack/` — monotonic stack, parentheses
- `tree/` — DFS/BFS, recursion patterns
- `graph/` — traversal, topological sort, shortest path
- `heap/` — top-K, priority queue
- `binary_search/` — search space reduction
- `sorting/`
- `backtracking/` — subsets, combinations, permutations
- `dynamic_programming/`

Each file is self-contained with the `Solution` class and a `test_*()` function with LeetCode examples plus edge cases. Run directly with `python3 path/to/problem.py`.

## SQL

LeetCode SQL problems (numbered files) and company interview questions (TikTok, Google, Spotify, Twitter, etc.). Topics covered:

- Window functions (`RANK`, `DENSE_RANK`, `LAG`/`LEAD`, running aggregates)
- Self-joins, anti-joins, correlated subqueries
- Date/time arithmetic, streaks, retention analysis
- Pivots, aggregation, percentile/median logic
- ETL data quality patterns

## Conventions

- Python: 3.x, type hints (`list[int]`, `dict[str, int]`), no `typing.List`
- File names: `snake_case` matching the problem slug
- Commit messages: the problem URL
