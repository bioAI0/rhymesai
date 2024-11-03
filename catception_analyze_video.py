import base64
import os
import sys
from openai import OpenAI

base_url = 'https://api.rhymes.ai/v1'
aria_api_key = os.getenv('ARIA_API_KEY')

client = OpenAI(
    base_url=base_url,
    api_key=aria_api_key
)

def image_to_base64(image_path):
    """
    Converts an image to a base64-encoded string.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The base64-encoded string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode("utf-8")
        return base64_string
    except FileNotFoundError:
        return "Image file not found. Please check the path."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def read_previous_prompt(file_path):
    """
    Reads the previous prompt from a specified file.

    Args:
        file_path (str): The path to the file containing the previous prompt.

    Returns:
        str: The previous prompt string.
    """
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "Prompt file not found. Please check the path."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Check for the required number of command-line arguments
if len(sys.argv) < 4:
    print("Usage: python script.py <prompt_file> <image1_path> <image2_path>")
    sys.exit(1)

# Get the file name and image paths from command-line arguments
prompt_file = sys.argv[1]
image1_path = sys.argv[2]
image2_path = sys.argv[3]

previous_prompt = read_previous_prompt(prompt_file)
base64_image_1 = image_to_base64(image1_path)
base64_image_2 = image_to_base64(image2_path)

response = client.chat.completions.create(
    model="aria",  # Model name updated
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_1}"
                    }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_2}"
                    }
                },
                {
                    "type": "text",
                    "text": f"<image><image>\nPlease rate the cuteness of these two images on a scale from 1 to 100 on a variety of measures including cuteness, how engaging the image is but be a very harsh judge with an average score for a cute cat being 50 from the prompt {previous_prompt}.  Please also note if there are any visual distortions."
                }
            ]
        }
    ],
    stream=False,
    temperature=0.6,
    max_tokens=1024,
    top_p=1,
    stop=["<|im_end|>"]
)

print(response.choices[0].message.content)


    
