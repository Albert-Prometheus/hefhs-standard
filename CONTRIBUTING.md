# Contributing to HEFHS Standard

<!-- Introduction: Welcome message and brief overview -->
Thank you for your interest in contributing to the HEFHS (Harness Engineering Filesystem Hierarchy Standard) initiative.

<!-- Vision: Explains the goal and scope of HEFHS -->
## HEFHS Vision

HEFHS aims to establish a community-driven standard for:
- Directory structure conventions in Agentic AI projects
- Naming conventions for variables, classes, and resources
- Cross-framework consistency across different Agent frameworks

<!-- Ways to Contribute: Three main channels for participation -->
## Ways to Contribute

### 1. Proposing Changes

The easiest way to contribute is to open an issue to discuss:
- New directory structure proposals
- Naming convention suggestions
- Framework compatibility mappings
- Real-world use cases

### 2. Submitting Improvements

If you've implemented HEFHS in a project:
- Share your experience
- Propose modifications to the standard
- Submit additional examples

### 3. Developing Tools

Help build the HEFHS ecosystem:
- Validators for other languages
- Migration scripts
- IDE plugins
- Documentation improvements

<!-- Getting Started: Prerequisites and basic setup steps -->
## Getting Started

### Setting Up Your Environment

```bash
# Clone the repository
git clone https://github.com/hefhs/hefhs-standard.git
cd hefhs-standard

# Explore the structure
ls -la
cat HEFHS.md
```

<!-- Validating Your Project: Using the CLI validator -->
### Validating Your Project

```bash
# Use the Python validator
python hefhs_validator.py /path/to/your/project

# With automatic fixes
python hefhs_validator.py /path/to/your/project --fix
```

## Pull Request Process

### 1. Fork the Repository

Click the "Fork" button on GitHub or run:
```bash
git fork https://github.com/hefhs/hefhs-standard.git
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/description-of-fix
```

### 3. Make Your Changes

Follow these guidelines:
- Keep changes focused and atomic
- Update documentation if needed
- Add examples when proposing new features

### 4. Submit a Pull Request

Fill in the required template:

```markdown
## Description
Briefly describe your changes.

## Motivation
Explain why this change is needed.

## Changes
- List specific changes made
- Include file names where relevant

## Testing
- Describe how you tested your changes
- Include validation results if applicable

## Related Issues
Link any related issues using #issue-number
```

## Commit Message Style

Use conventional commits:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `example`: Adding examples
- `refactor`: Restructuring without behavior change
- `tool`: Adding or updating tools

Examples:
```
feat(agent): add orchestrator directory structure
fix(validator): correct snake_case detection logic
docs(examples): add enterprise multi-agent example
example(tool): add migration script for AutoGen
```

## Review Criteria

Pull requests are reviewed based on:

| Criterion | Description |
|-----------|-------------|
| **Clarity** | Is the proposal clearly documented? |
| **Compatibility** | Does it work with major frameworks? |
| **Evidence** | Is there a real-world use case? |
| **Extensibility** | Can the proposal handle future growth? |
| **Consistency** | Does it follow existing patterns? |

## Communication

### Issues
- Use GitHub Issues for proposals and discussions
- Tag issues appropriately (`proposal`, `question`, `example`)
- Search existing issues before creating new ones

### Discussions
- Use GitHub Discussions for questions
- Be respectful and constructive
- Focus on technical merit

## Recognition

Contributors are recognized in:
- CONTRIBUTORS.md file
- GitHub commit history
- Release notes (for significant contributions)

---

**Thank you for contributing to HEFHS!**

By contributing, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).