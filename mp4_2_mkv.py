""" remux mp4 to mkv """

from os import getcwd, listdir
import glob
import subprocess

dir_path = getcwd()
file_list = listdir(dir_path)
# mp4_files = Path(dir_path).glob('*.mp4')
mp4_files = glob.glob("*.mp4")

if not glob.glob("*.mp4"):
    raise Exception("There are no MP4 files.")

print("The current working directory is " + dir_path)
print(f"The files in the working directory are: {file_list}")
print(f"The MP4 files in the working directory are: {mp4_files}")

for file_name in mp4_files:
    print(file_name)
    filename_without_ext = path.splitext(file_name)[0]
    print(filename_without_ext)
    output_name = str.lower(filename_without_ext) + ".mkv"
    print(output_name)
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                f"{file_name}",
                "-c",
                "copy",
                "-map",
                "0",
                f"{output_name}",
            ],
            check=True,
        )
    except Exception:
        raise Exception("FFMPEG is not present")
