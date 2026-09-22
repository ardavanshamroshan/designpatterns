---
title: Dependency Inversion
---

# Dependency Inversion Principle

<p class="lead">Depend on abstractions, not concretions.</p>

## Intent

High-level modules (policy) and low-level modules (details) both depend on abstractions. Details implement those abstractions.

## Problem

`Research` wants John’s children. If it walks `relationships.relations` tuples directly, it is glued to how storage is laid out. Change the list → break research.

## Solution

Introduce `RelationshipBrowser.find_all_children_of`.  
`Relationships` implements it. `Research` only talks to the browser.

<p class="flow-row" aria-hidden="true">
  <span>Research</span>
  <span class="arrow">→</span>
  <span>RelationshipBrowser</span>
  <span class="arrow">←</span>
  <span>Relationships</span>
</p>

## Structure

| Piece | Role |
| --- | --- |
| `Research` | High-level use case |
| `RelationshipBrowser` | Abstraction |
| `Relationships` | Low-level store |
| `Person` / `Relationship` | Domain bits |

## Compare code

<div class="compare-block">

<span class="compare-block__label compare-block__label--bad">Violation — dig into relations storage</span>

```python
class Research:
    def __init__(self, relationships: Relationships):
        for r in relationships.relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John has a child called {r[2].name}")
```

</div>

<div class="compare-block">

<span class="compare-block__label compare-block__label--good">Compliant — this repo</span>

```python
class Research:
    def __init__(self, browser: RelationshipBrowser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")
```

</div>

## Walkthrough

<StepsReveal
  :steps="[
    {
      title: 'Build a small family graph',
      body: 'John is parent of Chris and Matt. Relationships stores parent/child pairs.'
    },
    {
      title: 'Low-level implements the browser',
      body: 'find_all_children_of hides the tuple list. Callers never touch .relations.'
    },
    {
      title: 'High-level depends on the abstraction',
      body: 'Research(relationships) works because Relationships is a RelationshipBrowser.'
    }
  ]"
/>

## Quick check

<Quiz
  question="Which change follows DIP?"
  :options="[
    'Let Research index into relationships.relations for every new query.',
    'Have Research call RelationshipBrowser methods; keep storage private.',
    'Make RelationshipBrowser inherit from Research.'
  ]"
  :answer="1"
  ok="Yes — both sides depend on the abstraction; details stay behind it."
  no="Hint: high-level should not know the storage shape."
/>

## Run locally

```bash
uv run dip
```

Expected:

```text
John has a child called Chris
John has a child called Matt
```

Source: [main.py](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/dependency_inversion/main.py) · [tutorial README](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/dependency_inversion/README.md)

## Takeaway

- Policy must not scrape infrastructure internals  
- Share an abstraction both sides depend on  
- Details implement the abstraction — they don’t own the high-level  
