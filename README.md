## PyInstaller Quickstart

Install PyInstaller from PyPI:

```shell
pip install pyinstaller
```

Go to your program’s directory and run:

```shell
pyinstaller yourprogram.py
```

This will generate the bundle in a subdirectory called dist.
Adding -F (or --onefile) parameter will pack everything into single "exe".

```shell
pyinstaller -F yourprogram.py
```

The --noconsole flag will disable a console opening when excuting the .exe

```shell
pyinstaller -F --noconsole yourprogram.py
```

Adding -F (or --onefile) parameter will pack everything into single "exe" and --noconsole will not show the terminal when running the exe.

```shell
pyinstaller -F --paths=<your_path>\Lib\site-packages yourprogram.py
```

running into "ImportError" you might consider side-packages.

```shell
pip install pynput==1.6.8
```

still runing in Import-Erorr - try to downgrade pyinstaller - see Getting error when using pynput with pyinstaller

For a more detailed walkthrough, see the manual.

https://pyinstaller.org/en/v4.1/usage.html
https://github.com/flatplanet/Tkinter.com-Youtube
https://projectgurukul.org/python-qr-code-generator/
https://ttkbootstrap.readthedocs.io/en/version-0.5/

## Activate venv

Creating:

```
python -m venv .venv
```

MacOs:

```
source .venv/bin/activate
```

Windows:

```
.venv\Scripts\activate
```

## Pip-tools:

https://github.com/jazzband/pip-tools/?tab=readme-ov-file

python -m pip install pip-tools

to generate requirements.txt use:

```shell
pip-compile requirements.in
```

To update the requirements.txt

```shell
pip-compile --upgrade
```

to install dependencies use:

```shell
pip-sync
```

or

```shell
pip install -r requirements.txt
```
