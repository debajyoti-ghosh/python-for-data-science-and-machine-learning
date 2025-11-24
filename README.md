## How to Install VS Code

1. Go to the [Visual Studio Code download page](https://code.visualstudio.com/).
2. Choose your operating system (Windows, macOS, or Linux).
3. Download the installer and run it.
4. Follow the installation prompts.
5. Once installed, launch VS Code from your applications menu or desktop shortcut.

For more details, refer to the [official documentation](https://code.visualstudio.com/docs/setup/setup-overview).


## How to Check if Python is Installed

1. Open a terminal (Command Prompt, PowerShell, or Terminal).
2. Run the following command to check the installed Python version:
    ```
    python --version
    ```
    or
    ```
    python3 --version
    ```
3. If Python is installed, you will see the version number (e.g., `Python 3.10.5`).

If you see an error or no version is displayed, Python is not installed.

## How to Install Python

1. Go to the [official Python download page](https://www.python.org/downloads/).
2. Download the installer for your operating system.
3. Run the installer and follow the setup instructions.
    - On Windows, ensure you check **"Add Python to PATH"** during installation.
4. After installation, verify by running `python --version` or `python3 --version` in a new terminal.





## How to Create a Python Virtual Environment (.venv)

1. Open VS Code and launch a new terminal.
2. Navigate to your project directory using `cd path/to/your/project`.
3. Create a virtual environment using one of the following commands:

   - **Standard command** (default Python):
     ```
     python -m venv .venv
     ```

   - **OR, if you have multiple Python versions and want a specific one (e.g., 3.12.2):**
     
     - **Windows:**
       ```
       py -3.12.2 -m venv .venv
       ```

     - **macOS/Linux:**
       ```
       python3.12.2 -m venv .venv
       ```

4. Activate the virtual environment:
    - **Windows:**  
      ```
      .venv\Scripts\activate
      ```
    - **macOS/Linux:**  
      ```
      source .venv/bin/activate
      ```



5. Your terminal prompt should now indicate that the virtual environment is active.

For more information, see the [Python venv documentation](https://docs.python.org/3/library/venv.html).


## How to Install Python Libraries (e.g., pandas)

1. Ensure your virtual environment is activated.
2. Install the desired library using `pip`. For example, to install `pandas`, run:
    ```
    pip install pandas
    ```
3. You can install multiple libraries at once, e.g.:
    ```
    pip install pandas numpy matplotlib
    ```
4. To save your installed libraries to a requirements file:
    ```
    pip freeze > requirements.txt
    ```
5. To install libraries from a requirements file:
    ```
    pip install -r requirements.txt
    ```

For more details, see the [pip documentation](https://pip.pypa.io/en/stable/).