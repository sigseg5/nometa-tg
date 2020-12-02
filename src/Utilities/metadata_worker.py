from shutil import move
import piexif


def delete_metadata(full_path_to_img):
    piexif.remove(full_path_to_img, "clean_image.jpeg")
    move("clean_image.jpeg", "images/clean_image.jpeg")
