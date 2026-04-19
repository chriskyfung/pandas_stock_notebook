# Project Overview

This project provides a set of tools and examples for querying and analyzing Hong Kong stock data using Python. It primarily uses a Jupyter Notebook (`pandas_hkstock_datareader.ipynb`) as the main interface for data exploration and visualization. The core logic is encapsulated in the `stocks.py` file, which defines a `stock_profile` class for managing stock data.

The project leverages several key libraries:
-   **Pandas:** For data manipulation and analysis.
-   **yfinance:** To fetch financial data from Yahoo Finance.
-   **Jupyter Notebook:** For interactive data analysis and visualization.

## Building and Running

### 1. Environment Setup

It is recommended to use a Python virtual environment to manage dependencies.

### 2. Install Dependencies

Install the required Python packages using pip:

```shell
pip install -r requirements.txt
```

### 3. Running the Project

There are two main ways to use this project:

#### a) Jupyter Notebook

The `pandas_hkstock_datareader.ipynb` notebook provides a complete, interactive walkthrough of the project's functionality. It covers:
-   Loading stock profiles from `stocks.json`.
-   Fetching historical data from Yahoo Finance.
-   Displaying and analyzing the data using Pandas.

To run the notebook, start the Jupyter Notebook server:

```shell
jupyter notebook
```

Then, open the `pandas_hkstock_datareader.ipynb` file in your browser.

#### b) Python Script

The `stocks.py` file contains the `stock_profile` class, which can be imported and used in other Python scripts. The `README.md` provides a basic usage example.

## Development Conventions

-   **Stock-List:** The list of stocks to be analyzed is defined in `stocks.json`. This file contains a mapping of stock tickers to their names.
-   **Core-Logic:** The main logic for fetching and managing stock data is encapsulated in the `stock_profile` class in `stocks.py`.
-   **Notebook:** The Jupyter Notebook should be used for demonstration and interactive analysis, while the core reusable logic should be kept in `.py` files.

## Agent Development Notes

During the project refresh, several challenges were encountered, particularly when dealing with Jupyter Notebook (`.ipynb`) files and shell command execution within the agent environment. These notes serve as a guide for future development or troubleshooting.

### 1. Modifying Jupyter Notebooks (`.ipynb` files)

*   **Problem:** Directly modifying `.ipynb` files (which are JSON documents) using string `replace` operations is highly prone to errors due to sensitive JSON escaping rules. Backslashes (``) and double quotes (`"`) within code strings in the notebook's `source` arrays must be correctly escaped for JSON syntax. A single incorrect escape can corrupt the entire file, leading to "Bad control character in string literal in JSON" errors.
*   **Recommendation:** When making non-trivial changes to `.ipynb` files, prefer a programmatic approach:
    1.  Read the `.ipynb` file as a plain text string.
    2.  Parse the string into a Python (or equivalent language) JSON object using `json.loads()`.
    3.  Manipulate the Python object (e.g., modify `cell['source']` arrays, clear `cell['outputs']`).
    4.  Dump the modified Python object back into a JSON string using `json.dumps()` (which handles all escaping automatically).
    5.  Write the resulting JSON string back to the `.ipynb` file.
    *   **Caveat:** Ensure that Python code strings assigned to `cell['source']` arrays are themselves correctly Python-escaped for any internal backslashes or quotes.

### 2. Executing Shell Commands with Paths Containing Spaces

*   **Problem:** When using `run_shell_command` with paths or arguments that contain spaces (e.g., `C:\Users\ky fung\...\python.exe`), PowerShell's parsing can lead to `ParserError: UnexpectedToken` even if the primary executable path is quoted.
*   **Recommendation:**
    *   Always enclose paths and arguments containing spaces in double quotes.
    *   If a `ParserError` persists, try using relative paths for scripts/files when executing from a known `dir_path`.
    *   Consider copying temporary scripts to a path without spaces (e.g., project root) before execution, or pass the Python script content directly via `python -c "..."` if feasible for simple scripts.

### 3. Shell Commands within Jupyter Notebook Cells

*   **Problem:** Jupyter Notebook cells often contain shell commands (`!command`) where internal quoting (e.g., `!"$(pwd)"`) can conflict with the JSON structure of the `.ipynb` file itself if not correctly escaped. This led to persistent JSON parsing errors.
*   **Recommendation:** When correcting `.ipynb` files programmatically, pay extra attention to shell commands embedded in `source` fields. Any double quotes within these shell commands must be escaped for the JSON string, and potentially for the shell environment itself depending on the command. For example, `$(pwd)` in a shell command string needs to become `"$(pwd)"` in the Python string literal that goes into the JSON `source` array. This is a common source of "Bad control character" errors.
