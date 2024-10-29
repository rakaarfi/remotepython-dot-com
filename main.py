from parsing import Parsing
from exporting import Exporting

def main():
  parsing = Parsing()
  url = "https://www.remotepython.com/jobs/"
  info, id = parsing.get_content(url)
  result = Exporting.create_dict(data=info, id=id)
  Exporting.append_to_csv(result)

if __name__ == "__main__":
  main()