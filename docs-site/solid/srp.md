---
title: Single Responsibility
---

# Single Responsibility Principle

<p class="aka-line"><em>Also related: Separation of Concerns</em></p>

## Intent

A class should have **one primary reason to change**. Put different kinds of work in different places.

> **Responsibility** ≈ a reason the class would need to change — not “number of methods.”

## Problem

You start a simple `Journal`: add entries, remove them, print them. Then someone asks to save to disk. You add `save()` on the same class.

Now the class changes when entry rules change *and* when file format or I/O changes. Two reasons. Testing and reuse get harder.

## Solution

Keep `Journal` focused on entries. Move persistence to `PersistenceManager`.

<p class="flow-row" aria-hidden="true">
  <span>Journal · entries</span>
  <span class="arrow">→</span>
  <span>PersistenceManager · I/O</span>
  <span class="arrow">→</span>
  <span>journal.txt</span>
</p>

That second class is the **fix**, not the violation.

## Structure (analogy)

Structural patterns often need a translator between worlds. The Adapter intent image below (from Refactoring.Guru) shows the same *shape* of thinking: keep incompatible concerns apart with a thin middle layer.

![Adapter pattern intent illustration](/images/guru/adapter-intent.png)

<p class="figure-cite">
  Source:
  <a href="https://refactoring.guru/design-patterns/adapter" rel="noopener">refactoring.guru/design-patterns/adapter</a>
  · Illustration © Refactoring.Guru / Dmitry Zhart · used under their
  <a href="https://refactoring.guru/content-usage-policy" rel="noopener">content usage policy</a>
  (≤10 illustrations).
</p>

| Class | Responsibility | Methods |
| --- | --- | --- |
| `Journal` | Manage diary entries | `add_entry`, `remove_entry`, `__str__` |
| `PersistenceManager` | Write a journal to disk | `save_to_file` |

## Compare code

<details>
<summary><strong>Violation — persistence inside Journal</strong></summary>

```python
class Journal:
    def add_entry(self, text): ...
    def remove_entry(self, index): ...

    def save(self, filename):  # second responsibility
        with open(filename, "w") as f:
            f.write(str(self))
```

</details>

<details>
<summary><strong>Compliant — this repo</strong></summary>

```python
class Journal:
    def add_entry(self, text): ...
    def remove_entry(self, index): ...
    # no save / load here

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as f:
            f.write(str(journal))
```

</details>

## Walkthrough

<StepsReveal
  :steps="[
    {
      title: 'Create a journal and add entries',
      body: 'add_entry stores numbered lines. Printing joins them with newlines — pure domain logic.'
    },
    {
      title: 'Save via PersistenceManager',
      body: 'save_to_file only opens a file and writes str(journal). Swap storage later without touching Journal.'
    },
    {
      title: 'Confirm the file',
      body: 'The demo writes journal.txt next to main.py and prints its contents.'
    }
  ]"
/>

## Quick check

<Quiz
  question="In the compliant example, which statement is true?"
  :options="[
    'PersistenceManager violates SRP because it exists at all.',
    'Journal owns entries; PersistenceManager owns saving.',
    'SRP means every class may have only one method.'
  ]"
  :answer="1"
  ok="Yes — PersistenceManager isolates I/O so Journal keeps one reason to change."
  no="Hint: look at which class owns saving in the compliant example."
/>

## Run locally

```bash
uv run srp
```

Source: [main.py](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/single_responsibility/main.py) · [tutorial README](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/single_responsibility/README.md)

## Takeaway

- Domain object → business data and behavior
- Persistence helper → how that data is stored
- Mixing them couples your model to the filesystem

<style>
.aka-line { margin: -0.35rem 0 1rem; color: var(--text-faint); font-size: 0.95rem; }
details { margin: 0.65rem 0; padding: 0.5rem 0.75rem; border: 1px solid var(--line); }
details summary { cursor: pointer; }
</style>
