import os
import requests

def query_video_status(token, request_id):
    url = "https://api.rhymes.ai/v1/videoQuery"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "requestId": request_id
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

bearer_token = os.getenv("ALLEGRO_API_KEY")
request_id = "6fcbd15a-b6eb-4cf8-b9ab-697238a74462"
response_data = query_video_status(bearer_token, request_id)
print(response_data)

