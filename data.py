import requests


api = "https://opentdb.com/api.php?amount=15&type=boolean"
questions = requests.get(url=api)
questions.raise_for_status()
question_data = questions.json()["results"]
