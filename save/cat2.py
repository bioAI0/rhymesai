import os
import sys
import time
import requests

def read_file(file_path):
    """Reads the content of the provided file and returns it."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        sys.exit(1)

def generate_video(token, prompt):
    """Starts video generation and returns the request ID."""
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
        return response.json().get("requestId")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def query_video_status(token, request_id):
    """Checks the status of the video generation."""
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
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def download_image(token, download_url):
    """Downloads the image from the given URL."""
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    try:
        response = requests.get(download_url, headers=headers)
        response.raise_for_status()

        # Save the image to a file
        with open("image1.jpg", 'wb') as file:
            file.write(response.content)
        print("Image downloaded as image1.jpg")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    file_content = read_file(input_file)
    
    bearer_token = os.getenv("ALLEGRO_API_KEY")
    if not bearer_token:
        print("Environment variable ALLEGRO_API_KEY is not set.")
        sys.exit(1)

    request_id = generate_video(bearer_token, file_content)
    if not request_id:
        print("Failed to get request ID.")
        sys.exit(1)

    while True:
        status = query_video_status(bearer_token, request_id)
        if status.get("status") != "":
            download_url = status.get("download_url")
            if download_url:
                download_image(bearer_token, download_url)
            break
        else:
            print("Waiting for video to complete...")
            time.sleep(5)

if __name__ == "__main__":
    main()
