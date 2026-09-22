---
title: Open / Closed
---

# Open/Closed Principle

<p class="lead">Open for extension, closed for modification.</p>

## Intent

Add new behavior **without editing** existing, working classes. Prefer new types over endless patches to one filter.

## Problem

`ProductFilter` starts simple: `filter_by_color`, then `filter_by_size`, then `filter_by_size_and_color`. Every new criterion or combination means opening that class again. Combinations explode.

## Solution

Introduce a **Specification**: an object that answers “does this item match?”  
`BetterFilter` only knows how to apply a spec. New rules are new classes.

<p class="flow-row" aria-hidden="true">
  <span>Products</span>
  <span class="arrow">→</span>
  <span>BetterFilter + Spec</span>
  <span class="arrow">→</span>
  <span>Matches</span>
</p>

## Structure

| Piece | Role |
| --- | --- |
| `Product` | Name, color, size |
| `ProductFilter` | Old approach (violation) |
| `Specification` | Match rule (`is_satisfied`) |
| `ColorSpecification` / `SizeSpecification` | Concrete rules |
| `AndSpecification` | Combine rules |
| `BetterFilter` | Apply any spec |

## Compare code

<div class="compare-block">

<span class="compare-block__label compare-block__label--bad">Violation — methods grow on ProductFilter</span>

```python
class ProductFilter:
    def filter_by_color(self, products, color): ...
    def filter_by_size(self, products, size): ...
    def filter_by_size_and_color(self, products, size, color): ...
    # next: weight, size+weight, color+weight, ...
```

</div>

<div class="compare-block">

<span class="compare-block__label compare-block__label--good">Compliant — this repo</span>

```python
class ColorSpecification(Specification):
    def is_satisfied(self, item):
        return item.color == self.color

class BetterFilter(Filter):
    def filter(self, items, spec):
        return [item for item in items if spec.is_satisfied(item)]

# compose without touching BetterFilter
large_blue = AndSpecification(
    SizeSpecification(Size.LARGE),
    ColorSpecification(Color.BLUE),
)
```

</div>

## Walkthrough

<StepsReveal
  :steps="[
    {
      title: 'Build a small catalog',
      body: 'Apple (green/small), Tree (green/large), House (blue/large). Same list for both filters.'
    },
    {
      title: 'Old filter still works — but is rigid',
      body: 'ProductFilter.filter_by_color finds green items. Adding a new rule would mean editing ProductFilter.'
    },
    {
      title: 'Specs + BetterFilter',
      body: 'ColorSpecification and SizeSpecification plug into BetterFilter. AndSpecification combines them for large + blue.'
    }
  ]"
/>

## Quick check

<Quiz
  question="Which change follows OCP for a new “filter by price” need?"
  :options="[
    'Add filter_by_price (and every combination) to ProductFilter.',
    'Add a PriceSpecification and keep BetterFilter unchanged.',
    'Copy BetterFilter into BetterFilter2 and hard-code price.'
  ]"
  :answer="1"
  ok="Yes — extend with a new Specification; leave the filter engine closed."
  no="Hint: OCP favors new classes over editing the old filter."
/>

## Run locally

```bash
uv run ocp
```

Source: [main.py](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/open_closed/main.py) · [tutorial README](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/open_closed/README.md)

## Takeaway

- Don’t grow one filter with every criterion  
- Encode criteria as composable objects  
- Extend by adding classes; keep the engine closed  
