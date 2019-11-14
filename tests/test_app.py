from pptx import Presentation

from pptx_converter import extract_content


def test_app(fx_simple_pptx: Presentation) -> None:
    contents = extract_content(fx_simple_pptx)
    assert contents == [
        {
            'title': 'Test Presentation Title',
            'texts': ['Test Presentation Subtitle'],
        },
        {
            'title': 'Test Page Title',
            'texts': ['Test Page Text'],
        },
    ]
