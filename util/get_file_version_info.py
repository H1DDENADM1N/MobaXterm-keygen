import os
import platform

import win32api


def get_file_version_info(file_path: str) -> tuple[int, int, int, int]:
    """
    Get the version information of a file.

    Args:
        file_path (str): The path of the file.

    Returns:
        tuple[int, int, int, int]: A tuple containing the version information, or (-1, -1, -1, -1) if version info cannot be retrieved.
    """
    if platform.system() != "Windows":
        raise OSError("This function is only supported on Windows.")
    try:
        info = win32api.GetFileVersionInfo(file_path, os.sep)
        ms = info["FileVersionMS"]
        ls = info["FileVersionLS"]
        version = (
            win32api.HIWORD(ms),
            win32api.LOWORD(ms),
            win32api.HIWORD(ls),
            win32api.LOWORD(ls),
        )
        return version
    except Exception as e:
        print(f"Error retrieving file version information: {e}")
        return (-1, -1, -1, -1)


if __name__ == "__main__":
    # Example usage
    file_path = r"C:\Program Files (x86)\Mobatek\MobaXterm\MobaXterm.exe"  # Change this to the path of your MobaXterm executable
    version = get_file_version_info(file_path)
    if version != (-1, -1, -1, -1):
        print(f"MobaXterm Version: {version}")
    else:
        print("Failed to retrieve MobaXterm version information.")
