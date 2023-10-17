This is a README for Command line for the win project

Requirements
General
A README.md file, at the root of the folder of the project, is mandatory
This project will be manually reviewed.
As each task is completed, the name of that task will turn green
Create a screenshot, showing that you completed the required levels
Push this screenshot with the right name to GitHub, in either the PNG or JPEG format
Specific
In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

References :

SFTP Guide
SFTP File Transfer Tutorial
Here are the steps to follow:

Take the screenshots of the completed levels as mentioned in the general requirements.
Open a terminal or command prompt on your local machine.
Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the hostname, username, and password provided to you for the sandbox environment.
Once connected, navigate to the directory where you want to upload the screenshots.
Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.
Make sure to include the steps you followed to use the SFTP command-line tool in your project’s README.md file. This will help the reviewers understand how you performed the file transfer using SFTP.
NOTE :
The screenshoots of completed level should be inside the dir /root/alx-system_engineering-devops/command_line_for_the_win/


PROCESS

1. I opened command prompt and copied the SFTP address of my sandbox  using and pasted it into the terminal
2. I then proceeded to enter my password 
3. After logging in, I went into /root/alx-system_engineering-devops/ directory and created the directory named command_line_for_the_win.
This was all achieved with the "cd" and "mkdir" commands.
4. I went insied the command_line_for_the_win directory to upload my screenshots.
5. I used the "lls" command to list the directories and on my local computer.
6. I used the "lcd" command to enter the directory that contained the screenshots.
7. I then proceeded to use the "put" command with the file names to upload the screenshots to the SFTP sever.

These are the steps that I took to upload the screenshots.

Thank you.
