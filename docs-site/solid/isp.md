---
title: Interface Segregation
---

# Interface Segregation Principle

<p class="lead">Don’t force clients to depend on methods they don’t use.</p>

## Intent

Prefer **many small interfaces** over one fat interface. A print-only device should only know about printing.

## Problem

`Machine` demands `print`, `fax`, and `scan`. An old printer can only print. It still must stub fax and raise on scan — a lie forced by the base type.

## Solution

Split into `Printer`, `Scanner`, and `Fax`. Implement only what you need. A multi-function device **composes** the small roles.

<p class="flow-row" aria-hidden="true">
  <span>Printer</span>
  <span class="arrow">+</span>
  <span>Scanner</span>
  <span class="arrow">+</span>
  <span>Fax</span>
  <span class="arrow">→</span>
  <span>MultiFunctionDevice</span>
</p>

## Structure

| Piece | Role |
| --- | --- |
| `Machine` / `OldFashionedPrinter` | Fat interface (violation) |
| `Printer` / `Scanner` / `Fax` | Segregated interfaces |
| `*Impl` classes | Focused implementations |
| `MultiFunctionDeviceImpl` | Delegates to `_printer`, `_scanner`, `_fax` |

## Compare code

<div class="compare-block">

<span class="compare-block__label compare-block__label--bad">Violation — fat Machine</span>

```python
class OldFashionedPrinter(Machine):
    def print(self, document): ...
    def fax(self, document): pass  # forced
    def scan(self, document):
        raise NotImplementedError  # forced
```

</div>

<div class="compare-block">

<span class="compare-block__label compare-block__label--good">Compliant — small interfaces + compose</span>

```python
class PrinterImpl(Printer):
    def print(self, document):
        print(document)

class MultiFunctionDeviceImpl(MultiFunctionDevice):
    def __init__(self, printer, scanner, fax):
        self._printer = printer
        self._scanner = scanner
        self._fax = fax

    def fax(self, document):
        self._fax.fax(document)
```

</div>

## Walkthrough

<StepsReveal
  :steps="[
    {
      title: 'Fat interface hurts simple devices',
      body: 'OldFashionedPrinter inherits Machine and must deal with fax/scan even though it cannot do them.'
    },
    {
      title: 'Segregate by role',
      body: 'Printer, Scanner, and Fax each declare one concern. Implementations only take what they need.'
    },
    {
      title: 'Compose the multi-function device',
      body: 'MultiFunctionDeviceImpl delegates to injected collaborators. Underscored fields avoid shadowing the methods.'
    }
  ]"
/>

## Quick check

<Quiz
  question="Which design follows ISP?"
  :options="[
    'One Machine base with print, fax, and scan for every device.',
    'Separate Printer / Scanner / Fax interfaces; compose when needed.',
    'Make OldFashionedPrinter raise NotImplementedError for unused methods and stop there.'
  ]"
  :answer="1"
  ok="Yes — small interfaces, compose for richer devices."
  no="Hint: ISP is about not forcing unused methods on clients."
/>

## Run locally

```bash
uv run isp
```

Expected:

```text
Hello, world!
Scanning Hello, world!
Faxing Hello, world!
```

Source: [main.py](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/interface_segregation/main.py) · [tutorial README](https://github.com/ardavanshamroshan/designpatterns/blob/main/solid/interface_segregation/README.md)

## Takeaway

- Fat interfaces force stub methods and lies  
- Split by client need  
- Compose multi-capability types from small roles  
