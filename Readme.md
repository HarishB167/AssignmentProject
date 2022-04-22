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
_domain_/store/categories<br/>
API to get subcategories for a category<br/>
_domain_/store/subcategories/?category*id=\_id*<br/>
API to get all products for a category<br/>
_domain_/store/products/?category=_id_
API to get all products for a subcategory<br/>
_domain_/store/products/?subcategory*id=\_id*
API to post new product under existing subcategory and category<br/>
Post request at :<br/>
_domain_/store/products/<br/>
