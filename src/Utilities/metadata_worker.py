from PIL import Image


def delete_metadata(full_path_to_img):
    image_filename = "picture_with_EXIF.jpg"
    image_file = open('image_filename')
    image = Image.open(image_file)

    # next 3 lines strip exif
    image_data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(image_data)

    image_without_exif.save(u"clean_{}".format(image_filename))
