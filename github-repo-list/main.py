import requests

username = input("Masukan username github: ")
response = requests.get("https://api.github.com/users/"+username+"/repos")
myProject = response.json()

for project in myProject:
    print(f"Project Name: {project['name']}\n Project URL: {project['html_url']}\n")