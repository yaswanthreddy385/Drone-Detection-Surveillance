import os
import requests
import time
# Folder Path
path = "E:\yolo\yolov5-master\Runs\detect\exp\labels"

# Change the directory
os.chdir(path)

def send_to_telegram(message):

    apiToken = '5760045578:AAHcX6s8hEfLuJ-06qijiZTT1pauuG31_Nk'
    chatID = '-930110912'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
#read the text file
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            x=line[0]
    return x
processed_files = set()
# iterate through all file
while True:
    for file in os.listdir():
        if file not in processed_files:
            file_path = f"{path}\{file}"

        # call read text file function
            label= read_text_file(file_path)
            if(label=='1'):
                send_to_telegram("Drone detected!!!!!")
        processed_files.add(file)
        time.sleep(1.5)