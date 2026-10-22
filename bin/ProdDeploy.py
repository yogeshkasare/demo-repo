import time

start = time.monotonic()
duration = 35

print("Deployment started", flush=True)

counter = 1

while True:
    elapsed = time.monotonic() - start

    if elapsed >= duration:
        break

    print(f"Deployment processing... {counter}", flush=True)
    counter += 1

    remaining = duration - (time.monotonic() - start)
    time.sleep(min(3, max(0, remaining)))

print("Deployment completed", flush=True)
