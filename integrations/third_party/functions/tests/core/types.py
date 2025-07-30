from typing import Any, Dict

class ActionOutput:
    def __init__(self, success: bool, results: Dict[str, Any]) -> None:
        self.success = success
        self.results = results
