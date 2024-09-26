import requests
import json
from pydub import AudioSegment
import io

url = 'http://43.205.228.194'  # Adjust the port if necessary
audio_file_path = "input_audio/ai.wav"

payload = {
    "data": [
        "Shut up shabika fathima",
        "en-US-AvaNeural",
        None
    ],
    "event_data": None,
    "fn_index": 1
}

response = requests.post(url+"/run/predict", json=payload)

if response.status_code == 200:
    try:
        json_data = response.json() 

        data = json_data.get('data')
        file_name = url + "/file=" +data[0]['name']

        response = requests.get(file_name)

        if response.status_code == 200:
            # with open("downloaded_audio.mp3", "wb") as file:
            #     file.write(response.content)
            mp3_data = io.BytesIO(response.content)
            audio = AudioSegment.from_mp3(mp3_data)
            audio.export(audio_file_path, format="wav")
            
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")

    except ValueError:
        print("Response is not in valid JSON format")
else:
    print(f"Request failed with status code: {response.status_code}")