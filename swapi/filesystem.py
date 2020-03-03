import os


def mkdirs_from_path(path):
    traversed_paths = []
    for directory in path.split("/"):
        traversed_paths.append(directory)
        current_path = os.path.join(*traversed_paths)
        if directory.find(".") == -1:
            if not os.path.exists(current_path):
                os.mkdir(current_path)