import boto3
import os
from boto3.s3.transfer import TransferConfig

# -----------------------------
# R2 Cloudflare credentials
# Make sure these are exported in terminal, NOT hardcoded
# export AWS_ACCESS_KEY_ID="YOUR_KEY"
# export AWS_SECRET_ACCESS_KEY="YOUR_SECRET"
# export AWS_DEFAULT_REGION="auto"
# -----------------------------
R2_ENDPOINT = "https://f58fea9e1b60da06ec030cf25a67cc53.r2.cloudflarestorage.com"
BUCKET_NAME = "music-app-album"
LOCAL_MUSIC_DIR = "./music_library"

# -----------------------------
# Boto3 client
# -----------------------------
client = boto3.client(
    "s3",
    endpoint_url=R2_ENDPOINT,
    region_name="auto"
)

# -----------------------------
# Transfer config to disable multipart upload for smaller files
# -----------------------------
config = TransferConfig(
    multipart_threshold=1024 * 1024 * 1024  # 1GB threshold, disables multipart for smaller files
)

# -----------------------------
# Upload files recursively
# -----------------------------
for root, dirs, files in os.walk(LOCAL_MUSIC_DIR):
    for file in files:
        local_path = os.path.join(root, file)
        relative_path = os.path.relpath(local_path, LOCAL_MUSIC_DIR)
        print(f"Uploading {relative_path}...")
        client.upload_file(
            local_path,
            BUCKET_NAME,
            relative_path,
            Config=config
        )

print("✅ Upload complete")

