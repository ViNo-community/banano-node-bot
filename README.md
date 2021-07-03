## Download

Make a new directory where you want to install and run the bot, and download all files to that directory. 

## Install Dependencies

Install Python if not already installed. Python 3.0 or above is recommended. 

Install the discord.py and dotenv Python packages with:

> $ pip install discord.py dotenv

## Configuration

To get the bot to run, you need to edit some configuration values in the .env file. 

Open the .env file in a text editor. The .env file holds your configuration data. The two variables that need to be set before the bot can be run are DISCORD_TOKEN and RPC_URL.

**IMPORTANT: The .env file should be private - it contains sensitive information that should not be visible to other people.**

If anyone has access to your DISCORD_TOKEN they'll be able to control the bot. .env file should have read and wite permissions for the owner only. If on Linux you can set the appropriate permissions with $chmod 600 .env 

Add your DISCORD_TOKEN to the placeholder. This is the special unique hexadecimal token that acts as a "key" to access your Discord bot. It is found on the [Discord Applications settings](https://discord.com/developers/applications) in the bot section. Select your bot and click where it says "Click to Reveal Token." Copy and paste this token to your .env file. Remember, do not tell anyone else your Discord token or else they'll be able to control your bot. 

Add the API endpoint url of your nano node to RPC_URL.

The other settings are optional. The COMMAND_PREFIX setting sets what prefix is used to give commands to the bot. The default is !. For example, if you set the COMMAND_PREFIX to n!, a user would type n!balance in the chat to see what the current account balance is. COMMAND_PREFIXs can be any length (including zero). The LOGGING_LEVEL setting sets the sensitivity of the logging. The lower the value the more information will be logged. For example, a value of 50 will only log severe errors, while a value of 0 will log everything. The default log level is 30, which will log only warnings and errors. A table description of log levels in Python is displayed below:


Log Level     | Numeric Value | Description
------------- | ------------- | -----------
CRITICAL      | 50            | A serious error, indicating that the program itself may be unable to continue running.
ERROR         | 40            | Due to a more serious problem, the software has not been able to perform some function.
WARNING       | 30            | Something unexpected happened, but the software is still working as expected.
INFO          | 20            | Confirmation that things are working as expected.
DEBUG         | 10            | Detailed information, typically of interest only when diagnosing problems.
NOTSET        | 0             | Log everything.

## Run

**IMPORTANT: For security reasons, do not run the bot as root.**
To run the bot

> $ python nano_node_bot.py. 

For security reasons, do not run the bot as root. It is recommended to add a bot as a service, which will allow you to have greater control over the execution. 

On Linux, you can do this by adding it as a service with systemd. A good guide for adding a Python script as a service on Linux is here:

For security reasons, do not run as root. It is recommended to create a new user specifically for running the bot. [Here is a straight-forward guide for adding a Python script as a service in systemd](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267)

You can also run the bot on Windows. To do this, [install NSSM (Non-Sucking Service Manager)](https://nssm.cc/) which is a Windows equivalent of systemd. [Here is a good guide for adding a Python script to NSSM.](https://www.devdungeon.com/content/run-python-script-windows-service)

## Notes

This project is a work in progress and settings and execution will most likely change in the future. This README will be updated to reflect these changes.
