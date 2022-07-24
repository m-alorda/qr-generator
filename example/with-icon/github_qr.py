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

try:
    from qr_generator import QrGenerator
except ModuleNotFoundError:
    print(
        "To run this example, install qr_generator locally, running from "
        "the root of the project `python -m pip install -e .`"
    )
    exit(1)

EXAMPLE_DIR = Path(__file__).absolute().parent

QrGenerator().generate(
    "https://github.com/m-alorda",
    embedded_image_path=EXAMPLE_DIR / "github-logo.png",
    output_file=EXAMPLE_DIR / "github-qr.png",
    radius=0.7,
    center_color_rgb=(247, 181, 2),
)
