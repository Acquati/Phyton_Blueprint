import json
from pathlib import Path
from typing import Any


def load_config(file_path: str, default_values: dict[str, Any] | None = None) -> dict[str, Any]:
	if default_values is None:
		default_values = {}
	try:
		data = json.loads(Path(file_path).read_text(encoding="utf-8"))
		config = default_values.copy()
		config.update(data)
		return config
	except FileNotFoundError:
		print(f"Config file not found at {file_path}, using defaults.")
		return default_values
	except json.JSONDecodeError:
		print(f"Error decoding JSON from {file_path}, using defaults.")
		return default_values


def save_config(file_path: str, data: dict[str, Any]) -> None:
	try:
		path = Path(file_path)
		path.parent.mkdir(parents=True, exist_ok=True)
		path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
	except Exception as exception:
		print(f"Error saving config: {exception}")
