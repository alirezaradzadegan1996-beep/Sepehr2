
class ImageInput:

    def receive(self, image):

        return {
            "image": image,
            "status": "received"
        }


image_input = ImageInput()
