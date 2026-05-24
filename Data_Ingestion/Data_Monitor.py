from libraries import *


def data_monitor(folder_path):

    file_paths = []

    for file in os.listdir(
        folder_path
    ):

        file_path = os.path.abspath(
            os.path.join(
                folder_path,
                file
            )
        )

        if os.path.isfile(
            file_path
        ):

            print(
                f"File found: "
                f"{file}"
            )

            file_paths.append(
                file_path
            )

    return file_paths