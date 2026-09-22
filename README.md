# Design Patterns & SOLID

Hands-on Python tutorials for classic **design patterns** and the **SOLID** principles.

## Docs

**https://ardavanshamroshan.github.io/designpatterns/**

```bash
cd docs-site
npm install
npm run docs:dev
```

## Requirements

- Python **≥ 3.14**
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync
uv run srp
uv run ocp
uv run lsp
uv run isp
```

## SOLID

| Principle | Folder | Status | Run |
|-----------|--------|--------|-----|
| **S** — Single Responsibility | [`solid/single_responsibility/`](solid/single_responsibility/) | Ready | `uv run srp` |
| **O** — Open/Closed | [`solid/open_closed/`](solid/open_closed/) | Ready | `uv run ocp` |
| **L** — Liskov Substitution | [`solid/liskov/`](solid/liskov/) | Ready | `uv run lsp` |
| **I** — Interface Segregation | [`solid/interface_segregation/`](solid/interface_segregation/) | Ready | `uv run isp` |
| **D** — Dependency Inversion | — | Planned | — |
