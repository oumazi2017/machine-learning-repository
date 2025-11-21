# Machine Learning Repository

## Simple GUI Calculator App

A beautiful and functional calculator application built with Python and tkinter.

### Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Parentheses Support**: Use ( and ) for complex expressions
- **Modern Dark Theme**: Easy on the eyes with a sleek black/gray color scheme
- **Clear Display**: Large, readable numbers and operations
- **Additional Functions**:
  - **C** - Clear all
  - **⌫** - Backspace (delete last character)
  - **( )** - Parentheses for grouping operations
  - **.** - Decimal point

### Screenshots

![Calculator Interface](https://github.com/user-attachments/assets/dc3ed44b-8f93-4c13-88ce-148ad41c6ab1)

### Requirements

- Python 3.x
- tkinter (usually included with Python)

**On macOS (MacBook Pro):**
- Python from [python.org](https://www.python.org/downloads/) includes tkinter by default
- If using Homebrew Python: `brew install python-tk@3.12` (adjust version as needed)

**On Ubuntu/Debian systems:**
```bash
sudo apt-get install python3-tk
```

### Installation

1. Clone this repository:
```bash
git clone https://github.com/oumazi2017/machine-learning-repository.git
cd machine-learning-repository
```

2. Ensure tkinter is installed (see Requirements section above)

### Usage

**Run directly with Python:**
```bash
python3 calculator.py
```

### Troubleshooting (white background / missing button text)

If the app window shows a white background or the button labels are not visible (common on some macOS/Python/tkinter combinations), this repository includes an update that uses label-based clickable widgets for consistent coloring across platforms. To run the updated app:

```bash
python3 calculator.py
```

If you still see issues, ensure your Python installation includes Tcl/Tk (tkinter). On macOS, install Python from python.org or ensure `python-tk` is available for your distribution.

**On macOS, make it executable:**
```bash
chmod +x calculator.py
./calculator.py
```

**Create a macOS Desktop Application (.app bundle):**

To convert the calculator to a standalone desktop application on macOS, you can use `py2app`:

1. Install py2app:
```bash
pip3 install py2app
```

2. Create a setup file (`setup.py`) in the same directory:
```python
from setuptools import setup

APP = ['calculator.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app_icon.icns',  # Optional: add your own icon
    'plist': {
        'CFBundleName': 'Calculator',
        'CFBundleDisplayName': 'Simple Calculator',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```

3. Build the application:
```bash
python3 setup.py py2app
```

4. The `.app` file will be created in the `dist/` folder. You can:
   - Double-click `dist/Calculator.app` to run it
   - Drag it to your Applications folder
   - Add it to your Dock for quick access

**Alternative: Create an Automator App (Simple Method for macOS):**

1. Open **Automator** (found in Applications)
2. Choose **Application** as the document type
3. Search for "Run Shell Script" in the actions
4. Add this script:
```bash
cd /path/to/machine-learning-repository
/usr/local/bin/python3 calculator.py
```
5. Save as "Calculator.app" in your Applications folder

### How to Use

1. Click on number buttons (0-9) to enter numbers
2. Click on operator buttons (+, -, *, /) to select an operation
3. Use parentheses **( )** to group operations for complex expressions
4. Click **=** to calculate the result
5. Click **C** to clear the display
6. Click **⌫** to delete the last entered character
7. Click **.** to add a decimal point

### Examples

- **Simple Addition**: `5 + 3 = 8`
- **Multiplication**: `8 * 2 = 16`
- **Complex Expression**: `(10 + 5) * 2 = 30`
- **Decimal Numbers**: `3.14 * 2 = 6.28`
- **Nested Parentheses**: `((5 + 3) * 2) - 4 = 12`

### License

This project is open source and available for educational purposes.