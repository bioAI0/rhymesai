import base64
import os
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

base64_image_1 = image_to_base64('image1.jpg')
base64_image_2 = image_to_base64('image2.jpg')

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
                    "text": "<image><image>\nPlease rate the cutness of these two images on a scale from 1 to 100 on a variety of measures including cuteness, how engaging the image is and if there are any visual distortions but be a very harsh judge with an average score for a cute cat being 50.  Based on this and the previous prompt which was 'generate images of adorable cats' please make a new prompt for a diffusion based video generation image that is designed to be extremely engaging for viewers so much so they can't tear their eyes away.  "
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
