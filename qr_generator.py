#!/usr/bin/env python

#    Copyright 2022 m-alorda
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from pathlib import Path
import shutil
import uuid
import io

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


PROJECT_DIR = Path(__file__).absolute().parent
OUTPUT_DIR = PROJECT_DIR / "QRs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

Color = tuple[int, int, int]


class QrGenerator:
    """Generates QR Codes"""

    def generate(
        self,
        content: str,
        output_file: Path | None = None,
        embedded_image_path: Path | None = None,
        radius: float = 0.5,
        background_color_rgb: Color = (255, 255, 255),
        center_color_rgb: Color = (0, 0, 0),
        edge_color_rgb: Color = (0, 0, 0),
    ) -> Path:
        """Generate a QR code"""
        if output_file is None:
            output_file = OUTPUT_DIR / f"{uuid.uuid4()}.png"
        qr = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_H)
        qr.add_data(content)
        qr.make()
        image = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(radius),
            color_mask=RadialGradiantColorMask(
                background_color_rgb,
                center_color_rgb,
                edge_color_rgb,
            ),
            embeded_image_path=embedded_image_path,
        )
        image.save(output_file)
        return output_file

    def generate_as_ascii(
        self,
        content: str,
    ) -> str:
        """Generates QRs as ASCII text"""
        result = io.StringIO()
        qr = qrcode.QRCode()
        qr.add_data(content)
        qr.print_ascii(result)
        result.seek(0)
        return result.read()

    def generate_recursive(
        self,
        content: str,
        depth: int = 1,
        output_file: Path | None = None,
        radius: float = 0.5,
        background_color_rgb: Color = (255, 255, 255),
        center_color_rgb: Color = (0, 0, 0),
        edge_color_rgb: Color = (0, 0, 0),
    ) -> Path:
        """Generates a nested QR code"""
        if depth < 0:
            raise ValueError(f"Depth cannot be less than 0: {depth}")

        result = self.generate(content)
        for _ in range(depth):
            previous = result
            result = self.generate(
                content,
                embedded_image_path=previous,
                radius=radius,
                background_color_rgb=background_color_rgb,
                center_color_rgb=center_color_rgb,
                edge_color_rgb=edge_color_rgb,
            )
            previous.unlink(missing_ok=True)

        if output_file is not None:
            result = result.rename(output_file)

        return result

    def clean(self) -> None:
        """Removes all unnamed generated QRs"""
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)


if __name__ == "__main__":
    import fire

    fire.Fire(QrGenerator)
