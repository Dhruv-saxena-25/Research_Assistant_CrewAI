import os

# Define the file and folder structure directly at the script's location
structure = {
    "app.py": "",
    ".env": "",
    "requirements.txt": "",
    "pyproject.toml": "",
    ".streamlit": {
        "secrets.toml": ""
    },
    "assets": {},  # Empty, placeholder for static files
    "experiment": {
        "run.py": ""
    },
    "src": {
        "__init__.py": "",
        "crew.py": "",
        "agents": {
            "__init__.py": "",
            "agent.py": ""
        },
        "llms": {
            "__init__.py": "",
            "init_llms.py": ""
        },
        "tasks": {
            "__init__.py": "",
            "task.py": ""
        },
        "tools": {
            "__init__.py": "",
            "custum_tool.py": ""
        },
        "UI": {
            "__init__.py": "",
            "sidebar.py": ""
        },
        "utils": {
            "__init__.py": "",
            "output_handler.py": ""
        }
    }
}

def create_structure(base_path, tree):
    for name, content in tree.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(base_path, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory where template.py is located
    create_structure(current_dir, structure)
    print("✅ Project structure created successfully in the current directory.")
