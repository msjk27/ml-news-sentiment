import os

folder_structure = [
    "data/raw", "data/processed", "data/external",
    "src/crawling", "src/preprocessing", "src/analysis",
    "src/models", "src/app", "notebooks", "config"
]

base_files = {
    "README.md": "# Financial News Market Analysis",
    "requirements.txt": "",
    ".gitignore": "__pycache__/\n*.pyc\ndata/raw/\ndata/processed/\ndata/external/\nconfig/config.json\n.env",
    "config/config_template.json": "{\n  \"news_api_key\": \"your_api_key_here\"\n}",
    "src/__init__.py": "",
    "src/crawling/__init__.py": "",
    "src/preprocessing/__init__.py": "",
    "src/analysis/__init__.py": "",
    "src/models/__init__.py": "",
    "src/app/__init__.py": "",
}

for path in folder_structure:
    os.makedirs(path, exist_ok=True)

for filepath, content in base_files.items():
    with open(filepath, "w") as f:
        f.write(content)

print("✅ Folder structure and base files created.")
