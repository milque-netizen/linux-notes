#!/usr/bin/env python3
import sys
from datetime import datetime

def add_note(command, description):
    try:
        with open("README.md", "a") as f:
            f.write(f"## {description}\n")
            f.write(f"```bash\n{command}\n```\n")
            f.write(f"*Added on: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        print(f" Success: Note added to README.md")
    except Exception as e:
        print(f" Error writing to file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if we have exactly 2 arguments (excluding the script name)
    if len(sys.argv) != 3:
        print("Usage: note 'command' 'description'")
        print("Example: note 'ls -la' 'List all files with details'")
        sys.exit(1)
    
    # Run the function with arguments from the terminal
    add_note(sys.argv[1], sys.argv[2])
