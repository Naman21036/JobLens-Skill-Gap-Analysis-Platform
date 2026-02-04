import os


PROJECT_STRUCTURE = [
    "data/raw/job_postings",
    "data/raw/resumes",
    "data/raw/skill_demand",
    "data/processed/nlp",
    "data/processed/ml",
    "data/processed/dl",

    "notebooks",

    "src/joblens/nlp",
    "src/joblens/ml",
    "src/joblens/dl",
    "src/joblens/utils",

    "scripts",
    "artifacts/models",
    "artifacts/reports",
    "tests"
]


def create_structure():
    for path in PROJECT_STRUCTURE:
        os.makedirs(path, exist_ok=True)
        print(f"created {path}")


def create_init_files():
    init_paths = [
        "src/joblens/__init__.py",
        "src/joblens/nlp/__init__.py",
        "src/joblens/ml/__init__.py",
        "src/joblens/dl/__init__.py",
        "src/joblens/utils/__init__.py",
    ]

    for file_path in init_paths:
        with open(file_path, "w"):
            pass
        print(f"created {file_path}")


if __name__ == "__main__":
    create_structure()
    create_init_files()
    print("project structure created successfully")
