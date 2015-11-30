import zipfile, urllib.request, shutil, os

courseid = input('Course ID: ')
url = 'https://www.webucator.com/ClassFiles/getClassFiles.cfm?CourseID=' + courseid
file_name = 'classfiles.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()
