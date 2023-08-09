'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import requests

def main():
    # Test the functions in this module
    test_get_apod_info()
    test_get_apod_image_url()

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    api_url = "https://api.nasa.gov/planetary/apod"
    api_key = "K9VDo6hD4IXFn4x1AvQJLGxEWilyNQR1JitYsTxf"  
    
    params = {
        "date": apod_date,
        "thumbs": True,
        "api_key": api_key
    }

    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        apod_info = response.json()
        return apod_info
    else:
        print("Error:", response.text)
        return None

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    media_type = apod_info_dict.get("media_type")
    if media_type == "image":
        return apod_info_dict.get("url")
    elif media_type == "video":
        return apod_info_dict.get("thumbnail_url")
    else:
        return None

def test_get_apod_info():
    apod_date = "2023-08-01"
    apod_info = get_apod_info(apod_date)
    if apod_info:
        print("APOD Title:", apod_info.get("title"))
        print("APOD Explanation:", apod_info.get("explanation"))

def test_get_apod_image_url():
    apod_date = "2023-08-01"
    apod_info = get_apod_info(apod_date)
    if apod_info:
        image_url = get_apod_image_url(apod_info)
        print("APOD Image URL:", image_url)

if __name__ == '__main__':
    main()