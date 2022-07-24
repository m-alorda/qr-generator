from pathlib import Path

from qr_generator import QrGenerator

EXAMPLE_DIR = Path(__file__).absolute().parent

QrGenerator().generate(
    "https://github.com/m-alorda",
    embedded_image_path=EXAMPLE_DIR / "github-logo.png",
    output_file=EXAMPLE_DIR / "github-qr.png",
    radius=0.7,
    center_color_rgb=(247, 181, 2),
)
