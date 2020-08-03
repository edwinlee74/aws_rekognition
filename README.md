# AWS Rekognition

Rekognition 是AWS所提供的一種臉部辨識服務, 除了人臉識別外, 也可偵測開心或悲傷等情緒。

# Requirements

- python 3+
- boto3             => aws SDK
- aws cli v2        => aws command line tool(https://docs.aws.amazon.com/zh_tw/cli/latest/userguide/install-cliv2.html)

# Installation

        pip install boto3

# Using the AWS CLI

安裝完aws cli v2後, 需在aws 上建立IAM帳號, AWS建議不要以root帳號操作, 而是開放對服務所需的權限即可, 使用rekognition需要AmazonRekognitionFullAccess和AmazonS3ReadOnlyAccess。

注意: 使用帳號所在的region需與S3所在的region相同, 否則會報錯。

        aws rekognition detect-labels --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" --region us-west-2

如沒問題, 上述指令應可從S3抓取圖片, 並回傳分析結果。

# Using AWS SDK API

SDK 的API可參考 [官方文件](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html)

直接引入boto3後, 指定所要使用的服務名稱。

                import boto3
                client = boto3.client('rekognition')
