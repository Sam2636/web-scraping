import requests

#response = requests.get("https://generator.artblocks.io/1017")
response = requests.get("https://lh3.googleusercontent.com/GNgiQdyLRqvDFfYO6Vk5T8POHB7zi8U2DGnDJGTYtysYLOSkaZvfLDUeZNtop6ApgaT-_NhMco9ImD3DDxS5z3hsdw=w600")

file=open("1017.jpg",'wb')
file.write(response.content)
file.close()