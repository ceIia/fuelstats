def download_archive(file_name, bucket_name): 
  import boto3, botocore, random, string, os
  from zipfile import ZipFile

  s3 = boto3.resource('s3')
  
  def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
  
  archive_name = '/tmp/' + randomStringDigits(8) + '_' + os.getenv("DATA_ARCHIVE_NAME") + '_archive.zip'
  target_file_name = os.getenv("DATA_ARCHIVE_NAME") + '.zip'
  
  # download file from aws s3 somehow
  try:
    s3.Bucket(os.getenv("S3_BUCKET_NAME")).download_file(target_file_name, archive_name)
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
      print("The S3 object you requested does not exist.")
    if e.response['Error']['Code'] == "403":
      print("You do not have permission to access the S3 object you requested.")
    else:
      raise
     
  with ZipFile(archive_name, 'r') as zipObj:
    for name in zipObj.namelist():
      localFilePath = zipObj.extract(name, '/tmp/')
    
    files = (localFilePath, archive_name)
  # return xml file name path
  return files