from PyDictionary import PyDictionary
import elevenlabs

def get_word_meaning(word):
    dictionary = PyDictionary()
    meaning = dictionary.meaning(word)
    if meaning:
        return meaning['Noun'][0]
    else:
        return f"Sorry, I couldn't find the meaning of {word}."

def generate_audio(text):
    voice_id = "XB0fDUnXU5powFXDhCwa"
    audio = elevenlabs.generate(text=text, voice=voice_id)
    elevenlabs.play(audio)

word_to_lookup = input("Enter a word: ")
meaning = get_word_meaning(word_to_lookup)
generate_audio(meaning)