import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext


def leadership_institute_course_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "leadershipinstitute/course/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )


def leadership_institute_categories_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "leadershipinstitute/categories/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )


def leadership_institute_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "leadershipinstitute/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )
