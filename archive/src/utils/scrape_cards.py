"""
ace - https://upload.wikimedia.org/wikipedia/commons/5/5f/English_pattern_ace_of_clubs.svg
two - https://upload.wikimedia.org/wikipedia/commons/3/30/English_pattern_2_of_clubs.svg
jack - https://upload.wikimedia.org/wikipedia/commons/8/80/English_pattern_jack_of_clubs.svg
queen - https://en.wikipedia.org/wiki/File:English_pattern_queen_of_clubs.svg
king - https://en.wikipedia.org/wiki/File:English_pattern_king_of_clubs.svg
diamonds ace - https://en.wikipedia.org/wiki/File:English_pattern_ace_of_diamonds.svg
heart ace - https://en.wikipedia.org/wiki/File:English_pattern_ace_of_hearts.svg
spades ace - https://en.wikipedia.org/wiki/File:English_pattern_ace_of_spades.svg
"""
import requests

# Dictionary of card names and their corresponding URLs
cards = {
    "ace": "https://upload.wikimedia.org/wikipedia/commons/5/5f/English_pattern_ace_of_clubs.svg",
    # Add the rest of your cards here...
}

for card, url in cards.items():
    # Download the image
    image_response = requests.get(url)

    # Save the image to a file
    with open(f'{card}.svg', 'wb') as f:
        f.write(image_response.content)


        