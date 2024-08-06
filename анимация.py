from PIL import Image, ImageDraw, ImageSequence

def create_gif(images, duration=0.1):
    """
    Создает GIF-анимацию из последовательности изображений.

    Args:
        images (list): Список изображений PIL.Image.
        duration (float, optional): Длительность каждого кадра в секундах. По умолчанию 0.1.

    Returns:
        PIL.Image: GIF-анимация.
    """

    frames = []
    for image in images:
        frames.append(image.copy())

    frames[0].save(
        "animated.gif",
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=int(duration * 1000),
        loop=0
    )

    return frames[0]


images = [Image.open(f"image{i}.png") for i in range(1, 4)]
create_gif(images)