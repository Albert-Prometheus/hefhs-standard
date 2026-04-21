"""Main entry point for HEFHS project.

This is a placeholder main.py following HEFHS conventions.
"""

import yaml
from pathlib import Path


def load_config(config_path: str = "config/default.yaml") -> dict:
    """Load configuration from YAML file."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def main():
    """Main entry point."""
    config = load_config()
    print(f"Starting {config['project']['name']} v{config['project']['version']}")
    print("HEFHS-compliant project initialized.")
    print("\nProject structure:")
    print("  agent/ - Agent definitions")
    print("  tool/ - Tool definitions")
    print("  memory/ - Memory storage")
    print("  config/ - Configuration")
    print("\nEdit config/default.yaml to customize.")


if __name__ == "__main__":
    main()