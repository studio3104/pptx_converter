from pptx import Presentation

from pptx_converter import extract_content


def test_app(fx_simple_pptx: Presentation) -> None:
    extract_content(fx_simple_pptx)
