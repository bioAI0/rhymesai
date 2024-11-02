import os
import requests

def generate_video(token):
    url = "https://api.rhymes.ai/v1/generateVideoSyn"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "refined_prompt": "Adorable cats playing",
        "num_step": 100,
        "cfg_scale": 7.5,
        "user_prompt": "Adorable cats playing",
        "rand_seed": 12345
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

bearer_token = os.getenv("ALLEGRO_API_KEY")
response_data = generate_video(bearer_token)
print(response_data)


