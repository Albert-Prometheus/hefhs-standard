# HEFHS: Harness Engineering Filesystem Hierarchy Standard

## A Proposal for Standardizing Agentic AI Directory Structures and Naming Conventions

---

## Proposal Overview

**HEFHS** (Harness Engineering Filesystem Hierarchy Standard)

Inspired by Linux FHS and Python PEP 8, aiming to establish a community-driven standard for:

1. **Directory structure conventions** for Agentic AI projects
2. **Naming conventions** for variables, classes, and resources
3. **Cross-framework consistency** across different Agent frameworks

---

## I. Core Philosophy

### Design Principles

| Linux FHS | PEP 8 (Python) | HEFHS |
|----------|---------------|-------|
| `/usr`, `/etc`, `/var` | `snake_case` | `/agent`, `/tool`, `/memory`, `/context` |
| Clear directory responsibility | Readable naming style | Semantic structure |
| Predictable locations | Style consistency & readability | Portable conventions |

### Core Values

| Value | Description |
|-------|-------------|
| **Discoverability** | File location is predictable |
| **Portability** | Cross-framework compatibility |
| **Readability** | Naming is documentation |
| **Consistency** | Shared language across teams |

---

## II. Directory Structure Standard (HEFHS-FHS)

### Top-Level Directory Layout

```
hefhs_project/
├── agent/              # Agent definitions and configs
├── tool/              # Tool/MCP tool definitions
├── memory/            # Agent memory storage
├── context           # Working context data
├── state/            # State management
├── workspace/        # Execution workspace
├── config/           # Configuration files (/etc equivalent)
├── var/              # Variable data (logs, cache)
├── lib/             # Shared libraries (/usr/lib equivalent)
└── doc/             # Documentation (/usr/share/doc equivalent)
```

### Detailed Structure

```
agent/
├── {agent_name}/
│   ├── config.yaml         # Agent configuration
│   ├── system_prompt.md # System prompt
│   └── tools.yaml        # Tool whitelist
├── registry.yaml        # Global agent registry
└── _builtin/          # Built-in agent templates

tool/
├── {tool_name}/
│   ├── __init__.py      # Tool entry point
│   ├── config.yaml      # Tool configuration
│   └── schema.json    # Input/Output schema
├── registry.yaml     # Global tool registry
└── _builtin/      # Built-in tools

memory/
├── ephemeral/          # Short-term memory (/tmp equivalent)
├── working/          # Working memory (session-level)
├── persistent/       # Long-term memory (/var equivalent)
└── vector/          # Vector memory (optional pgvector)

context/
├── active/            # Currently active context
├── history/           # Context history
└── template/         # Context templates

state/
├── agent/             # Per-agent state
├── session/           # Session state
└── workflow/          # Workflow state

config/
├── default.yaml        # Default configuration
├── environment/       # Environment configs (dev/staging/prod)
└── secrets.yaml       # Sensitive config (encrypted)

var/
├── log/               # Log directory
├── cache/             # Cache directory
└── data/              # Data exports
```

### Optional Modules

```
# Project-specific additions
├── plugin/             # Plugin extensions
├── middleware/        # Middleware
├── metric/           # Metrics collection
└── audit/            # Audit logs
```

---

## III. Naming Conventions (HEFHS-PEP8)

### Basic Rules

| Type | Style | Example | Source |
|------|-------|---------|--------|
| Variables | snake_case | `agent_context` | PEP 8 |
| Constants | SCREAMING_SNAKE_CASE | `DEFAULT_TIMEOUT` | PEP 8 |
| Classes | PascalCase | `AgentConfig` | PEP 8 |
| Files | snake_case | `agent_config.py` | PEP 8 |
| Directories | snake_case | `agent_context/` | FHS-inspired |

### Agentic AI Extensions

```python
# ===== Agent Conventions =====
agent_name: str          # Agent instance (matches directory name)
agent_config: dict       # Configuration object
_agent: object           # Private agent instance
BaseAgent: class         # Base class (PEP 8)

# ===== Tool Conventions =====
tool_name: str           # Tool name
tool_handler: callable # Tool handler
tool_schema: dict      # Tool definition
register_tool(): func   # Registration function

# ===== Context Conventions =====
context: dict           # Context object
context_id: str         # Context identifier
ctx: object            # Short form
_context: object        # Private context

# ===== Memory Conventions =====
memory: object          # Memory abstraction
short_term: list       # Short-term memory
long_term: dict        # Long-term memory
embedding: np.ndarray   # Vector embedding

# ===== State Conventions =====
state: dict            # State object
session_id: str        # Session identifier
workflow_state: str   # Workflow state
```

### Discouraged Patterns

```python
# AVOID
agentName = "gpt4"           # mixedCase (not PEP 8)
AgentConfig = {}               # Starts with capital (class style)
agent_dict = {}               # Type prefix
AGENT_CONFIG = {}              # Constant style (but not constant)

# PREFERRED
agent_name = "gpt-4"
AGENT_CONFIG = {}             # If truly constant
agent_config = {}             # If configuration object
def register_agent(): ...     # Verb function
class AgentRegistry: ...        # Noun class
```

### Tool Naming

```python
# Tool function names
def translate_text(): ...      # snake_case + descriptive verb
def search_documents(): ...
def calculate_embedding(): ...

# Tool configuration
TOOL_CONFIG = {              # Module-level constant
    "timeout": 30,
    "retry": 3
}

# Tool registry
class ToolRegistry:
    _tools: Dict[str, Tool]  # Private tools dict
```

