import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A6NO3u15x0w2hKkCdlyKa0SZTYUsO7z8bDpiClcKM5KW0WlYJcyH1tQ79NqrhtHtWcnbjVS6GCkc5csfVPnmhZMgy_OxVzjTEJIxLgg7YFuJVYZx6VDSQo7qUrsyU1Ytox_FvbLONCM'
    transferData = TransferData(access_token)

    file_from = input("File to be transfered ")
    file_to =  input(" Enter full path to upload the file to, including the file name")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Your File has been uploaded")


main()
