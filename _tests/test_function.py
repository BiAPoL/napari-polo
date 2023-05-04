import numpy as np
from skimage.io import imread
from pathlib import Path

ROOT_DIR = Path(__file__).parent


def test_generate_clean_orientation_image():
    image = imread(ROOT_DIR / "liver_example.tif")
    from napari_polo import generate_clean_orientation_image
    result = generate_clean_orientation_image(image)
    expected = imread(ROOT_DIR / "liver_example_cleaned.tif")
    assert np.allclose(result, expected, atol=0.001)
