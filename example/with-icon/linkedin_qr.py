from pathlib import Path

from qr_generator import QrGenerator

EXAMPLE_DIR = Path(__file__).absolute().parent

QrGenerator().generate(
    "https://www.linkedin.com/in/miguel-alorda/",
    embedded_image_path=EXAMPLE_DIR / "linkedin-logo.png",
    output_file=EXAMPLE_DIR / "linkedin-qr.png",
    radius=0.2,
    center_color_rgb=(66, 135, 245),
)
