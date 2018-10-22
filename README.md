# Product Development Hiring Project

## Problem

Since BriteCore was created to work mostly with property-based insurance, the data model is pretty rigid. The data model assumes that all risks are properties and have addresses. This makes it difficult for BriteCore to work with different forms of insurance like Automobile Policies, Cyber Liability Coverage (protection against hacking), or Prize Insurance (if someone gets a $1 million hole-in-one prize at a golf tournament, the golf course doesn't pay it, they have an insurance policy to cover them).

## Primary Goal

In a github repo, we would like to see you come up with a solution that allows insurers to define their own custom data model for their risks. There should be no database tables called `automobiles`, `houses`, or `prizes`. Instead, insurers should be able to create their own risk types and attach as many different fields as they would like.

Fields are bits of data like first name, age, zip code, model, serial number, Coverage A limit, or prize dollar amount. Basically any data the carrier would want to collect about the risk. Fields can also be of different types, like text, date, number, currency, and so forth.

## Approach
MY approach to a solution for this problem would be to build a UI that will allow users to create their own risks of whatever type the desire.  Along with as many fields of type text, number, date, or enum (for choices) that they need to define the risk type.  I will store all of this in a database with this model: https://app.quickdatabasediagrams.com/#/d/Tobph1.  The backend API will be built in django using djangos rest framework along with class based views.  The front end will utilize bootstrap and Vue.js.  I will deploy the application to AWS lambda and zappa.

### Data

For the data layer, model the risk types and how the generic fields and field types would relate to these risk types. Field types should be either `text`, `number`, `date`, or `enum` (where there are multiple potential options but only one choice can be made).

### Backend

For the backend, create two API endpoints. One that returns a single risk type and one that returns a list of all risk types. Include all of the risk types' fields, field types, and any other data about the fields. This is your chance to show that you know how to create clean REST APIs.


### Frontend

The frontend is all about collecting information as it relates to these generic models. Create a single page that hits your risk type API endpoint(s) and displays all of the fields to the user in a form. Be sure to display at least one field of each type on the page. Don't worry about submitting the form.

Fields should use appropriate widgets based on their type. `text` fields should display as text boxes, `date` fields should use date pickers, and so on.


### Usage / Documentation

This web app contains two main API endpoints of detail and list views for the risk types in the database.  All risks will be listed at the bottom of the page to show the current risks in the database.  If you wish to create a new risk to add then simply name the risk type in the risk type input field and add field if you wish to add more data types to the risk.  Once finished creating the risk type along with any fields hit the Create Risk button and it will be added to the database.

To use the deployed application navigate to https://xaf3dqdcrg.execute-api.us-east-1.amazonaws.com/aws.  Currently POST requests are not working.  But to check out the sweet code and use the full functionality play around with the project in your local dev environment.

## Build Setup

First clone the project to your local environment, and set up a virtual environment.
``` bash
git clone https://github.com/JoeAlexBV/Product_development_project.git

cd Product_development_project

virtualenv env

# Activate the virtual environment (this is how to in Windows)
source env/Scripts/activate
```
Then install the requirements with: 
``` bash
pip install -r requirements.txt
```
Then install the frontend dependencies:

``` bash
# install dependencies
npm install
```
Navigate to the backend directory where manage.py is located and run:
``` bash
# Create a local sqlite3 database
python manage.py migrate
python manage.py makemigrations
# Run localhost development server
python manage.py runserver
```
In another terminal we will serve the frontend.  Navigate to the root directory of the project and run:

``` bash
# serve with hot reload at localhost:8080
npm run dev
```

Navigate in your desired browser to your localhost:8080 and enjoy the app!


