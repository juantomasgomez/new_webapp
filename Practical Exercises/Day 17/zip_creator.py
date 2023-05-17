import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    folderpath = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(folderpath, 'w') as archive:
        for i in filepaths:
            i = pathlib.Path(i)
            archive.write(i, arcname=i.name)

if __name__ == "__main__":
    make_archive(filepaths=["abc.txt", "def.txt" ], dest_dir='../../Files/dest')

