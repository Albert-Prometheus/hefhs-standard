#!/usr/bin/env python3
"""
HEFHS Validator - CLI tool for validating project structure compliance.

Usage:
    python hefhs_validator.py /path/to/project
    python hefhs_validator.py /path/to/project --fix
    python hefhs_validator.py /path/to/project --json
"""

import argparse
import json
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class Issue:
    severity: Severity
    message: str
    path: Optional[str] = None
    fixable: bool = False


@dataclass
class ValidationResult:
    valid: bool
    issues: list[Issue] = field(default_factory=list)
    
    def add_issue(self, severity: Severity, message: str, path: str = None, fixable: bool = False):
        self.issues.append(Issue(severity, message, path, fixable))
        if severity == Severity.ERROR:
            self.valid = False


class HEFHSValidator:
    """Validates projects against HEFHS standard."""
    
    REQUIRED_DIRS = ["agent", "tool", "config"]
    OPTIONAL_DIRS = [
        "memory", "context", "state", "workspace", "var", "lib", "doc",
        "plugin", "middleware", "metric", "audit"
    ]
    
    # snake_case directories
    DIRECTORY_RULES = {
        "agent": "Agent definitions and configs",
        "tool": "Tool/MCP tool definitions",
        "memory": "Agent memory storage",
        "context": "Working context data",
        "state": "State management",
        "workspace": "Execution workspace",
        "config": "Configuration files (/etc equivalent)",
        "var": "Variable data (logs, cache)",
        "lib": "Shared libraries (/usr/lib equivalent)",
        "doc": "Documentation (/usr/share/doc equivalent)",
    }
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.result = ValidationResult(valid=True)
    
    def validate(self) -> ValidationResult:
        """Run all validations."""
        if not self.project_path.exists():
            self.result.add_issue(
                Severity.ERROR,
                f"Project path does not exist: {self.project_path}"
            )
            return self.result
        
        if not self.project_path.is_dir():
            self.result.add_issue(
                Severity.ERROR,
                f"Path is not a directory: {self.project_path}"
            )
            return self.result
        
        self._validate_required_directories()
        self._validate_naming_conventions()
        self._validate_file_structure()
        self._validate_config_files()
        
        return self.result
    
    def _validate_required_directories(self):
        """Check for required top-level directories."""
        existing_dirs = [d.name for d in self.project_path.iterdir() if d.is_dir()]
        
        for required in self.REQUIRED_DIRS:
            if required not in existing_dirs:
                self.result.add_issue(
                    Severity.ERROR,
                    f"Missing required directory: {required}",
                    fixable=True
                )
        
        # Check for non-standard directories
        for dir_name in existing_dirs:
            if dir_name.startswith('.') or dir_name.startswith('_'):
                continue
            if dir_name not in self.REQUIRED_DIRS + self.OPTIONAL_DIRS:
                self.result.add_issue(
                    Severity.WARNING,
                    f"Non-standard directory: {dir_name} (consider adding to HEFHS structure)"
                )
    
    def _validate_naming_conventions(self):
        """Check naming conventions."""
        for item in self.project_path.rglob("*"):
            if not item.is_file():
                continue
            
            name = item.name
            
            # Check Python files use snake_case
            if name.endswith(".py"):
                if "_" not in name and name != "__init__.py" and name != "__main__.py":
                    # Exception for single-word modules
                    if len(name.replace(".py", "")) > 1:
                        self.result.add_issue(
                            Severity.WARNING,
                            f"Python file should use snake_case: {name}",
                            path=str(item.relative_to(self.project_path))
                        )
            
            # Check YAML files
            elif name.endswith((".yaml", ".yml")):
                if "_" not in name and name not in ["docker-compose.yaml"]:
                    self.result.add_issue(
                        Severity.WARNING,
                        f"YAML file should use snake_case: {name}",
                        path=str(item.relative_to(self.project_path))
                    )
            
            # Check directories use snake_case
            elif item.is_dir():
                if "_" not in name and name not in ["agent", "tool", "lib"]:
                    # Allow common exceptions
                    if name.lower() not in ["test", "tests", "docs", "src", "bin"]:
                        self.result.add_issue(
                            Severity.WARNING,
                            f"Directory should use snake_case: {name}",
                            path=str(item.relative_to(self.project_path))
                        )
    
    def _validate_file_structure(self):
        """Validate specific directory structures."""
        # Check agent/ structure
        agent_dir = self.project_path / "agent"
        if agent_dir.exists():
            self._validate_agent_directory(agent_dir)
        
        # Check tool/ structure
        tool_dir = self.project_path / "tool"
        if tool_dir.exists():
            self._validate_tool_directory(tool_dir)
    
    def _validate_agent_directory(self, agent_dir: Path):
        """Validate agent subdirectories."""
        for item in agent_dir.iterdir():
            if not item.is_dir():
                continue
            
            # Each agent should have config.yaml
            config_file = item / "config.yaml"
            if not config_file.exists():
                self.result.add_issue(
                    Severity.WARNING,
                    f"Agent '{item.name}' missing config.yaml",
                    path=str(item.relative_to(self.project_path))
                )
    
    def _validate_tool_directory(self, tool_dir: Path):
        """Validate tool subdirectories."""
        for item in tool_dir.iterdir():
            if not item.is_dir():
                continue
            
            # Each tool should have __init__.py
            init_file = item / "__init__.py"
            if not init_file.exists():
                self.result.add_issue(
                    Severity.WARNING,
                    f"Tool '{item.name}' missing __init__.py",
                    path=str(item.relative_to(self.project_path))
                )
    
    def _validate_config_files(self):
        """Validate configuration files."""
        config_dir = self.project_path / "config"
        
        if config_dir.exists():
            default_config = config_dir / "default.yaml"
            if not default_config.exists():
                self.result.add_issue(
                    Severity.WARNING,
                    "Missing config/default.yaml",
                    fixable=True
                )
    
    def fix(self) -> int:
        """Apply automatic fixes."""
        fixes_applied = 0
        
        # Create missing required directories
        for required in self.REQUIRED_DIRS:
            dir_path = self.project_path / required
            if not dir_path.exists():
                dir_path.mkdir()
                self.result.add_issue(
                    Severity.INFO,
                    f"Created directory: {required}"
                )
                fixes_applied += 1
        
        # Create default config
        config_dir = self.project_path / "config"
        if config_dir.exists():
            default_config = config_dir / "default.yaml"
            if not default_config.exists():
                default_config.write_text("""# HEFHS Default Configuration
project:
  name: "hefhs_project"
  version: "1.0.0"

agent:
  default_model: "gpt-4"
  default_temperature: 0.7
  timeout: 30

memory:
  type: "ephemeral"
  max_history: 10

logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
""")
                self.result.add_issue(
                    Severity.INFO,
                    "Created config/default.yaml"
                )
                fixes_applied += 1
        
        return fixes_applied


