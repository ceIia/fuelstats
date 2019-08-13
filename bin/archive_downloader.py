import wget

def download_archive(file_name, bucket_name):
  # build url
  
  url = "https://" + bucket_name + ".s3.eu-west-3.amazonaws.com/" + file_name + ".xml"
  print(url)
  
  # download the xml data archive
  fileName = wget.download(url, 'temp/')
  
  filePath = fileName

  # return xml file name path
  return filePath