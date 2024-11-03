import os
import sys
import requests

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
        "rand_seed": 12345
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            prompt = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        sys.exit(1)

    bearer_token = os.getenv("ALLEGRO_API_KEY")

    if not bearer_token:
        print("Error: ALLEGRO_API_KEY environment variable not set.")
        sys.exit(1)

    print(prompt, file=sys.stderr)
    
    response_data = generate_video(bearer_token, prompt)
    print(response_data)

if __name__ == "__main__":
    main()
