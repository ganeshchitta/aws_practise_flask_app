import zipfile
import os

print(os.getcwd())
os.chdir("lambdas/")

def create_zip(filename, zipname):
    with zipfile.ZipFile(zipname, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(filename)

# Example usage: create a zip archive of a file named "example.txt"
create_zip('flask_lambda_copy_data_to_dynamodb.py', "flask-lambda-copy-to-dynamodb.zip")
# create_zip('flask_lambda_copy_data_to_dynamodb.py.py', "copytodynamodbcode.zip")
import shutil
shutil.make_archive("flask-dependencies-lambda-layer", 'zip', 'build')

