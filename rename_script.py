
import os
import re
import argparse

def rename_files(working_path=".", extension="mp3"):
  """
  Renames files in a folder, normalizing to lowercase, 
  removing the weekday name, and handling different file extensions.

  Args:
    working_path: The path to the folder containing the files. 
                   Defaults to the current directory if not provided.
    extension: The file extension to process (e.g., "mp3", "csv", "txt"). 
               Defaults to "mp3".
  """
  for filename in os.listdir(working_path):
    if filename.lower().endswith(f".{extension}"):  # Case-insensitive check for extension
      

      # Use regular expression to remove the weekday and surrounding underscores
      new_filename = re.sub(r".*(lunes|martes|miércoles|jueves|viernes|sábado|domingo)_?", "", filename, flags=re.IGNORECASE)
      
      old_filepath = os.path.join(working_path, filename)
      new_filepath = os.path.join(working_path, new_filename)
      
      os.rename(old_filepath, new_filepath)
      print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Rename files in a folder.")
  parser.add_argument(
      "working_path", 
      nargs="?",  # Make the argument optional
      default=".",  # Default to current directory
      help="Path to the folder containing the files"
  )
  parser.add_argument(
      "-e", "--extension", 
      default="mp3", 
      help="File extension to process (e.g., mp3, csv, txt)"
  )
  args = parser.parse_args()
  rename_files(args.working_path, args.extension)

