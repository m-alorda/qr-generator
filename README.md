# QR Generator

This project is a CLI wrapper of [qrcode][qrcode-pypi].

## Usage

### Generate an QR with an image

```console
$  ./qr_generator.py generate https://www.linkedin.com/in/miguel-alorda/ \
    --embedded_image_path ./example/with-icon/linkedin-logo.png \
    --radius 0.2 \
    --center_color_rgb [66,135,245]
```

![QR with LinkedIn logo](example/with-icon/linkedin-qr.png)

```console
$ ./qr_generator.py generate "https://github.com/m-alorda" \
    --embedded_image_path ./example/with-icon/github-logo.png \
    --radius 0.7 \
    --center_color_rgb [247,181,2]
```

![QR with GitHub logo](example/with-icon/github-qr.png)

### Generate as ASCII

```console
$ ./qr_generator.py generate_as_ascii https://github.com/m-alorda/qr-generator

    █▀▀▀▀▀█ ▀   ▄██▀▀▀▀▄  █▀▀▀▀▀█
    █ ███ █ ▄▀▄▀▄▄█▄▀▀▄   █ ███ █
    █ ▀▀▀ █ █▀▀█▄█ ▀██▀▄  █ ▀▀▀ █
    ▀▀▀▀▀▀▀ █ █ █ ▀▄▀▄█ █ ▀▀▀▀▀▀▀
    ▀  ▄█ ▀▀▀▀▄█▄ ▄▄▄▀  ██████▄▄█
    ▄█  █▀▀▄▄▀▄▀ ▀█▀▀▄  █ ██▄▄ ▄█
    ▀▄██▀▀▀▄▀▀▄ █▄ █▄▀▄ ▀▀▄▄▄▄▄█▄
    █▀▄█▄█▀▀▀▄▄▄ ▀ █ █▀▄██▀▀ ▀▀▄█
    ▄▄ ▄▀▀▀█▄ ▄██▀█▄▄▀▄ █ ▄█▄▄ █▄
      ▀█▄▄▀█   ▀▀█▀▀ █▄ █▄ ▄▄ ▀▄█
    ▀▀▀ ▀ ▀▀█▀█▄ █▄▄▄██▄█▀▀▀█▀  █
    █▀▀▀▀▀█ ▀ ▄ █ ▄█ ▄███ ▀ █▀▀▄█
    █ ███ █ ▀ █▄██▀█ ▀ ▀▀█▀▀▀▀  █
    █ ▀▀▀ █  ▀▄ █▄█▀██▄▀██▄ ▄█▀██
    ▀▀▀▀▀▀▀ ▀▀ ▀▀▀  ▀▀  ▀▀▀▀▀▀ ▀
```

### CLI options

```console
$ ./qr_generator.py generate --help
NAME
    qr_generator.py generate - Generate a QR code

SYNOPSIS
    qr_generator.py generate CONTENT <flags>

DESCRIPTION
    Generate a QR code

POSITIONAL ARGUMENTS
    CONTENT
        Type: str

FLAGS
    --output_file=OUTPUT_FILE
        Type: Optional[pathlib.Path | None]
        Default: None
    --embedded_image_path=EMBEDDED_IMAGE_PATH
        Type: Optional[pathlib.Path | None]
        Default: None
    --radius=RADIUS
        Type: float
        Default: 0.5
    --background_color_rgb=BACKGROUND_COLOR_RGB
        Type: tuple
        Default: (255, 255, 255)
    --center_color_rgb=CENTER_COLOR_RGB
        Type: tuple
        Default: (0, 0, 0)
    --edge_color_rgb=EDGE_COLOR_RGB
        Type: tuple
        Default: (0, 0, 0)

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

[qrcode-pypi]: https://pypi.org/project/qrcode/
