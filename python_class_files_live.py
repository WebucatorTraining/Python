import zipfile, urllib.request, shutil, os

course_id = input('Course ID: ').upper()
url = 'https://www.webucator.com/ClassFiles/getClassFiles.cfm?Type=Onsite&CourseID=' + course_id
file_name = 'classfiles.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

with zipfile.ZipFile(file_name) as zf:
    zf.extractall()
