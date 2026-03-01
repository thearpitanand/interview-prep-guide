# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A structured interview preparation guide covering 5 pillars: DSA, System Design, Engineering Core, Behavioral, and AI/ML. It contains ~245 Python coding problems and ~138 topics of markdown study material.

## Running DSA Problems

Each Python problem file is self-contained with inline tests. Run any problem directly:

```bash
python 01-dsa/01-arrays-and-bits/easy/01_reverse_array.py
```

No external dependencies, test frameworks, or build tools are needed. A passing file prints "All tests passed!".

## Repository Structure Conventions

- Directories are numbered (`01-`, `02-`, ...) to enforce study order
- Each section has a `00-README.md` with its navigation and overview
- `00-README.md` at root is the master guide (not `README.md`)

### DSA Problem File Format (`01-dsa/`)

Each `.py` file follows this structure:
1. **Docstring**: Problem name, LeetCode reference, day number, difficulty, examples, constraints, hint, and pattern
2. **Function stub**: With type hints and `pass` body (to be filled in by the student)
3. **Inline tests**: Under `if __name__ == "__main__":` using `assert` statements

Problems are organized by topic, then by difficulty (`easy/`, `medium/`, `hard/`). Each topic folder has a `concepts.md` with theory.

### Other Pillars

- `02-system-design/`: Markdown guides split into `fundamentals/`, `hld/` (high-level design), `lld/` (low-level design)
- `03-engineering-core/`: Markdown across `backend-internals/`, `codebase-design/`, `production-engineering/`, `debugging/`, `language-internals/`
- `04-behavioral/`: Markdown across `communication/`, `senior-mindset/`, `mock-interviews/`
- `05-ai-ml/`: Each subtopic has a `concepts.md`
