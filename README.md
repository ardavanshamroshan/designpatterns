# Design Patterns & SOLID

Hands-on Python tutorials for classic **design patterns** and the **SOLID** principles.

Small, runnable examples — one idea per folder. Read the local README, run the script, see the point.

## Requirements

- Python **≥ 3.14**
- [uv](https://docs.astral.sh/uv/) (recommended)

```bash
uv sync
```

## SOLID

| Principle | Folder | Status | Run |
|-----------|--------|--------|-----|
| **S** — Single Responsibility | [`solid/single_responsibility/`](solid/single_responsibility/) | Ready | `uv run srp` |
| **O** — Open/Closed | — | Planned | — |
| **L** — Liskov Substitution | — | Planned | — |
| **I** — Interface Segregation | — | Planned | — |
| **D** — Dependency Inversion | — | Planned | — |

### Single Responsibility (SRP)

A class should have **one primary reason to change**.

- Tutorial: [`solid/single_responsibility/README.md`](solid/single_responsibility/README.md)
- Code: [`solid/single_responsibility/main.py`](solid/single_responsibility/main.py)

```bash
uv run srp
```

`Journal` manages entries. `PersistenceManager` saves to `journal.txt`. Two concerns, two classes.

## Project layout

```text
designpatterns/
├── solid/
│   └── single_responsibility/
│       ├── README.md      # tutorial
│       ├── main.py        # example
│       └── journal.txt    # sample output from a run
├── main.py
├── pyproject.toml
└── README.md              # this file
```

## Docs site

Interactive GitHub Pages docs (dark / light, quizzes, code compare):

**https://ardavanshamroshan.github.io/designpatterns/**

Source lives in [`docs/`](docs/). Local preview:

```bash
cd docs && python -m http.server 8080
```

Then open `http://127.0.0.1:8080`.

## License

Educational use. Add a license file when you publish for others.
