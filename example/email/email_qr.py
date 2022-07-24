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

import urllib.parse
from pathlib import Path

from qr_generator import QrGenerator

EXAMPLE_DIR = Path(__file__).absolute().parent

MAIL_BODY = urllib.parse.quote(
    """Hi!

You are receiving this email from a QR code generated by <https://github.com/m-alorda/qr-generator>
"""
)
MAIL_SUBJECT = urllib.parse.quote("Hi from the generated QR")
MAIL_DEST = "miguel.alorda.cantero@gmail.com"
URI = f"mailto:{MAIL_DEST}?subject={MAIL_SUBJECT}&body={MAIL_BODY}"

QrGenerator().generate(
    URI,
    output_file=EXAMPLE_DIR / "email-qr.png",
    embedded_image_path=EXAMPLE_DIR / "email-icon.png",
    edge_color_rgb=(18, 21, 112),
)