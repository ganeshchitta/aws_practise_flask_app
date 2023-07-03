import zipfile

def create_zip(filename, zipname):
    with zipfile.ZipFile(zipname, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(filename)

# Example usage: create a zip archive of a file named "example.txt"
create_zip('copy_post_data_to_dynamodb.py', "copytodynamodbcode.zip")
create_zip('copy_post_data_to_dynamodb.py', "copytodynamodbcode.zip")
import shutil
shutil.make_archive("dependencies", 'zip', 'build')
shutil.make_archive("flaskdependencies", 'zip', 'build')

