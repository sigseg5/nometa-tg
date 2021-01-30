from shutil import move
import piexif
from PIL import Image


# TODO: delete moving file from this func
def delete_metadata(full_path_to_img):
    """
    This function used for remove metadata only from documents, if you send image 'as image' Telegram automatically
    removes all metadata at sending. This function removes all metadata via 'piexif' lib, saved image in '/app'
    folder, and after that move it to 'documents' folder.
    :param full_path_to_img: path to folder with documents e.g.'documents/image.jpg'
    """
    piexif.remove(full_path_to_img, "clean_image.jpg")
    move("clean_image.jpg", "documents/clean_image.jpg")


def delete_metadata_from_png(full_path_to_img):
    """
    This function used for remove metadata only from png documents, if you send image 'as image' Telegram
    automatically removes all metadata at sending. This function removes all metadata via 'PIL' lib and saved image
    in 'documents' folder.
    :param full_path_to_img: path to folder with documents e.g.'documents/image.png'
    """
    # image = Image.open(full_path_to_img)
    #
    # data = list(image.getdata())
    # image_without_exif = Image.new(image.mode, image.size)
    # image_without_exif.putdata(data)
    #
    # image_without_exif.save('documents/clean_image.png')
