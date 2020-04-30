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
* [Overview](https://github.com/CoDev-20/Covid19Chatbot/#overview)
* [Objectives](https://github.com/CoDev-20/Covid19Chatbot/#objectives)
* [Scope and Limitations](https://github.com/CoDev-20/Covid19Chatbot/#scope-and-limitations)
* [User Stories (General User)](https://github.com/CoDev-20/Covid19Chatbot#user-stories-general-user)
* [User Stories (Administrator)](https://github.com/CoDev-20/Covid19Chatbot#user-stories-administrator)
* [Setup and Installation](https://github.com/CoDev-20/Covid19Chatbot/#setup-and-installation)
* [Running the program](https://github.com/CoDev-20/Covid19Chatbot/#running-the-program)
* [Sample Snapshots](https://github.com/CoDev-20/Covid19Chatbot/#sample-snapshots)
  * [Website Homepage](https://github.com/CoDev-20/Covid19Chatbot/#website-homepage)
  * [About us page](https://github.com/CoDev-20/Covid19Chatbot/#about-us-page)
  * [FAQs page](https://github.com/CoDev-20/Covid19Chatbot/#faqs-page)
  * [Chatbot page](https://github.com/CoDev-20/Covid19Chatbot/#chatbot-page)
  * [Chatbot Interactions](https://github.com/CoDev-20/Covid19Chatbot/#chatbot-interactions)
  * [Administrator Homepage](https://github.com/CoDev-20/Covid19Chatbot/#administrator-homepage)
  * [Accounts Database](https://github.com/CoDev-20/Covid19Chatbot/#accounts-database)
  * [Messages Database](https://github.com/CoDev-20/Covid19Chatbot/#messages-database)
  



 
## Overview
The outbreak of the novel coronavirus has sparked a health crisis that in turn has unleashed an unprecedented deployment of resources. The scientific and technology communities have put their full weight behind finding solutions that help mitigate the impact of the pandemic as it expands worldwide. CoDev-20 is an organization of students from MAPUA University. The developers created an Artifially Intelligent healthcare chatbot entitled CoDev-20 Chatbot that is designed to answer inquiries and questions from the user regarding the pandemic Corona Virus. The developers aim to provide reliable information and facts about the Corona Virus to lessen the falsification of information regarding the virus through an interactive chatbot that responds to the user’s queries. Individuals who suspect they might have the virus can conduct a physical self-assessment based on their symptoms while communicating with the bot, and depending on the result, they will receive instructions and advice about steps to take for treatment. This initiative aims to reduce call congestion for the regional coronavirus hotline and giving people an access to information that can help them during this crisis.
 
## Objectives
* To create a chatbot that responds to the queries of users about the Corona Virus.
* To provide a correct information regarding the virus
* To lessen the misconception about corona virus and avoid confusion to the people
* To fight corona virus with the aid of technology by providing people necessary information
 
## Scope and Limitations
The scope and limitation of the CoDev-20 Chatbot is that the bot is trained to answer queries limited to the topic regarding Corona Virus. The data gathered is based only in the Philippines in terms of total cases, recoveries, and deaths. It will not entertain other issues unrelated to Corona Virus.  
 
## User Stories (General User)
<b>Sign-up form</b>
* As a general user, I want to be able to register an account to access the website.

<b>Sign-in form</b>
* As a general user, I want to be able to login with my pre-existing account to use the features of the website.

<b>Website GUI</b>
* As a general user, I want the website’s features to be user-friendly and is pleasant to see so that it easy to learn and use.

<b>Website Main Page</b>
* As a general user, I want a brief introduction at the start to be able to understand what I could do to the website.

<b>Chat-bot Page</b>
* As a general user, I want to be able to access the chat-bot page so that I could interact with the chat-bot.

<b>Chat-bot</b>
* As a general user, I want the chat-bot to respond to my greetings and inquiries about the COVID19 situation and information.

<b>Chat-bot Voice Reading</b>
* As a general user, I want to be able to hear the information just in case a situation arise that I would use that feature.

<b>Voice-to-Chat Feature</b>
* As a general user, I want to be able to convert my spoken words to chat in case a situation arise that I would use such feature.

<b>About Us Page</b>
* As a general user, I want an in-depth information about the website such as who created the website so that I could easily access such necessary information.

<b>FAQs Page</b>
* As a general user, I want to be able to learn about the frequently asked questions so that I would know what the page is for or how to chat/use the chat-bot.

## User Stories (Administrator)
<b>View all and Edit Messages</b>
* As an admin, I want to view all the user's responses to our COVID bot and also have a complete access to the database of the messages.

<b>Sign in as admin</b>
* As an admin, I want to sign as an admin to manipulate the users and admins list.

<b>Sign up as admin</b>
* As an admin, I want to sign up another admin onto to the administrator homepage.

<b>CRUD (Create, Read, Update, Delete) Users list</b>
* As an admin, I want to create, read, update and delete the database of the users list.

<br>

---
 
<br>
 
## Setup and Installation
 
Setup a virtual environment like Anaconda or python venv. For this project, we used Anaconda Virtual Environment<br>
To create an environment, open Anaconda prompt and execute the command on the terminal.
```
conda create -n codev20 python=3.7
conda activate codev20
```
install the libraries for the project
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
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/2.PNG "Logo Title Text 1")
 
### FAQs page
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/3.PNG "Logo Title Text 1")
 
### Chatbot page
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/4.PNG "Logo Title Text 1")
 
### Chatbot interactions
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/5.PNG "Logo Title Text 1")
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/6.PNG "Logo Title Text 1")
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/7.PNG "Logo Title Text 1")
 
<br>
 
### Administrator Homepage
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/8.PNG "Logo Title Text 1")
 
<br>
 
### Accounts database
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/9.PNG "Logo Title Text 1")
 
<br>
 
### Messages Database
 
![alt text](https://github.com/CoDev-20/Covid19Chatbot/blob/master/images/10.PNG "Logo Title Text 1")
