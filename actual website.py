from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation="
).text

soup = BeautifulSoup(html_text, "lxml")

jobs = soup.find("li", class_="clearfix job-bx wht-shd-bx")
company_name = jobs.find("h3", class_="joblist-comp-name").text.replace(" ", "")
skills = jobs.find("ul", class_="list-job-dtl clearfix").text.replace(" ", "")
print(
    f"""
Company Name:: {company_name.strip()}
Job Description:: {skills.strip()}
"""
)
