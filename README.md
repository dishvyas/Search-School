# Search-School
Simple backend to search sort and filter schools using Django and REST API

I have used Django for my backend with REST API to develop the API interface. No additional modules are imported for this simple backend app.

Install Django and Django REST framework libraries which are the only required modules for this app by : 
pip install django 
pip install djangorestframework

I have converted the Bangalore_school.csv file from this repo link https://github.com/openbangalore/bangalore/blob/master/bangalore/Education/Bangalore_schools.csv and converted into JSON file. You can find new JSON file already present at the path /school/api. I have created a parser.py file which converts CSV to JSON and prints the data in JSON file. You can run and check the process by running the file with "python parser.py".

I have added sorting and searching filters which are provided by the REST Framework i.e. SearchFilter and OrderingFilter to search and order schools according to a specific set of fields as mentioned in the code in /school/api/views.py. You can create the appropriate frontend html to render and display the results by creating suitable buttons/tabs to see search and sort changes.

To run the app, use the command : 
python manage.py runserver
