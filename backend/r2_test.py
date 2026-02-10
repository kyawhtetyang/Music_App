import boto3

# Cloudflare R2 credentials
R2_ACCESS_KEY = "c6f7dfa98bf8626202d454dc866a453a"
R2_SECRET_KEY = "4e3cc1c3dff91d81475bdc96092a0d15bd290224a5df7c16e3181f605c0f0b1c"
R2_ENDPOINT = "https://f58fea9e1b60da06ec030cf25a67cc53.r2.cloudflarestorage.com"
BUCKET_NAME = "music-app-album"

# Create S3 client pointing to R2
client = boto3.client(
    's3',
    endpoint_url=R2_ENDPOINT,
    aws_access_key_id=R2_ACCESS_KEY,
    aws_secret_access_key=R2_SECRET_KEY
)

# List objects in the bucket
response = client.list_objects_v2(Bucket=BUCKET_NAME)
for obj in response.get('Contents', []):
    print(obj['Key'])


