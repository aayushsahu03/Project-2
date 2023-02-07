def validate_user(username:str, minlen):
    assert type(username) ==str, "value must be a string" 
    assert type(minlen) ==int, "value must be a string" 
    
    if minlen<1:
        raise ValueError("min len less than 1")
    if len(username)<minlen:
        return False
    if not username.isalnum():
        return False
    return True

def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/<username>/data/user_emails.csv')
    # Find and print the email
    return email_dict.get(fullname.lower())
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))



print(validate_user(1,2))