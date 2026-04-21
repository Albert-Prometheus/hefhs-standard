# Hacker News Show - HEFHS Announcement

---

## Title

HEFHS: A Filesystem Standard for Agentic AI Projects (inspired by Linux FHS + PEP 8)

---

## Body

## What is this?

I've been building AI agent applications for a while, and I noticed that every project has the same chaos:

- Where do I put agent definitions?
- What's the naming convention for tools?
- How do I structure memory?

Every team invents their own structure. Switching frameworks means starting over.

I created **HEFHS** — a community-driven standard for organizing Agentic AI projects.

## It works like this:

```
hefhs_project/
├── agent/              # Agent definitions
├── tool/              # Tool definitions
├── memory/            # Memory storage
├── context/           # Working context
├── state/            # State management
├── config/           # Configuration
├── lib/              # Shared libraries
└── var/              # Logs & cache
```

Plus PEP 8 naming:
- `snake_case` for files
- `PascalCase` for classes

## Framework compatibility:

| Framework | Maps to HEFHS |
|-----------|--------------|
| OpenCode | Direct match |
| LangChain | /tool/ |
| AutoGen | /agent/ |
| Claude | /agent/, /tool/ |
| Codex | /agent/ |

## What's included:

- Standard document
- CLI validator
- Project scaffold template
- Examples

## License: Apache 2.0

---

## Comments

I'd love your feedback! 

- Is this useful?
- What would you change?
- What frameworks should I add?

---