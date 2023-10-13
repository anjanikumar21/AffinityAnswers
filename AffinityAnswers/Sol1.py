# Import requests library to make HTTP requests
import requests

# Define a function that takes an address as input and returns True if the PIN code is valid, False otherwise
def validate_pin_code(address):
  # Get the PIN code from the address
  pin_code = address.split(",")[-1].strip()
  # Get the response from the API
  response = requests.get(f"https://api.postalpincode.in/pincode/{pin_code}")
  # Check if the response is OK
  if response.ok:
    # Get the data from the response
    data = response.json()
    # Check if the data is valid
    if data and data[0].get("Status") == "Success":
      # Get the post offices from the data
      post_offices = data[0].get("PostOffice", [])
      # Check if any post office matches the address
      for post_office in post_offices:
        # Get the details of the post office
        name = post_office.get("Name", "")
        district = post_office.get("District", "")
        state = post_office.get("State", "")
        country = post_office.get("Country", "")
        # Normalize the address by removing spaces and lowercasing
        normalized_address = address.lower().replace(" ", "")
        # Check if the address contains all the details of the post office
        if (name.lower() in normalized_address and
            district.lower() in normalized_address and
            state.lower() in normalized_address and
            country.lower() in normalized_address):
          # Return True as the PIN code is valid for this address
          return True
      # Return False as none of the post offices match the address
      return False
    else:
      # Return False as the data is invalid
      return False
  else:
    # Return False as the response is not OK
    return False

# Test the function with some examples
correct_addresses = ["2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050",
                     "2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050",
                     "374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050"]

incorrect_addresses = ["2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095",
                       "Colony, Bengaluru, Karnataka 560050"]

for address in correct_addresses:
  print(f"Address: {address}")
  print(f"PIN code valid: {validate_pin_code(address)}")
  print()

for address in incorrect_addresses:
  print(f"Address: {address}")
  print(f"PIN code valid: {validate_pin_code(address)}")
  print()
