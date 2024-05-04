import pygame

# Initialize Pygame
pygame.init()

# Initialize the mixer module
pygame.mixer.init()

# Set the dimensions of the window
window_width = 800
window_height = 600

# Create the window
window = pygame.display.set_mode((window_width, window_height))

# Load the logo
logo = pygame.image.load('markstudios_logo.png')
logo_rect = logo.get_rect()
logo_rect.center = (window_width // 2, window_height // 2)

# Load the "missing.png" image
missing_image = pygame.image.load('missing.png')
missing_rect = missing_image.get_rect()
missing_rect.center = (window_width // 2, window_height // 2)

# Set the duration for each phase
fade_in_duration = 1000 # 1 second
stay_duration = 850 # 0.85 seconds
fade_out_duration = 1000 #1 second
# The duration is alligned to be on beat 

# Calculate the number of frames for each phase
fade_in_frames = fade_in_duration // 16 # Assuming 60 FPS
stay_frames = stay_duration // 16
fade_out_frames = fade_out_duration // 16

# Set the initial alpha value for the logo
alpha = 0

# Initialize a counter for the animation phase
animation_phase = 0

# Load and play the music
pygame.mixer.music.load('missingmusic.mp3')
pygame.mixer.music.play(-1) # Loop indefinitely

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fade in, stay, and fade out as before
    if animation_phase == 0: # Fade in phase
        # Fade in logic here
        if alpha < 255:
            alpha += 255 // fade_in_frames
            if alpha > 255:
                alpha = 255
        if alpha >= 255:
            animation_phase = 1 # Move to the stay phase
    elif animation_phase == 1: # Stay phase
        # Stay logic here
        stay_frames -= 1
        if stay_frames <= 0:
            animation_phase = 2 # Move to the fade out phase
    elif animation_phase == 2: # Fade out phase
        # Fade out logic here
        if alpha > 0:
            alpha -= 255 // fade_out_frames
            if alpha < 0:
                alpha = 0
        if alpha <= 0:
            # Set the background to white
            window.fill((255, 255, 255))
            # Display the "missing.png" image
            window.blit(missing_image, missing_rect)
            # Update the display
            pygame.display.flip()

    # Draw the logo with the current alpha value
    logo_surface = pygame.Surface(logo.get_size(), pygame.SRCALPHA)
    logo_surface.blit(logo, (0, 0))
    logo_surface.set_alpha(alpha)
    window.blit(logo_surface, logo_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()