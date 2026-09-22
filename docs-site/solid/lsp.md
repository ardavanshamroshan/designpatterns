---
title: Liskov Substitution
---

# Liskov Substitution Principle

<p class="lead">Subtypes must be usable wherever their base type is expected.</p>

## Intent

If a function accepts a `Rectangle`, passing a `Square` (when `Square` is-a `Rectangle`) must not break the function’s assumptions.

## Problem

It feels natural: a square *is a* rectangle. So `Square` subclasses `Rectangle` and overrides setters so sides stay equal.

But callers of `Rectangle` assume setting `height` only changes height. `Square` also rewrites `width`. The contract breaks.

## Violation (this example)

`use_it` saves width, sets `height = 10`, expects `area == width * 10`.

<p class="flow-row" aria-hidden="true">
  <span>use_it(Rectangle)</span>
  <span class="arrow">→</span>
  <span>OK</span>
</p>
<p class="flow-row" aria-hidden="true">
  <span>use_it(Square)</span>
  <span class="arrow">→</span>
  <span>Wrong area</span>
</p>

## Structure

| Piece | Role |
| --- | --- |
| `Rectangle` | Independent width / height |
| `Square` | Setters keep sides equal (breaks parent contract) |
| `use_it` | Client that trusts Rectangle behavior |

## Compare code

<div class="compare-block">

<span class="compare-block__label compare-block__label--bad">Subtype changes the meaning of setters</span>

```python
class Square(Rectangle):
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value
```

</div>

<div class="compare-block">

<span class="compare-block__label compare-block__label--good">Client assumes Rectangle rules</span>

```python
def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected: {expected}, Actual: {rc.area}")
```

</div>

## Walkthrough

<StepsReveal
  :steps="[
    {
      title: 'Rectangle behaves as promised',
      body: 'Rectangle(2, 3): set height to 10 → area 20. Expected matches actual.'
    },
    {
      title: 'Square looks like a Rectangle',
      body: 'Square(5) is passed to the same use_it. Type-wise it is a Rectangle subclass.'
    },
    {
      title: 'Numbers diverge',
      body: 'Setting height also sets width. Expected 50, actual 100 — LSP violation in action.'
    }
  ]"
/>

## Quick check

<Quiz
  question="Why does Square break LSP here?"
  :options="[
    'Because Square has fewer methods than Rectangle.',
    'Because it changes setter behavior so Rectangle clients get wrong results.',
    'Because LSP forbids inheritance completely.'
  ]"
  :answer="1"
  ok="Yes — substitution fails when the subtype weakens or alters the parent contract."
  no="Hint: look at what use_it assumes about height."
/>

## Run locally

```bash
uv run lsp
```

Expected shape:

```text
Expected: 20, Actual: 20
Expected: 50, Actual: 100
```

Source: [main.py](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/liskov/main.py) · [tutorial README](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/liskov/README.md)

## Takeaway

- Inheritance is a behavioral promise, not just reuse  
- If the subtype can’t honor the parent contract, don’t inherit that way  
- Prefer a shared `Shape` (or similar) over forcing Square into Rectangle  

## Better direction

Don’t model a mutable square as a rectangle subtype — keep them as siblings under a common abstraction, or drop independent setters on a shared base.
