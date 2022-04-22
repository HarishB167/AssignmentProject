## INTRODUCTION

This is a backend for project for the Assignment Project.<br/>
for frontend part see : https://github.com/HarishB167/AssignmentProjectFrontend

Requirements are mentioned in Pipfile

## Configuration

At root folder .env file is required with following key-values<br/>
SECRET_KEY = '<secret-key>'

## Installation

Following command will install dependencies from Pipfile.<br/>
pipenv install

## Running

python manage.py runserver

## Api endpoints overview

API to get all categories<br/>
**domain**/store/categories<br/><br/>

API to get subcategories for a category<br/>
**domain**/store/subcategories/?category_id=**id**<br/><br/>

API to get all products for a category<br/>
**domain**/store/products/?category_id=**id**<br/><br/>

API to get all products for a subcategory<br/>
**domain**/store/products/?subcategory_id=**id**<br/><br/>

API to post new product under existing subcategory and category<br/>
Post request at :<br/>
**domain**/store/products/<br/>
