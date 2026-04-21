# Memory directories (HEFHS structure)

## Purpose

This directory stores agent memory according to HEFHS standard:

- `ephemeral/` - Short-term memory (session-scoped, like /tmp)
- `working/` - Working memory (task-scoped)
- `persistent/` - Long-term memory (user-scoped)
- `vector/` - Vector memory (semantic search)

## Usage

```python
from memory import ephemeral, working, persistent, vector
```

*Note: Implement memory abstraction based on your needs.*