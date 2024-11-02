import os
import sys
import ast
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

def get_request_id_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Using ast.literal_eval to safely evaluate the string content
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

    response_data = query_video_status(bearer_token, request_id)
    print(response_data)
