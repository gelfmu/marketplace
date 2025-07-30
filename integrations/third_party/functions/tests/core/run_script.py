from ..core.types import ActionOutput

def run_script(script_name: str, parameters: dict, session, product) -> ActionOutput:
    input_str = parameters.get("Input String", "")

    return ActionOutput(
        success=True,
        results={
            "JsonResult": {
                "domains": ["example.com"] if "example.com" in input_str else [],
                "ips": ["1.1.1.1"] if "1.1.1.1" in input_str else [],
                "urls": ["https://example.com"] if "https://example.com" in input_str else [],
                "emails": ["test@mail.com"] if "test@mail.com" in input_str else [],
            }
        }
    )
