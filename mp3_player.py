import pygame



def mp3_p(file_name):

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load(file_name)  # Replace 'your_file.mp3' with the path to your MP3 file

    # Play the loaded MP3 file
    pygame.mixer.music.play()



