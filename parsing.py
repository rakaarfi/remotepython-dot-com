from bs4 import BeautifulSoup as bs
from requesting import Requesting

class Parsing():
  def __init__(self):
    self.requester = Requesting()

  def get_soup(self, url):
    # Get the page content from the URL
    page_content = self.requester.get_response(url)

    if page_content:
      return bs(page_content, 'html.parser')
    else:
      print("No content.")

  # Get Title, Company-Name and Date
  def get_content(self, url):
    soup = self.get_soup(url)
    if soup:
      # Find all tags containing the specified content
      articles = soup.find_all('div', class_='item')

      info = []
      id = []
      for i in articles:

        # Get Title
        title_tag = i.find('a')
        title = title_tag.get_text(strip=True) if title_tag else "No title found."

        # Get Company-Name
        company_tag = i.find('span', class_='color-black')
        company = company_tag.get_text(strip=True) if company_tag else "No company found."

        # Get Date
        span_tags = i.find_all('span', class_='color-white-mute')
        date = None
        for span in span_tags:
          text = span.get_text(strip=True)
          # Only extract text that starts with "Posted"
          if text.startswith("Posted"): 
            # Extract the date by deleting the "Posted: "
            date = text.replace("Posted: ", "")
        if not date:
          date = "No date found."

        # Get links to get Desired-Skills
        baseurl = 'https://www.remotepython.com'
        link = i.find('a').get('href')
        complete_link = baseurl + link
        des_skills = self.get_desired_skills(complete_link)

        # ID to get unique ID
        unique_id = link.split('/')[-2]
        
        # Store all data in dictionary
        data = {
          "Job-Title": title,
          "Company-Name": company,
          "Date-Posted": date,
          "Desired-Skills": des_skills,
        }
        info.append(data)
        id.append(unique_id)
      return info, id

  def get_desired_skills(self, url):
    soup = self.get_soup(url)
    if soup:
      # Find the exact tag with "Desired Skills" text
      des_skills_header = soup.find('h3', string="Desired Skills")

      if des_skills_header:

        # Find all desired skills
        des_skills_tag = des_skills_header.find_next('ul').find_all('li')
        des_skills = [i.get_text(strip=True) for i in des_skills_tag]
        return des_skills

      else: # If there's no desired skill
        return f"No Desired Skills in {url}"
    else:
      print("No content.")


if __name__ == "__main__":
  url = "https://www.remotepython.com/jobs/"
  parsing = Parsing()

  info = parsing.get_content(url)
  print(info)
  # links = parsing.get_links(url)
  # all_des_skills = parsing.get_all_desired_skills(url)

  # link = "https://www.remotepython.com/jobs/72f042b6a6bb407a915bee48483b59be/"
  # des_skills = parsing.get_desired_skills(link)
  # print(des_skills)