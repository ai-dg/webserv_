import requests
from concurrent.futures import ThreadPoolExecutor
import time

URL = "http://localhost:8080"  
NUM_REQUESTS = 100               
CONCURRENCY = 1                

def make_request(index):
    try:
        response = requests.get(URL, timeout=5)  
        return response.status_code
    except requests.RequestException as e:
        return f"Error: {e}"

start_time = time.time()
with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
    responses = list(executor.map(make_request, range(NUM_REQUESTS)))

end_time = time.time()
success_count = sum(1 for r in responses if r == 200)
error_count = NUM_REQUESTS - success_count

print(f"Total requests: {NUM_REQUESTS}")
print(f"Success responses: {success_count}")
print(f"Errors: {error_count}")
print(f"Total time: {end_time - start_time:.2f} seconds")
