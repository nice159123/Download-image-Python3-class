# import
import re
import os
import requests

class DownloadImg:

    fullPath = ''
    link = ''

    def __init__(self):
        print('Download Image')

    """
    # 
    # Requests
    # 
    """
    def requestd(self, url, st = False):
        return requests.get(url, stream=st)

    """
    # 
    # Regex Code
    # 
    """
    def regexCode(self, code, regex):
        return re.finditer(regex, code, re.MULTILINE)

    """
    # 
    # Get Data Groups
    # 
    """
    def getDataGroups(self, datas):
        data_log = []
        for data in datas:
            data_log.append(data.groups()[0])
        return data_log

    """
    # 
    # Download
    # 
    """
    def download(self, url, image_path, image_name):
        try:
            path = '{path}/{name}'.format(path = image_path, name = image_name)
            fileImage = open(path, 'wb')
            fileImage.write(self.requestd(url, True).content)
            fileImage.close()
        except IOError:
            print('Download: {name}\t\t[error]'.format(name = image_name))
            return False
        else:
            print('Download: {name}\t\t[success]'.format(name = image_name))
            return True

    """
    # 
    # Create Directory
    # 
    """
    def create_directory(self, directory_name):
        try:
            if not os.path.exists(directory_name):
                os.makedirs(directory_name)
        except OSError:
            print ("Creation of the directory %s failed" % directory_name)
            return False
        else:
            print ("Successfully created the directory %s" % directory_name)
            return True

    """
    # 
    # Delete Directory
    # 
    """
    def delete_directory(self, directory_name):
        try:
            if not os.path.exists(directory_name):
                os.rmdir(directory_name)
        except OSError:
            print ("Deletion of the directory %s failed" % directory_name)
            return False
        else:
            print ("Successfully deleted the directory %s" % directory_name)
            return True
# main
def main():
    img1 = DownloadImg()
    img1.create_directory('nice')
    img1.download('https://images.freeimages.com/images/large-previews/dfa/jungle-1377573.jpg', 'uploads', 'image1.jpg')

# run
if __name__ == "__main__":
    main()
