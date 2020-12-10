from shutil import move
import piexif


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
