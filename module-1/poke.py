# this script asks the user for a webpage and uses the requests and time packages in order to "ping"
# the page. A timer is started before this ping and once it is completed. The length of the variable 
# associated with the ping is the amount of bytes collected. With known "ping" time this can be turned
# into mega bytes per second


import requests
import time

# ask user to input webpage without prefix
url = input("desired url (https:// prefix not needed): ")
# turn the simple input into the full url with prefix using f-string concatenation
urlString = f"https://{url}"
# start timer
startTime = time.perf_counter()
# go to webpage and count how many bytes were collected
response = requests.get(urlString)
# end timer
endTime = time.perf_counter()
# find the amount of bytes collected which is the length of the variable associated with the "ping"
nbytes = len(response.content)
poke = endTime - startTime
# calcualte mega bytes per second
mbs = (nbytes / 1e6) / (poke)

# print the results in f-string with line breaks
print(f"{nbytes} bytes read from {url}\n"
      , f"speed: {mbs: .1f}MB/s\n", 
      f"poke: {poke * 1000: .1f}ms")