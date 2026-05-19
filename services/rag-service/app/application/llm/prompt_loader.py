from pathlib import Path

class PromptLoader:
    def __init__(self, base_path: Path | None = None):
        if base_path is None:
            base_path = Path(__file__).parent / "prompts"
        self.base_path = base_path

    def load(self, name: str)-> str:
        path = self.base_path / f"{name}.txt"

        if not path.exists():
            raise FileNotFoundError(f"Prompt '{name}' not found")
        return path.read_text(encoding = "utf-8")