import zipfile, urllib.request, shutil, os

course_id = input('Course ID: ').upper()
if course_id == 'PYT211':
    url = 'https://www.webucator.com/class-files/index.cfm?versionId=4283'
elif course_id == 'PYT251':
    url = 'https://www.webucator.com/class-files/index.cfm?versionId=3804'
else:
    url = 'https://www.webucator.com/ClassFiles/getClassFiles.cfm?CourseID=' + course_id
file_name = 'classfiles.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

with zipfile.ZipFile(file_name) as zf:
    zf.extractall()
