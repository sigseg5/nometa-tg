from shutil import move
import piexif


def delete_metadata(full_path_to_img):
    piexif.remove(full_path_to_img, "clean_image.jpg")
    move("clean_image.jpg", "documents/clean_image.jpg")
