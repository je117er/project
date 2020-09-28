from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles auth

# upload files
drive = GoogleDrive(gauth)
file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello World!')
file1.Upload()

# update file1's metadata (e.g., its name)
file1['title'] = 'HelloWorld.txt'
file1.Upload()  # Update metadata
print('title: {}'.format(file1['title']))

# download file metadata from file ID
# create googledrivefile instance with fileid of file1
file2 = drive.CreateFile({'id': file1['id']})
print('title: {}, mimeType: {}'.format(file2['title'], file2['mimeType']))

# download file content
file2.GetContentFile('HelloBuddy.txt')

# paginate file lsits by specifying number of max results
# list files in Trash
for file_list in drive.ListFile({'q': 'trashed=true', 'maxResults': 10}):
    print('Received {} files from Files.list()'.format(len(file_list)))  # <= 10
    for file1 in file_list:
        print('title: {}, id: {}'.format(file1['title'], file1['id']))

# some other file editing methods
# file1.Trash()
# file1.Untrash()
# file1.Delete()

'''
# auto-iterate through all files matching this query
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
    print('title: {}, id: {}'.format(file1['title'], file1['id']))
'''
