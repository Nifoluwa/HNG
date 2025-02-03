This project is written as a submission for the HNG backend internship track.
See <https://hng.tech/internship> for more information about the internship and <https://hng.tech/hire/python-developers>
for more about the stack used to develop this API

All code is written in python using the FastAPI framework and the requirements are specified in the requirements.txt file.
To set up and run locally, install a python version >= 3.10 or greater and in terminal enter:
---"pip install -r requirements.txt".
----Next run the main.py file
The endpoints should run locally.
The API is made publicly accessible/deployed from Github using Railway.app (Documentation here: <https://docs.railway.com>)

TASK 0:
The endpoints are: <https://hng-production-4aa2.up.railway.app/> for an intro page and
                  <https://hng-production-4aa2.up.railway.app/result> as the API with the answers to the task.
Request Format:
import requests
r = requests.get(url = "any of the endpoints above")
print(r.json())

Response Format:
{  "Email":"Response E_mail",
"Current_datetime": datetime in ISO 8601 format
"GitHub_URL": A link to this repository.
}

TASK 1:
The endpoints are: <https://hng-production-4aa2.up.railway.app/> for an intro page and
                  <https://hng-production-4aa2.up.railway.app/api/classify-number?number=*> as the API with the answers task one.

Tests have also been written(to the best of my knowledge) to ensure the API meets the task requirements.
Thank you.
