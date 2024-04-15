import urllib3

http = urllib3.PoolManager()

mp4_link = input("Input the URL here : ")

file_name = input("Input your filename here as .mp4: ")
response = http.request("GET", mp4_link)
if response.status == 200:
    with open(file_name, 'wb') as f:
        f.write(response.data)
    print("Download completed successfully.")

else:
    print("Download failed. Status code : ", response.status)
