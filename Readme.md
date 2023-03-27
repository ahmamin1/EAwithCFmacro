#Easy-Attend Codeforces
This Python script uses the Codeforces API to generate a report of solved problems for a given contest, and then merges that report with an attendance list to create a final report with Easy-Attend IDs.

The script reads configuration data from a `config.json` file, which includes the Codeforces group ID, contest ID, page number, and Easy-Attend session ID. It then calls the Codeforces API to retrieve a JSON object with data on the contestants and their solved problems. The script calculate the number of problems solved by each contestant, and writes the results to a CSV file named `output.csv`.

The script then reads the `dataset.csv` file, which contains a list of attendees with their Easy-Attend IDs, and merges it with the `output.csv` file to create a final report with Easy-Attend IDs. The resulting report is written to a file named `report.csv`.

Finally, the script calls the `attMacro` to run a macro that marks the attendees as attended in the Easy-Attend system, using the provided session ID.

To use this script, simply modify the `config.json` file to match your contest and Easy-Attend session and credentials, and then run the script using `Python 3.x.` The script requires the `requests`, `csv`, `json`, `math`, `pandas` modules.

This script is useful for anyone who needs to manage attendance for Codeforces contests using the Easy-Attend system, and wants to automate the process of marking attendees as attended. The script is open-source and can be customized and extended to meet the specific needs of different users and organizations.

##Requirements
1. Python 3.x
2. Requests
3. CSV
4. JSON
5. Math
6. Pandas

##installation of Requirements
- Python 3.x is a programming language and can be downloaded from the official website: https://www.python.org/downloads/. Select the appropriate version for your operating system and follow the installation instructions.

For the following modules, you can use pip, which is a package installer for Python:

- Requests: open a command prompt or terminal and enter the command `pip install requests`.
- CSV: this is a built-in module in Python and doesn't require installation.
- JSON: this is a built-in module in Python and doesn't require installation.
- Math: this is a built-in module in Python and doesn't require installation.
- Pandas: open a command prompt or terminal and enter the command `pip install pandas`.

Make sure to use a version of pip that corresponds to the version of Python you have installed.
You can check the version of Python you have by entering `python --version` in the command prompt or terminal.

##Usage
- Modify config.json to match your contest and Easy-Attend session
- Run the script using python CF-EA.py
- Wait for the script to generate the report.csv file and attendance macro will run automaticly 
##Contributing
Contributions are welcome! If you have any ideas or suggestions for improving this script, please submit an issue or a pull request.

