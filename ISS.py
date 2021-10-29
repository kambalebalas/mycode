#!/usr/bin/env python3
# imports always go at the top of your code
import requests
import os
import json

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get("http://api.open-notify.org/iss-now.json")

    # display the methods available to our new object
    #print( dir(resp) )
    space_data= resp.json()
    #os.chdir("/home/student/mycode/")
    #with open("iss-now.json", "r") as of:
        # space_data is python data types returned by our conversion tool json.load()
        #space_data = json.load(of)

    # test to ensure I can now work with the data in Python
    #print(space_data)            # we should now see the data from the file
    #print(type(space_data))      # the data type should be 'dict' NOT 'str'
    print(" CURRENT LOCATION OF THE ISS:", space_data.get('iss_position'))  # perform a test lookup on a 'dict' data type
    print(" Timestamp is : ", space_data.get('timestamp'))

if __name__ == "__main__":
    main()
