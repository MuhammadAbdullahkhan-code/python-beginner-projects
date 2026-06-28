# Python Fundamentals

A structured collection of Python scripts covering core language fundamentals,
through to object-oriented programming and small practice projects.

## Structure

```
python-fundamentals/
│── README.md
│
├── 01_variables/         -> variable assignment, types, type casting
├── 02_input_output/      -> input(), print(), formatting
├── 03_conditions/        -> if / elif / else, match-case
├── 04_loops/             -> for, while, break, continue
├── 05_functions/         -> params, *args/**kwargs, lambdas, recursion
├── 06_lists/             -> creation, slicing, methods, comprehensions
├── 07_tuples/            -> immutability, unpacking, nested tuples
├── 08_dictionaries/      -> key-value pairs, comprehensions, merging
├── 09_sets/              -> uniqueness, set operations, frozensets
├── 10_file_handling/     -> reading/writing text & JSON files
├── 11_oop/
│   ├── class.py          -> classes, objects, properties, encapsulation
│   ├── inheritance.py    -> single/multi-level/multiple inheritance
│   └── polymorphism.py   -> method overriding, duck typing, ABCs
│
└── mini_projects/
    ├── calculator.py            -> CLI calculator (+ - * /)
    ├── number_guessing.py       -> number guessing game
    ├── password_generator.py    -> random secure password generator
    ├── todo_list.py              -> JSON-persisted to-do list manager
    └── student_management.py    -> OOP-based student record system
```

## How to run

Each file is self-contained and runnable on its own:

```bash
python 01_variables/variables.py
python mini_projects/calculator.py
```

Requires Python 3.10+ (for `match-case` support in `03_conditions/if_else.py`).
Everything else works on Python 3.6+.

## Notes

- Files with interactive `input()` calls have their interactive sections
  commented out by default and include a non-interactive `demo()` function
  so they can be run and inspected without manual input. Uncomment the
  marked lines to try them interactively.
- `10_file_handling/file.py` and `mini_projects/todo_list.py` will create
  small data files (`sample.txt`, `data.json`, `tasks.json`) alongside
  themselves when run.
