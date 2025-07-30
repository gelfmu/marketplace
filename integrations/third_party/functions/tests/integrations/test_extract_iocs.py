from ..core.product_iocs import Product
from ..core.session_iocs import MockSession
from ..core.run_script import run_script
from ..core.types import ActionOutput

def test_extract_iocs_success() -> None:
    # Arrange
    session = MockSession()
    product = Product()
    input_text = "Go to https://example.com or email test@mail.com or ping 1.1.1.1"
    parameters = {"Input String": input_text}

    result: ActionOutput = run_script("Extract IOCs", parameters, session, product)

    assert result.success is True
    assert result.results["JsonResult"]["domains"] == ["example.com"]
    assert result.results["JsonResult"]["ips"] == ["1.1.1.1"]
    assert result.results["JsonResult"]["urls"] == ["https://example.com"]
    assert result.results["JsonResult"]["emails"] == ["test@mail.com"]
