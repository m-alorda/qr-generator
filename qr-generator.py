#!/usr/bin/env python

from pathlib import Path
import uuid

import qrcode


PROJECT_DIR = Path(__file__).absolute().parent


class QrGenerator:
    """Generates QR Codes"""

    def generate(self, content: str, output_file: Path | None = None) -> Path:
        """Generate a qr code"""
        if output_file is None:
            output_file = PROJECT_DIR / f"{uuid.uuid4()}.png"
        qr = qrcode.QRCode()
        qr.add_data(content)
        qr.make()
        image = qr.make_image()
        image.save(output_file)
        return output_file


if __name__ == "__main__":
    import fire

    fire.Fire(QrGenerator)
