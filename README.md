# PyAutoGUI for SAP Automation

The tasks of login into a SAP server, running a certain TCODE, and logging out are all automated by this project. The PyAutoGUI package is used to replicate mouse and keyboard movements.

## Dependencies

- Python 3
- PyAutoGUI

## How it functions

The script proceeds as follows:

1. Starts the SAP Logon program.
2. Acquires a SAP server login.
3. Enters the user's SAP login information.
4. Types the TCODE "ZRS_SP_PERFORM".
5. carries out the TCODE.
6. Closes the SAP Logon application and logs off of the SAP server.

The script reports errors and force-closes the SAP Logon application if there are any during the procedure.

## Logging

Every step of the procedure, including any problems, is recorded by the script in a text file.  The log file is located at `D:\Robot\09_Log\`.

## Environment Variables

The script uses the following environment variables for the SAP credentials:

- `SAP_USERNAME`: The user's SAP username.
- `SAP_PASSWORD`: The user's SAP password.

## Usage

To run the script, simply execute the `robot.py` file:

```bash
python robot.py
