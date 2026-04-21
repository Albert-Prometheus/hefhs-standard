# {{project_name}}

A HEFHS-compliant Agentic AI project.

## Quick Start

```bash
# Install dependencies
pip install -e ".[dev]"

# Run the agent
python main.py

# Run tests
pytest
```

## Project Structure

This project follows the HEFHS (Harness Engineering Filesystem Hierarchy Standard).

```
{{project_name}}/
├── agent/              # Agent definitions
├── tool/              # Tool definitions
├── memory/            # Memory storage
├── context/           # Working context
├── state/            # State management
├── config/           # Configuration
├── lib/             # Shared libraries
└── var/             # Variable data
```

## Configuration

Edit `config/default.yaml` to customize your project.

## Documentation

See [HEFHS Standard](https://github.com/hefhs/hefhs-standard) for full specifications.

## License

Licensed under the Apache License, Version 2.0.