import pytest

from pptx import Presentation
from pathlib import Path


@pytest.fixture
def pptx_assets_dir() -> Path:
    return Path(__file__).parent / Path('assets')


@pytest.fixture
def fx_simple_pptx(pptx_assets_dir: Path) -> Presentation:
    return Presentation(pptx_assets_dir / 'simple.pptx')
