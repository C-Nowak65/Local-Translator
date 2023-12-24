'''Used to handle the backend processes of the translation.'''

#imports
import requests

def translate_text(text, source_language, target_language):
    '''Main function used to translate text using the Libretranslate public api.'''

    url = "https://libretranslate.com/translate"

    payload = {
        "q": text,
        "source": source_language,
        "target": target_language,
        "format": "text"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['translatedText']
    else:
        return f"Error: {response.status_code} Unable to translate text."
    
def get_supported_languages():
    url = "https://libretranslate.com/languages"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            languages = response.json()
            return[lang['name'] for lang in languages]
        else:
            print("Error fetching languages:", response.status_code)
    except requests.RequestException as e:
        print(f"Request failed:", e)
    
    return []
