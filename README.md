# Covid-19 Chatbot
### Covid-19 Chatbot is a project developed by team CoDev-20 from Mapua Univesity.
 
### Members
* Gian Karlo Madrid
* Ethan James Reyes
* John Rivera
* Rendell Sheen Suliva
* Clint Aldrin Valencia
* Rane Gillian Villanueva
 
### Instructor
* Engr. Dionis Padilla
 
<br><br>
_____
<br><br>
## Project Documentation
 
 
## Overview
The outbreak of the novel coronavirus has sparked a health crisis that in turn has unleashed an unprecedented deployment of resources. The scientific and technology communities have put their full weight behind finding solutions that help mitigate the impact of the pandemic as it expands worldwide. CoDev-20 is an organization of students from MAPUA University. The developers created an Artifially Intelligent healthcare chatbot entitled CoDev-20 Chatbot that is designed to answer inquiries and questions from the user regarding the pandemic Corona Virus. The developers aim to provide reliable information and facts about the Corona Virus to lessen the falsification of information regarding the virus through an interactive chatbot that responds to the user’s queries. Individuals who suspect they might have the virus can conduct a physical self-assessment based on their symptoms while communicating with the bot, and depending on the result, they will receive instructions and advice about steps to take for treatment. This initiative aims to reduce call congestion for the regional coronavirus hotline and giving people an access to information that can help them during this crisis.
 
## Objectives
* To create a chatbot that responds to the queries of users about the Corona Virus.
* To provide a correct information regarding the virus
* To lessen the misconception about corona virus and avoid confusion to the people
* To fight corona virus with the aid of technology by providing people necessary information
 
## Scope and Limitations
The scope and limitation of the CoDev-20 Chatbot is that the bot is trained to answer queries limited to the topic regarding Corona Virus. The data gathered is based only in the Philippines in terms of total cases, recoveries, and deaths. It will not entertain other issues unrelated to Corona Virus.  
 
<br>
 
---
 
<br>
 
## Setup and Installation
 
Setup a virtual environment like Anaconda or python venv. For this project, we used Anaconda Virtual Environment<br>
To create an environment, open Anaconda prompt and execute the command on the terminal.
```
conda create -n codev20
```
install all the dependencies and libraries for the project
```
pip install -r requirements.txt
```
Libraries will take time to download especially for the tensorflow.
 
<br>
 
---
 
<br>
 
## Running the program
 
To run the program on VS Code, navigate to the folder using the terminal then execute the command in conda terminal:
```
code .
```
Next is to make necessary migrations for the database.
 
```
python manage.py makemigrations
```
 
Then apply the migrations.
 
```
python manage.py migrate
```
We will then create a superuser or admin.
```
python manage.py createsuperuser
```
It will prompt for several details including username, email, and password.
<br><br>
Lastly, run the server.
 
```
python manage.py runserver
```
Open the URL using Google Chrome. Other browsers will hinder the voice functionality.
<br><br><br>
## Sample Snapshots
### Website Homepage
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/1.PNG "Logo Title Text 1")
 
 
### About us page
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/2.png "Logo Title Text 1")
 
### FAQs page
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/3.png "Logo Title Text 1")
 
### Chatbot page
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/4.png "Logo Title Text 1")
 
### Chatbot interactions
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/5.png "Logo Title Text 1")
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/6.png "Logo Title Text 1")
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/7.png "Logo Title Text 1")
 
<br>
 
### Administrator Homepage
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/8.png "Logo Title Text 1")
 
<br>
 
### Accounts database
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/9.png "Logo Title Text 1")
 
<br>
 
### Messages Database
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/10.png "Logo Title Text 1")
