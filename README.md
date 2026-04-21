# HEFHS: Harness Engineering Filesystem Hierarchy Standard

<!-- Badges: License, Version, GitHub link -->
<p align="center">
  <a href="https://github.com/Albert-Prometheus/hefhs-standard">
    <img src="https://img.shields.io/badge/github-hefhs--standard-blue?style=flat&logo=github" alt="GitHub">
  </a>
  <a href="https://github.com/Albert-Prometheus/hefhs-standard/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%202.0-green?style=flat" alt="License">
  </a>
  <a href="https://github.com/Albert-Prometheus/hefhs-standard/releases">
    <img src="https://img.shields.io/badge/version-1.0.0-yellow?style=flat" alt="Version">
  </a>
</p>

> A community-driven standard for organizing Agentic AI projects, inspired by Linux FHS and Python PEP 8.

<!-- Quick Summary: What HEFHS provides and why it matters -->

## What is HEFHS?

**HEFHS** (Harness Engineering Filesystem Hierarchy Standard) provides a consistent directory structure and naming conventions for Agentic AI projects. It helps teams:

- **Discoverability** - File locations are predictable
- **Portability** - Cross-framework compatibility
- **Readability** - Naming is self-documenting
- **Consistency** - Shared language across teams

<!-- Design Philosophy: Explains the two main inspirations (Linux FHS + PEP 8) -->
## Design Philosophy

| Linux FHS | PEP 8 (Python) | HEFHS |
|----------|---------------|-------|
| `/usr`, `/etc`, `/var` | `snake_case` | `/agent`, `/tool`, `/memory`, `/context` |
| Clear directory responsibility | Readable naming style | Semantic structure |
| Predictable locations | Style consistency | Portable conventions |

**Core Values:**
- **Discoverability** - File location is predictable
- **Portability** - Cross-framework compatibility
- **Readability** - Naming is documentation
- **Consistency** - Shared team language

<!-- Quick Start: Minimal example to get users up and running quickly -->
## Quick Start

### Directory Structure

```
hefhs_project/
├── agent/              # Agent definitions and configs
├── tool/              # Tool definitions
├── memory/            # Memory storage
├── context/           # Working context data
├── state/             # State management
├── config/            # Configuration files
├── lib/              # Shared libraries
└── var/              # Variable data (logs, cache)
```

### Minimal Example

```bash
# Clone the scaffold
git clone https://github.com/hefhs/hefhs-standard
cd hefhs-standard/project_scaffold

# Customize
edit config/default.yaml

# Validate structure
python ../hefhs_validator.py .
```

<!-- Installation: How to install the HEFHS validator tool -->
## Installation

```bash
pip install hefhs-validator
```

## Usage

```bash
# Validate your project
hefhs-validator /path/to/project

# With automatic fixes
hefhs-validator /path/to/project --fix

# JSON output
hefhs-validator /path/to/project --json
```

<!-- Framework Users: Shows compatibility with major Agentic AI frameworks -->
## For Framework Users

| Framework | Map to HEFHS |
|-----------|--------------|
| OpenCode (Oh-My-OpenAgent) | `/agent/`, `/tool/`, `/memory/`, `/context/` (direct mapping) |
| LangChain | `/langchain_modules/` → `/tool/` |
| AutoGen | `/agent/` (direct mapping) |
| CrewAI | `/crew/` → `/agent/` |
| OpenManus | `/tool/` (direct mapping) |
| Claude (Anthropic) | `/agent/`, `/tool/`, `/memory/` (direct mapping) |
| Codex (OpenAI) | `/agent/`, `/tool/` (direct mapping) |

See [EXAMPLES.md](EXAMPLES.md) for detailed mappings.

<!-- Why Standardize: Demonstrates the problem HEFHS solves (before/after comparison) -->
## Why Standardize?

### Before HEFHS

```
my-ai-app/
├── agents.py
├── new_agent.py
├── helpers.py
├── Toolz.py
├── memory_file.json
├── ctx.data
└── config.yml
```

### After HEFHS

```
my-ai-app/
├── agent/
│   ├── assistant/
│   │   ├── config.yaml
│   │   └── system_prompt.md
│   └── registry.yaml
├── tool/
│   ├── web_search/
│   │   ├── __init__.py
│   │   └── schema.json
│   └── document_loader/
├── memory/
│   ├── working/
│   └── persistent/
├── context/
│   └── active/
└── config/
    └── default.yaml
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md).

1. **Open an issue** to discuss proposals
2. **Share your use case** with real-world examples
3. **Submit improvements** via PR

## Community

- **Discussions**: https://github.com/Albert-Prometheus/hefhs-standard/discussions
- **Issues**: https://github.com/Albert-Prometheus/hefhs-standard/issues

## License

Licensed under [Apache License 2.0](LICENSE).

<!-- SimilarEfforts: References to related standards that inspired HEFHS -->
## SimilarEfforts

- [Linux FHS](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) - Filesystem Hierarchy Standard
- [PEP 8](https://peps.python.org/pep-0008/) - Python Style Guide
- [MCP Specification](https://spec.modelcontextprotocol.io/) - Model Context Protocol

---

**Join us in building the standard for Agentic AI development!**

⭐ If you find HEFHS useful, please star the repo!