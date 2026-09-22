---
title: Single Responsibility
---

# Single Responsibility Principle

<p class="lead">Also related: Separation of Concerns</p>

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

## Structure

| Class | Responsibility | Methods |
| --- | --- | --- |
| `Journal` | Manage diary entries | `add_entry`, `remove_entry`, `__str__` |
| `PersistenceManager` | Write a journal to disk | `save_to_file` |

## Compare code

<div class="compare-block">

<span class="compare-block__label compare-block__label--bad">Violation — persistence inside Journal</span>

```python
class Journal:
    def add_entry(self, text): ...
    def remove_entry(self, index): ...

    def save(self, filename):  # second responsibility
        with open(filename, "w") as f:
            f.write(str(self))
```

</div>

<div class="compare-block">

<span class="compare-block__label compare-block__label--good">Compliant — this repo</span>

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

</div>

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
