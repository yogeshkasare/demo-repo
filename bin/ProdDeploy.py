import sys
import time

print("Starting demo deployment...", flush=True)
time.sleep(2)

print("Checking deployment configuration...", flush=True)
time.sleep(2)

print("Uploading deployment artifact...", flush=True)
time.sleep(2)

print("Upload completed successfully.", flush=True)
time.sleep(2)

# Simulate the AWS Glue error seen in the customer logs
print(
    "An error occurred (IdempotentParameterMismatchException) "
    "when calling the CreateJob operation: "
    "Job already submitted with different configuration.",
    flush=True
)

time.sleep(2)

print("Continuing deployment after the error...", flush=True)
time.sleep(2)

print("Deployment script completed.", flush=True)

# Important: return success even though we printed an error
sys.exit(0)
