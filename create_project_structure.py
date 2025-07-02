import os


def create_file(path, content=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {path}")


def create_project_structure(root_dir):
    # 定义目录和文件结构
    structure = {
        "rentals_agent": {
            "__init__.py": "",
            "strategy_engine.py": "# strategy_engine module\n",
            "config": {
                "__init__.py": "",
                "config_reader.py": "# config_reader module\n",
                "user_config.yaml": "# User preferences configuration\n",
                "test_strategy_engine.py": (
                    "import unittest\n"
                    "from rentals_agent.strategy_engine import StrategyEngine\n\n"
                    "class TestStrategyEngine(unittest.TestCase):\n"
                    "    def test_example(self):\n"
                    "        self.assertTrue(True)\n\n"
                    "if __name__ == '__main__':\n"
                    "    unittest.main()\n"
                ),
            },
        },
        "README.md": "# Rentals Agent Project\n\nProject description here.\n",
        "requirements.txt": "PyYAML\n",
    }

    def _create(path, struct):
        for name, content in struct.items():
            current_path = os.path.join(path, name)
            if isinstance(content, dict):
                os.makedirs(current_path, exist_ok=True)
                print(f"Created directory: {current_path}")
                _create(current_path, content)
            else:
                create_file(current_path, content)

    _create(root_dir, structure)
    print("Project structure created successfully.")


if __name__ == "__main__":
    root_directory = input("Enter your project root directory path: ").strip()
    if not os.path.exists(root_directory):
        os.makedirs(root_directory)
        print(f"Created root directory: {root_directory}")
    create_project_structure(root_directory)
