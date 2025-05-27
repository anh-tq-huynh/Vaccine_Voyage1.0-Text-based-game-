# Introduction: Background information
This is a beginner's project, initiated during the studies in Metropolia University of Applied Science for 1st year IT students. In this project, the students are required to work in a group of 4, to build a text-based game using solely Python programming language. This project resulted in the creation of Vaccine Voyage.

As an RPG (role-playing game), Vaccine Voyage brings the player into a fictional world that is facing tremendous danger, under the effects of a deadly virus. It is spreading rapidly at a constant speed and posing a significant threat to people around the globe. The player will act as a devoted researcher who is on their journey towards different lands to find 7 (seven) ingredients for their vaccine formula.

There are 7 levels of the game, surpassing each level is equivalent to gaining 1 ingredient for the vaccine. In other words, by successfully passing 7 levels, the player shall win.

## Game's mechanism
- The game operates as a **country-guessing quiz**. There are seven levels, with each level representing a randomly assigned country.
- In each level, the player is given the 1st hint that points to the assigned country of that level. The higher level it is, the hints are more vague.
- The player can choose to see more hint with the cost of a number of points, depending on the level.

**To win:**
- The player must get all 7 countries correctly, while maintaining positive points

**The player will lose if:**
- The player's point become negative and the player's last guess is wrong

## See it in action
[See the video here](https://youtu.be/MhMVOYiMkyg)
[![Vaccine Voyage Gameplay Demo](https://github.com/user-attachments/assets/f22ec65c-2b9c-400c-8159-8390ac14f98b)](https://youtu.be/MhMVOYiMkyg)

## How to run
### Prerequisites
- **Database**: To run the backend, you will need
  - MariaDB or MySQL Server: Ensure you have a running instance of either MariaDB or MySQL on your local machine.
  - Database Client: Access to a command-line client (like mysql or mariadb) or a GUI tool (like DBeaver, MySQL Workbench, phpMyAdmin, etc.) to interact with your database server.
- **Python**: Make sure that you have Python installed, if not, you can install it from here [Python.org](https://www.python.org/downloads/)
- **Web browser**: Any modern browser, e.g Chrome, Firefox, Microsoft Edge, etc.
### Get started
#### Clone repository
1.Navigate to the folder into which you would like to save the repository
```bash
cd <your-path>
```
2. Clone the repository:
```bash
git clone https://github.com/anh-tq-huynh/Vaccine_Voyage1.0-Text-based-game-
```
#### Prepare for database
1. Log in to your database server
Open your terminal and enter the following command to log in to your database server
```bash
mysql -u root -p
#You will be asked to enter password
```
**Note:** If you use MariaDB, use the command ```mariadb -u root -p``` instead

2. Create database
```bash
CREATE DATABASE vaccine_voyage;
```
3. Select the database
```bash
USE vaccine_voyage
```
4. Create user
```bash
#Please keep 'newuser', 'password' as it is, no need to change. As this is a school project, security matter was not considered as top priority.
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password'
GRANT ALL PRIVILEGES ON vaccine_voyage.* TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
```
5. Clone the content of the game's database into the newly created vaccine_voyage
```bash
SOURCE <saved-repository-path>/Vaccine_Voyage1.0-Text-based-game-/vaccine_voyage.sql
```
**Note:** Sometimes the path may not work. If this happens, simply copy the vaccines_dumps.sql to the Download folder of your computer, then replace the command above with the new path. 

6. Exit from the database console
```bash
exit
```
#### Run the main game
1. Move to the main folder
```bash
cd <saved-repository-path>/Vaccine_Voyage1.0-Text-based-game-
```
2. Install required libraries
```bash
pip install mysql-connector-python
```
3. Run backend
```bash
python GameBody.py
```

### Acknowledgement
Teammates in building this project: 
- [Tamseela Mahmood](https://github.com/tamseelaa)
- [Taysa Abinader](https://github.com/TaysaAbinader)
- [Lan-Anh Tran](https://github.com/anhlt13)
- [Anh Huynh](https://github.com/anh-tq-huynh)
  
### Appendix
![image](https://github.com/user-attachments/assets/b22f3dc3-da71-433f-94b2-c4d0532baeb0)

_Flow chart_

![Database plane_Vaccine Voyage_TA, TM, AT, AH](https://github.com/user-attachments/assets/b4d5343d-7c51-452c-bbf7-5f2b1ac83c2b)

_Database structure_
