import turtle
import requests
from PIL import Image

def download_image(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Create a file-like object for the response content
    with open("image.jpg", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    return "image.jpg"

def draw_image(filename):
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    image = Image.open(filename)
    width, height = image.size

    # Calculate the scaling factor to fit the image within the screen
    scale = min(screen.window_width() / width, screen.window_height() / height)

    screen.setworldcoordinates(0, height * scale, width * scale, 0)

    turtle.speed(10)  # Fastest speed
    turtle.penup()
    turtle.hideturtle()

    # Loop through each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the RGB color of the pixel
            r, g, b = image.getpixel((x, y))

            # Convert the color to grayscale
            gray = (r + g + b) / 3

            # Set the turtle pen color
            turtle.pencolor((gray / 255, gray / 255, gray / 255))

            # Set the turtle position
            turtle.goto(x * scale, y * scale)

            # Draw a small dot
            turtle.pendown()
            turtle.dot(1)
            turtle.penup()

    turtle.done()

url = "" # Вставьте вашу картинку
filename = download_image(url)
draw_image(filename)