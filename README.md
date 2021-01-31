## SPAM COMMENTS DETECTING SUB MODULE
This is sub module project for hate content filetring project (4th year research project)

### Prerequisites
![Python 3.7](https://img.shields.io/badge/Python-3.7-brightgreen.svg)
You must have Scikit Learn,numpy,nltk, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict spam comments absed on trainign data in 'commentData.csv' file.
2. app.py - This contains Flask APIs that receives comments details through GUI, computes the precited value based on our model and returns it.
3. templates - This folder contains the HTML template to allow user to enter "YOU TUBE VIDEO ID" and displays the predicted spam comments.

### Running the project

type python app.py for start your server 
then copy the given url and paste it in your browser
then input a youtube video id for getting ham comments
