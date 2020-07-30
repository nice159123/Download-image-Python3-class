# Download-image-Python3-class
Class Download images
```
$ git clone https://github.com/nice159123/Download-image-Python3-class.git download_img
$ cd download_img
$ py download_img.py
```
# Functions
## request(url[string], stream[bool])
request ลิ้งค์
```
    """
    # 
    # Requests
    # 
    """
    def request(self, url, st = False):
        return requests.get(url, stream=st)
```
## regexCode(code[string], regex[string])
ค้นหา tag 
```
    """
    # 
    # Regex Code
    # 
    """
    def regexCode(self, code, regex):
        return re.finditer(regex, code, re.MULTILINE)
```
## getDataGroups(datas[Array])
ดึงข้อมูลใส่ Array
```
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
```
## download(url[string], image_path[string], image_name[string])
ดาวน์โหลด
```
    """
    # 
    # Download
    # 
    """
    def download(self, url, image_path, image_name):
        try:
            path = '{path}/{name}'.format(path = image_path, name = image_name)
            fileImage = open(path, 'wb')
            fileImage.write(self.request(url, True).content)
            fileImage.close()
        except IOError:
            print('Download: {name}\t\t[error]'.format(name = image_name))
            return False
        else:
            print('Download: {name}\t\t[success]'.format(name = image_name))
            return True
```
## create_directory(directory_name[string])
สร้าง Folder
```
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
```
## delete_directory(directory_name[string])
ลบ Folder
```
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
```