def print_results(result: ValidationResult, json_output: bool = False):
    """Print validation results."""
    if json_output:
        output = {
            "valid": result.valid,
            "issues": [
                {
                    "severity": i.severity.value,
                    "message": i.message,
                    "path": i.path,
                    "fixable": i.fixable
                }
                for i in result.issues
            ]
        }
        print(json.dumps(output, indent=2))
        return
    
    # Human-readable output
    error_count = sum(1 for i in result.issues if i.severity == Severity.ERROR)
    warning_count = sum(1 for i in result.issues if i.severity == Severity.WARNING)
    info_count = sum(1 for i in result.issues if i.severity == Severity.INFO)
    
    print(f"\n{'='*60}")
    print(f"HEFHS Validation Results")
    print(f"{'='*60}")
    print(f"Status: {'✓ PASS' if result.valid else '✗ FAIL'}")
    print(f"  Errors:   {error_count}")
    print(f"  Warnings: {warning_count}")
    print(f"  Info:     {info_count}")
    
    if result.issues:
        print(f"\n{'='*60}")
        print("Issues:")
        print(f"{'='*60}")
        
        for issue in result.issues:
            icon = {
                Severity.ERROR: "✗",
                Severity.WARNING: "⚠",
                Severity.INFO: "ℹ"
            }[issue.severity]
            
            msg = f"{icon} [{issue.severity.value.upper()}] {issue.message}"
            if issue.path:
                msg += f"\n    at: {issue.path}"
            if issue.fixable:
                msg += " [FIXABLE]"
            print(msg)
    
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Validate project structure against HEFHS standard"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to project directory (default: current directory)"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Apply automatic fixes where possible"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )
    
    args = parser.parse_args()
    
    project_path = Path(args.path).resolve()
    validator = HEFHSValidator(project_path)
    
    if args.fix:
        fixes = validator.fix()
        print(f"Applied {fixes} automatic fix(es)")
    
    result = validator.validate()
    
    # Treat warnings as errors in strict mode
    if args.strict and not result.valid:
        result.valid = False
    
    print_results(result, args.json)
    
    sys.exit(0 if result.valid else 1)


if __name__ == "__main__":
    main()
