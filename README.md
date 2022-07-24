# QR Generator

This project is a CLI wrapper of [qrcode][qrcode-pypi].

## Usage

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

Generate as ASCII

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

[qrcode-pypi]: https://pypi.org/project/qrcode/
