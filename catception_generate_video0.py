import os
import sys
import requests
import random

def generate_video(token, prompt):
    url = "https://api.rhymes.ai/v1/generateVideoSyn"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "refined_prompt": prompt,
        "num_step": 100,
        "cfg_scale": 7.5,
        "user_prompt": prompt,
        "rand_seed": random.randint(1, 10000)
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <prompt>")
        sys.exit(1)
    
    prompt = sys.argv[1]
    bearer_token = os.getenv("ALLEGRO_API_KEY")

    if not bearer_token:
        print("Error: ALLEGRO_API_KEY environment variable not set.")
        sys.exit(1)

    response_data = generate_video(bearer_token, prompt)
    print(response_data)

if __name__ == "__main__":
    main()
