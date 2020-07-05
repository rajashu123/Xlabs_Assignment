# Xlabs_Assignment

## Brief Description:
The tests has been written in pytest framework. There are two testcases. 
1) test_charctersListWithDescription : This method will output a tuple with values of character's name, descriptions and the series in which they are present when the description is not empty.
2) test_storiesWithoutCharacterDescription :  This method will output a tuple containing character's name , stories when the description of characters is empty.

## Approach:
The common functions has been written in Helper file, like triggering an http request, getting content from a json , logger etc. I am using allure framework for report generation, rather than conventional pytest reporting library.

## Intallation for allure:
- pip install pytest-allure
- install node js
- npm install -g allure-commandline --save-dev

## Running the test:
- pytest --alluredir Reports test_ValidateGetRequest.py
  Above step will generate json file in Reports directory
- allure serve Reports

Above step will convert the json file into a beautiful html report and will launch that html page as well automatically.




