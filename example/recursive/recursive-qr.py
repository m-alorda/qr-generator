from pathlib import Path

from qr_generator import QrGenerator

EXAMPLE_DIR = Path(__file__).absolute().parent

QrGenerator().generate_recursive(
    "https://github.com/m-alorda/qr-generator",
    depth=2,
    output_file=EXAMPLE_DIR / "recursive-qr.png",
    edge_color_rgb=(0, 0, 255),
)
