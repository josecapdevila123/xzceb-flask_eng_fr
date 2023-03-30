"""
Module that provides translation functions
"""
import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

def english_to_french(english_text):
    """
    Function that translates English text to French
    """
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(URL)

    # Translate the English text to French
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    # Extract the translated text
    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """
    Function that translates French text to English
    """
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(URL)

    # Translate the French text to English
    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    # Extract the translated text
    english_text = translation['translations'][0]['translation']

    return english_text