---

## IV. Implementation Examples

### Standard Project Structure

```
my_agent_project/
├── pyproject.toml
├── agent/
│   ├── assistant/
│   │   ├── __init__.py
│   │   ├── config.yaml
│   │   └── tool_list.yaml
│   └── _builtin/
│       └── base_agent.py
├── tool/
│   ├── web_search/
│   │   ├── __init__.py
│   │   └── schema.json
│   └── document_loader/
│       ├── __init__.py
│       └── schema.json
├── memory/
│   ├── working/
│   │   └── session_001.json
│   └── persistent/
│       └── user_knowledge/
├── context/
│   └── active/
│       └── current.json
├── config/
│   ├── default.yaml
│   └── environment/
│       ├── dev.yaml
│       └── prod.yaml
└── var/
    └── log/
        └── agent.log
```

### Python Implementation

```python
# agent/assistant/config.yaml
agent_name: "research_assistant"
model: "gpt-4"
temperature: 0.7

# tool/web_search/__init__.py
from dataclasses import dataclass

@dataclass
class ToolConfig:
    max_results: int = 10
    timeout: int = 30

def search_web(query: str, tool_config: ToolConfig = None) -> dict:
    """Search the web for relevant information."""
    tool_config = tool_config or ToolConfig()
    # implementation
    return {"results": [], "query": query}

# usage
from my_project.tool.web_search import search_web, ToolConfig
from my_project.agent.assistant import ResearchAssistant

config = ToolConfig(max_results=5)
result = search_web("HEFHS standard", config)
```

---

## V. Framework Compatibility

### Existing Framework Mapping

| Framework | HEFHS Structure | Notes |
|-----------|----------------|-------|
| **LangChain** | `/langchain_modules/` | Maps to `/tool/` |
| **AutoGen** | `/agent/` | Direct mapping |
| **CrewAI** | `/crew/` | Maps to `/agent/` |
| **OpenAI Assistants** | `/assistant/` | Cloud abstraction |
| **OpenManus** | `/tool/` | Direct mapping |

### Migration Strategy

```bash
# Existing project → HEFHS structure
# Recommended script
migrate_to_hefhs.py
├── scan_existing_structure()
├── create_directory_mapping()
├── move_files_with_metadata()
└── update_import_references()
```

---

## VI. Proposal Information

### GitHub Repository Structure

```
hefhs-standard/
├── HEFHS.md              # Main standard document
├── EXAMPLES.md          # Implementation examples
├── TOOLS/               # Supporting tools
│   ├── hefhs_validator.py
│   └── hefhs_migrator.py
├── TEMPLATES/           # Project templates
│   └── project_scaffold/
└── .github/
    └── ISSUE_TEMPLATE.md
```

### Community Value

| Stakeholder | Benefit |
|------------|---------|
| **Framework Developers** | Reduced learning curve via standardization |
| **AI Developers** | Portability and best practices |
| **Enterprise** | Reduced operational cost via standardization |
| **Educators** | Clear architecture aids teaching |

### Initial Goals

- [ ] Establish core conventions (directory + naming)
- [ ] Release validation tool (CLI)
- [ ] Collect 5+ real project case studies
- [ ] Obtain official acknowledgment from major frameworks
- [ ] Establish contribution guidelines

---

## VII. Open Questions

1. **Should `/agent/orchestrator/` level be included?** (Multi-agent coordination)
2. **Default vector memory storage strategy?** (Local vs. remote)
3. **Secret management approach?** (Environment vars vs. encrypted files)
4. **Version numbering needed?** (HEFHS v1.0?)
5. **Formal distinction from FHS?** (Non-POSIX compliant)

---

## VIII. How to Contribute

### Quick Start

```bash
# Clone and explore
git clone https://github.com/hefhs/hefhs-standard.git
cd hefhs-standard

# Review the standard
cat HEFHS.md

# Share your use case
# Open an issue: https://github.com/hefhs/hefhs-standard/issues
```

### Contributing

1. **Fork** the repository
2. **Create** a feature branch
3. **Submit** a PR with your proposed changes
4. **Join** the discussion

### Code of Conduct

- Be respectful and constructive
- Focus on technical merit
- Welcome newcomers and diverse perspectives

---

## IX. Appendix

### A. Glossary

| Term | Definition |
|------|------------|
| **Agent** | Autonomous AI entity that can execute tasks |
| **Tool** | MCP-compatible function/plugin |
| **Context** | Working data passed to Agent |
| **Memory** | Persistent state across sessions |
| **HEFHS** | Harness Engineering Filesystem Hierarchy Standard |

### B. References

- [Linux FHS](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
- [PEP 8](https://peps.python.org/pep-0008/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

### C. Similar Efforts

- [Structurer](https://github.com/structurer) - Project structure validator
- [Best-of.py](https://github.com/ml-tooling/best-of-python) - Python project conventions

---

> **Note**: This standard is intended as a convention, not a mandatory requirement. Adoption is optional and can be adapted to specific project needs.

---

**Repository**: https://github.com/hefhs/hefhs-standard

**Discussion**: https://github.com/hefhs/hefhs-standard/issues

**License**: MIT

---

*Proposed by: HEFHS Initiative*

*Last Updated: 2026-04-21*