import os
import sys
import ast
import time
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
        return {"error": str(e)}

def get_request_id_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = ast.literal_eval(file.read())
            return data.get('data', None)
    except (FileNotFoundError, SyntaxError) as e:
        print(f"Error reading request ID from file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    request_id = get_request_id_from_file(file_path)

    if not request_id:
        print("Request ID not found in the file.")
        sys.exit(1)

    bearer_token = os.getenv("ALLEGRO_API_KEY")
    if not bearer_token:
        print("Bearer token not found.")
        sys.exit(1)

    video_url = None
    while not video_url:
        response_data = query_video_status(bearer_token, request_id)
        if 'error' in response_data:
            print(response_data['error'])
            sys.exit(1)

        # Extract the 'data' field
        video_url = response_data.get('data', None)
        print("Video not available yet, waiting to retry...",
              end='',file=sys.stderr)
        if not video_url:
            print('.', end='', flush=True)
            time.sleep(10)  # Wait for 10 seconds before retrying

    print(f"Video URL: {video_url}")
