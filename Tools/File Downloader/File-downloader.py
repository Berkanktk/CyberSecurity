import requests

print('Beginning file download..')

url = input("Enter URL:\n> ")
filename = input('Enter filename with type\n> ')

response = requests.get(url)
file = open(filename, "wb")
file.write(response.content)
file.close()

print('Finished downloading the file')
