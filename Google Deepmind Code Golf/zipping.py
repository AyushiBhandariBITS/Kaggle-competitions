import zipfile
import os

submission_zip = f"submission.zip"

with zipfile.ZipFile(submission_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    task_count = 0
    for task_num in range(1, 401):
        task_id = f"{task_num:03d}"
        src_path = f"submission/task{task_id}.py"
        
        if os.path.exists(src_path):
            zipf.write(src_path, arcname=f"task{task_id}.py")
            task_count += 1

print(f"Created submission zip with {task_count} tasks: {submission_zip}")

# Display zip file size
zip_size = os.path.getsize(submission_zip)
print(f"Submission zip size: {zip_size:,} bytes ({zip_size/1024:.1f} KB)")