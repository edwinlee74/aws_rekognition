'''
注意:
1. 圖片格式需為PNG或JPEG。
2. 圖片可以base64或直接存放S3 bucket。
3. 以AWS CLI不能以base64編碼(bytes)方式, 只能透過S3 bucket來存取圖片。
4. 圖片不超過5MB。
'''
import boto3

client = boto3.client('rekognition')

def detect_faces(photo, bucket):
    '''偵測圖片中的人臉特徵'''
    response = client.detect_faces(Image={'S3Object':
                {'Bucket':bucket,'Name':photo}}, Attributes=[
                'ALL'])
    return response

def detect_labels(photo, bucket):
    '''偵測圖片中的物件, 如花、樹木、 桌子, 或是像生日派對、緍禮事件'''
    response = client.detect_labels(Image={'S3Object':
                {'Bucket':bucket,'Name':photo}}, MaxLabels=20, 
                MinConfidence=90.0)
    return response  

def compare_faces(source, target, bucket):
    '''比較兩張圖片中的人臉昰否同一人'''
    response = client.compare_faces(SourceImage={'S3Object':
                {'Bucket':bucket,'Name':source}},
                TargetImage={'S3Object':
                {'Bucket':bucket,'Name':target}},
                SimilarityThreshold=95.0     
    )  
    return response