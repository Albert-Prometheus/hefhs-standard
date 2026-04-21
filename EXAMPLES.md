# HEFHS Implementation Examples

This document provides practical examples of how to apply the HEFHS standard in real-world Agentic AI projects.

---

## I. Simple Agent Project

### Structure

```
simple_agent/
├── agent/
│   ├── hello/
│   │   ├── __init__.py
│   │   ├── config.yaml
│   │   └── system_prompt.md
├── tool/
│   ├── echo/
│   │   ├── __init__.py
│   │   └── schema.json
├── memory/
│   └── working/
├── config/
│   └── default.yaml
├── main.py
└── pyproject.toml
```

### Files

#### `agent/hello/config.yaml`

```yaml
agent_name: "hello_agent"
model: "gpt-4o-mini"
temperature: 0.7
max_tokens: 1000
system_prompt_file: "system_prompt.md"
```

#### `agent/hello/system_prompt.md`

```
You are a friendly assistant that always responds in a concise manner.
Your goal is to help users with their questions.
```

#### `tool/echo/__init__.py`

```python
"""Echo tool for testing purposes."""

from dataclasses import dataclass
from typing import Any


@dataclass
class EchoConfig:
    prefix: str = "Echo:"
    uppercase: bool = False


def echo(message: str, config: EchoConfig = None) -> dict[str, Any]:
    """
    Echo back the message with optional transformation.
    
    Args:
        message: The message to echo
        config: Optional configuration
        
    Returns:
        Dict with echoed message
    """
    config = config or EchoConfig()
    result = f"{config.prefix} {message}"
    
    if config.uppercase:
        result = result.upper()
    
    return {"result": result, "original": message}


# Tool metadata for registry
TOOL_NAME = "echo"
TOOL_SCHEMA = {
    "name": "echo",
    "description": "Echo back the input message",
    "parameters": {
        "type": "object",
        "properties": {
            "message": {"type": "string", "description": "Message to echo"},
            "config": {
                "type": "object",
                "properties": {
                    "prefix": {"type": "string"},
                    "uppercase": {"type": "boolean"}
                }
            }
        },
        "required": ["message"]
    }
}
```

#### `tool/echo/schema.json`

```json
{
  "name": "echo",
  "description": "Echo back the input message",
  "input_schema": {
    "type": "object",
    "properties": {
      "message": {
        "type": "string",
        "description": "Message to echo"
      }
    },
    "required": ["message"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "result": {"type": "string"},
      "original": {"type": "string"}
    }
  }
}
```

#### `config/default.yaml`

```yaml
project:
  name: "simple_agent"
  version: "0.1.0"

agent:
  default_model: "gpt-4o-mini"
  default_temperature: 0.7
  timeout: 30

memory:
  type: "ephemeral"
  max_history: 10

logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

#### `main.py`

```python
"""Main entry point for simple agent."""

import yaml
from pathlib import Path

from agent.hello import HelloAgent
from tool.echo import echo, EchoConfig


