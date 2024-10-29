import pandas as pd
from datetime import datetime
from parsing import Parsing

class Exporting:
    
  @staticmethod
  def create_dict(data, id):
    """Generate a dictionary with count, timestamp, and data."""
    generated_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create the dictionary
    result = {
      "Generated Time": generated_time,
      "Data": data,
      "ID": id
    }
    return result

  @staticmethod
  def append_to_csv(result, csv_file='result.csv'):
    """Append unique dictionary data to a CSV file."""
    # Create DataFrame
    new_df = pd.DataFrame(result)

    try:
      # Load existing data if the file exists
      existing_df = pd.read_csv(csv_file)
      # Combine existing and new data
      combined_df = pd.concat([existing_df, new_df], ignore_index=True)
      # Drop duplicates based on the 'ID' column
      combined_df = combined_df.drop_duplicates(subset='ID', keep='last')
    except FileNotFoundError:
      # If file does not exist, start with the new data
      combined_df = new_df

    # Save the combined DataFrame back to CSV
    combined_df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    url = "https://www.remotepython.com/jobs/"
    parsing = Parsing()

    info, id = parsing.get_content(url)
    result = Exporting.create_dict(data=info, id=id)
    Exporting.append_to_csv(result)
