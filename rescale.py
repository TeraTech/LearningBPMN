import math
from pathlib import Path

import PIL.ImageQt
from PIL import Image


class Rescale:

    def __init__(self):
        self.currDir = Path(__file__).parent
        self.imagesDir = self.currDir.joinpath("images")
        self.saveDir = self.currDir.joinpath("images/rescaled/")

        images = ["square_image.jpg", "tall_image.jpg", "wide_image.jpg"]

        print("Beginning rescaling")
        self.rescale_images(images, 1920, 1080)

    # Loop through images
    # 1920 x 1080 are default sizes
    def rescale_images(self, image_list, to_width=1920, to_height=1080):
        total = 0
        for image_name in image_list:
            self.rescale_image(image_name, to_width, to_height)
            total += 1
        print("Rescaling complete. " + str(total) + " images rescaled.")

    # Rescale an Image
    def rescale_image(self, image_name, to_width, to_height):
        image_loc = self.imagesDir.joinpath(image_name)
        try:
            image = Image.open(image_loc)
            print(image_name + " is " + str(image.width) + "px wide and " + str(image.height) + "px tall.")
        except FileNotFoundError as e:
            print("ERROR: " + str(e))
            exit()
        except ValueError as e:
            print("ERROR: " + str(e))
            exit()
        except TypeError as e:
            print("ERROR: " + str(e))
            exit()

        if to_width > to_height:
            # Is Wide
            print("Max area is Wide")
            ratio = to_height / image.height
        elif to_width < to_height:
            # Is Tall
            print("Max area is Tall")
            ratio = to_width / image.width
        else:
            # Is Square
            print("Max area is Square")
            ratio = to_height / image.height

        # calculate rescale based on ratio between image and desired area
        new_width = math.floor(image.width * ratio)
        new_height = math.floor(image.height * ratio)

        print("Scaled image " + image_name + " to " + str(new_width) + " width and " + str(new_height) + " height.")

        # resize Print to new rescale size
        size = (int(new_width), int(new_height))
        rescaled_image = image.resize(size, PIL.Image.BICUBIC)
        self.save_image(rescaled_image, image_name)

    # Save Image
    def save_image(self, image: Image, file_name: str):
        output_file = self.saveDir.joinpath(file_name)

        try:
            image.save(output_file)
        except ValueError as e:
            print("ERROR: " + str(e))
            exit()
        except OSError as e:
            print("OSError: " + str(e))
            exit()

        return image
