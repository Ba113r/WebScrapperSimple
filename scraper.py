import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/" # Link to view
page = requests.get(URL) # Uses the Requests Library to get the HTML data from the Link

soup = BeautifulSoup(page.content, "html.parser") # Uses BeautifulSoup to turn the HTML data into readable data by Beautiful Soup

results = soup.find(id="ResultsContainer") # Finds the results container, this is where data we are concerned about is stored
job_elements = results.find_all("div", class_="card-content") # takes the results and finds all the job elemtns card content


python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()