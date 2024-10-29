import requests

class Requesting:
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
  
  def __init__(self):
    self.session = requests.Session()

  def get_response(self, url):
    self.url = url
    self.request = self.session.get(url, headers=Requesting.headers)
    try:
      if self.request.status_code == 200:
        return self.request.text
      else:
        return f"Request failed with status code: {self.request.status_code}"
    except Exception as e:
      print(f"{e} - Failed to get response from {self.url}")
      return None