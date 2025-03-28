# DSA

This is a collection of exercises and notes collected by studying DSA.
The repo is setup using the following structure:
```
dsa-multi-language/
├── .gitignore              # Standard gitignore for multiple languages
├── README.md               # Main repo description, structure overview
│
├── concepts/                 # Language-agnostic theory & notes (optional)
│   ├── big_o.md
│   ├── recursion.md
│   └── data_structures_overview.md
│
├── data_structures/          # Core DS implementations (optional, good practice)
│   ├── linked_list/
│   │   ├── notes.md          # Concept notes for Linked Lists
│   │   ├── python/
│   │   │   └── linked_list.py
│   │   └── cpp/              # Example for C++ later
│   │       ├── include/
│   │       │   └── linked_list.h
│   │       └── src/
│   │           └── linked_list.cpp
│   ├── tree/
│   │   ├── notes.md
│   │   ├── python/
│   │   │   └── bst.py
│   │   └── ...
│   └── ...
│
├── algorithms/               # Core Algorithm implementations (optional)
│   ├── sorting/
│   │   ├── notes.md
│   │   ├── python/
│   │   │   └── merge_sort.py
│   │   └── cpp/
│   │       └── merge_sort.cpp
│   ├── searching/
│   │   ├── notes.md
│   │   ├── python/
│   │   │   └── binary_search.py
│   │   └── ...
│   └── ...
│
└── practice_problems/        # <<< CORE AREA FOR LEETCODE STYLE PROBLEMS
    ├── leetcode/
    │   ├── 001_two_sum/      # <<< Directory per problem
    │   │   ├── README.md     # Problem description, examples, constraints, notes
    │   │   ├── python/       # <<< Sub-directory per language
    │   │   │   └── solution.py # Contains Solution class + test block
    │   │   ├── cpp/          # Example for C++ later
    │   │   │   └── solution.cpp
    │   │   └── java/         # Example for Java later
    │   │       └── Solution.java
    │   │
    │   ├── 002_add_two_numbers/
    │   │   ├── README.md
    │   │   ├── python/
    │   │   │   └── solution.py
    │   │   └── ... # Add other language folders as needed
    │   │
    │   └── ... (other LeetCode problems)
    │
    └── hackerrank/           # If you use other platforms
        └── some_problem/
            ├── README.md
            ├── python/
            │   └── solution.py
            └── ...

```
