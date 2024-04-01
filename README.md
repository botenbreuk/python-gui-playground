PyInstaller Quickstart
Install PyInstaller from PyPI:

pip install pyinstaller
Go to your program’s directory and run:

pyinstaller yourprogram.py
This will generate the bundle in a subdirectory called dist.

pyinstaller -F yourprogram.py
Adding -F (or --onefile) parameter will pack everything into single "exe".

pyinstaller -F --noconsole yourprogram.py
Adding -F (or --onefile) parameter will pack everything into single "exe" and --noconsole will not show the terminal when running the exe.

pyinstaller -F --paths=<your_path>\Lib\site-packages yourprogram.py
running into "ImportError" you might consider side-packages.

pip install pynput==1.6.8
still runing in Import-Erorr - try to downgrade pyinstaller - see Getting error when using pynput with pyinstaller

For a more detailed walkthrough, see the manual.

https://pyinstaller.org/en/v4.1/usage.html
https://github.com/flatplanet/Tkinter.com-Youtube
https://projectgurukul.org/python-qr-code-generator/
https://ttkbootstrap.readthedocs.io/en/version-0.5/

Activate venv

Creating:

```
python -m venv venv
```

MacOs:

```
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```