def load_config(config_path: str = "config/default.yaml") -> dict:
    """Load configuration from YAML file."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def main():
    # Load config
    config = load_config()
    print(f"Starting {config['project']['name']} v{config['project']['version']}")
    
    # Initialize agent
    agent = HelloAgent(config["agent"])
    
    # Run echo tool
    result = echo("Hello, HEFHS!", EchoConfig(prefix=">>>"))
    print(f"Tool result: {result}")
    
    # Process with agent
    response = agent.process("Say hello to the world")
    print(f"Agent response: {response}")


if __name__ == "__main__":
    main()
```

---

## II. Multi-Agent Project (CrewAI Style)

### Structure

```
research_crew/
├── agent/
│   ├── researcher/
│   │   ├── __init__.py
│   │   ├── config.yaml
│   │   └── system_prompt.md
│   ├── writer/
│   │   ├── __init__.py
│   │   ├── config.yaml
│   │   └── system_prompt.md
│   ├── editor/
│   │   ├── __init__.py
│   │   ├── config.yaml
│   │   └── system_prompt.md
│   └── registry.yaml
├── tool/
│   ├── web_search/
│   ├── document_loader/
│   └── pdf_parser/
├── memory/
│   ├── working/
│   │   └── current_task.json
│   └── persistent/
│       └── knowledge_base/
├── context/
│   ├── active/
│   │   └── research_context.json
│   └── template/
│       └── research_template.yaml
├── state/
│   ├── workflow/
│   │   └── research_state.yaml
│   └── session/
└── config/
    ├── default.yaml
    └── environment/
        ├── dev.yaml
        └── prod.yaml
```

### Files

#### `agent/registry.yaml`

```yaml
agents:
  researcher:
    name: "researcher"
    role: "Research Analyst"
    goal: "Find and analyze relevant information"
    tools:
      - web_search
      - document_loader
    
  writer:
    name: "writer"
    role: "Content Writer"
    goal: "Create well-structured content"
    tools:
      - document_loader
    
  editor:
    name: "editor"
    role: "Quality Editor"
    goal: "Review and polish content"
    tools: []

workflow:
  sequence:
    - researcher
    - writer
    - editor
```

#### `agent/researcher/config.yaml`

```yaml
agent_name: "researcher"
role: "Research Analyst"
model: "gpt-4"
temperature: 0.5
max_tokens: 2000
tools:
  - web_search
  - document_loader
memory:
  type: "working"
  context_window: 5
```

#### `agent/researcher/system_prompt.md`

```
You are a research analyst specializing in finding accurate information.
Your responsibilities:
1. Search for relevant information using available tools
2. Analyze and summarize findings
3. Provide citations for all claims

Always verify information from multiple sources when possible.
```

#### `context/template/research_template.yaml`

```yaml
context_type: "research"
version: "1.0"

sections:
  - name: "topic"
    required: true
    description: "Research topic or question"
    
  - name: "scope"
    required: false
    default: "general"
    description: "Depth and breadth of research"
    
  - name: "sources"
    required: false
    description: "Preferred sources or domains"
    
  - name: "output_format"
    required: true
    default: "markdown"
    description: "Desired output format"

memory_prompts:
  short_term: "Focus on the current research question"
  long_term: "Remember user preferences and past research"
```

---

## III. Enterprise Multi-Agent System

### Structure

```
enterprise_ai_platform/
├── agent/
│   ├── orchestrator/
│   ├── specialist/
│   │   ├── code_assistant/
│   │   ├── data_analyst/
│   │   ├── document_processor/
│   │   └── support_agent/
│   └── helper/
├── tool/
│   ├── mcp/
│   │   ├── github/
│   │   ├── slack/
│   │   └── database/
│   └── custom/
│       ├── code_executor/
│       └── data_pipeline/
├── memory/
│   ├── ephemeral/     # Session-scoped
│   ├── working/       # Task-scoped
│   ├── persistent/    # User knowledge
│   └── vector/       # Semantic search
├── context/
│   ├── active/       # Current conversation
│   ├── history/      # Conversation history
│   └── session/      # Session metadata
├── state/
│   ├── agent/        # Per-agent state
│   ├── workflow/     # Workflow execution state
│   ├── session/      # Session state
│   └── metric/       # Metrics and telemetry
├── plugin/
│   ├── auth/         # Authentication plugins
│   ├── billing/      # Billing plugins
│   └── analytics/    # Analytics plugins
├── middleware/
│   ├── rate_limiter/
│   ├── logger/
│   └── validator/
├── config/
│   ├── default.yaml
│   ├── environment/
│   │   ├── dev.yaml
│   │   ├── staging.yaml
│   │   └── prod.yaml
│   └── secrets.enc   # Encrypted secrets
├── var/
│   ├── log/
│   ├── cache/
│   ├── data/
│   └── export/
├── lib/
│   ├── core/         # Core libraries
│   ├── adapter/     # Framework adapters
│   └── utils/       # Utilities
├── doc/
│   ├── api/
│   ├── architecture/
│   └── guide/
└── pyproject.toml
```

### Key Files

#### `agent/orchestrator/config.yaml`

```yaml
agent_name: "orchestrator"
role: "Task Coordinator"
model: "gpt-4-turbo"
temperature: 0.3

coordination:
  max_agents: 5
  timeout_per_agent: 300
  fallback_strategy: "escalate"

routing:
  rules:
    - pattern: "code/*"
      agent: "code_assistant"
    - pattern: "data/*"
      agent: "data_analyst"
    - pattern: "document/*"
      agent: "document_processor"
    - pattern: "*"
      agent: "support_agent"

escalation:
  max_retries: 2
  notify: ["human_supervisor"]
```

#### `config/environment/prod.yaml`

```yaml
environment: "production"

security:
  require_auth: true
  rate_limit:
    requests_per_minute: 60
    burst: 10
  
monitoring:
  enabled: true
  metrics_endpoint: "https://metrics.company.com/agent"
  tracing: true

agents:
  code_assistant:
    model: "gpt-4"
    temperature: 0.2
  data_analyst:
    model: "gpt-4"
    temperature: 0.1

memory:
  vector:
    provider: "pgvector"
    connection: "${DATABASE_URL}"
    dimension: 1536
    
persistence:
  backup:
    enabled: true
    schedule: "0 2 * * *"
    retention_days: 30
```

#### `middleware/rate_limiter/__init__.py`

```python
"""Rate limiting middleware."""

from dataclasses import dataclass
from time import time
from collections import defaultdict


@dataclass
class RateLimitConfig:
    requests_per_minute: int = 60
    requests_per_hour: int = 1000
    burst: int = 10


class RateLimiter:
    """Token bucket rate limiter."""
    
    def __init__(self, config: RateLimitConfig):
        self.config = config
        self.buckets: dict[str, dict] = defaultdict(lambda: {
            "tokens": config.burst,
            "last_refill": time()
        })
    
    def check(self, key: str) -> tuple[bool, dict]:
        """
        Check if request is allowed.
        
        Returns:
            (allowed: bool, info: dict)
        """
        now = time()
        bucket = self.buckets[key]
        
        # Refill tokens
        elapsed = now - bucket["last_refill"]
        refill_rate = self.config.requests_per_minute / 60
        bucket["tokens"] = min(
            self.config.burst,
            bucket["tokens"] + elapsed * refill_rate
        )
        bucket["last_refill"] = now
        
        # Check limit
        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True, {"remaining": int(bucket["tokens"])}
        
        return False, {"retry_after": 1 / refill_rate}
    
    def limit(self, key: str) -> bool:
        """Decorator-style rate limiting."""
        allowed, _ = self.check(key)
        return allowed
```

---

## IV. Migration Examples

### From LangChain Project

**Before (LangChain default)**:

```
langchain_project/
├── chains/
│   └── my_chain.py
├── agents/
│   └── my_agent.py
├── tools/
│   └── my_tool.py
├── memory/
├── embeddings/
└── vectorstores/
```

**After (HEFHS compliant)**:

```
langchain_project/
├── agent/
│   └── my_agent/
│       ├── __init__.py
│       └── config.yaml
├── tool/
│   ├── my_tool/
│   │   ├── __init__.py
│   │   └── schema.json
│   └── _builtin/
│       └── langchain_adapter.py
├── memory/
│   ├── working/
│   └── vector/
├── config/
│   └── default.yaml
└── lib/
    └── chains/
        └── my_chain.py    # Re-located from chains/
```

### From AutoGen Project

**Before (AutoGen default)**:

```
autogen_project/
├── agentchat/
│   ├── assistant/
│   └── user_proxy/
├──oai/
└── cores/
```

**After (HEFHS compliant)**:

```
autogen_project/
├── agent/
│   ├── assistant/
│   │   ├── __init__.py
│   │   └── config.yaml
│   ├── user_proxy/
│   │   ├── __init__.py
│   │   └── config.yaml
│   └── registry.yaml
├── tool/
│   └── oai/    # Mapped from oai/
├── config/
│   └── default.yaml
└── lib/
    └── cores/  # Re-located from cores/
```

---

## V. Testing Patterns

### Unit Test Example

```python
# tests/tool/test_echo.py
import pytest
from tool.echo import echo, EchoConfig


class TestEcho:
    """Tests for echo tool."""
    
    def test_basic_echo(self):
        """Test basic echo functionality."""
        result = echo("hello")
        assert result["result"] == "Echo: hello"
        assert result["original"] == "hello"
    
    def test_uppercase(self):
        """Test uppercase transformation."""
        config = EchoConfig(uppercase=True)
        result = echo("hello", config)
        assert result["result"] == "ECHO: HELLO"
    
    def test_custom_prefix(self):
        """Test custom prefix."""
        config = EchoConfig(prefix=">>>")
        result = echo("test", config)
        assert result["result"] == ">>> test"
    
    def test_empty_message(self):
        """Test with empty message."""
        result = echo("")
        assert result["result"] == "Echo: "
```

### Integration Test Example

```python
# tests/integration/test_agent.py
import pytest
from pathlib import Path
import yaml

from agent.hello import HelloAgent


class TestAgentIntegration:
    """Integration tests for agent."""
    
    @pytest.fixture
    def config(self):
        config_path = Path("config/default.yaml")
        with open(config_path) as f:
            return yaml.safe_load(f)
    
    @pytest.fixture
    def agent(self, config):
        return HelloAgent(config["agent"])
    
    def test_agent_response(self, agent):
        """Test full agent response."""
        response = agent.process("Hello")
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_agent_with_tools(self, agent):
        """Test agent using tools."""
        response = agent.process("Echo test message")
        assert "test message" in response.lower()
```

---

## VI. CI/CD Configuration

### GitHub Actions Example

```yaml
# .github/workflows/test.yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -e ".[dev]"
      
      - name: Run tests
        run: pytest tests/ -v
      
      - name: Validate HEFHS structure
        run: python -m hefhs_validator .
      
      - name: Type check
        run: mypy agent/ tool/
      
      - name: Lint
        run: ruff check agent/ tool/
```

---

## VII. Docker Compose for Development

```yaml
# docker-compose.dev.yaml
services:
  agent_dev:
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - ./agent:/app/agent
      - ./tool:/app/tool
      - ./config:/app/config
    environment:
      - PYTHONPATH=/app
      - LOG_LEVEL=DEBUG
    ports:
      - "8000:8000"
    command: uvicorn main:app --reload

  pgvector:
    image: pgvector/pgvector:pg16
    environment:
      POSTGRES_PASSWORD: dev_password
    ports:
      - "5432:5432"
    volumes:
      - pgvector_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pgvector_data:
```

---

*For more examples, see the HEFHS Standard repository.*
