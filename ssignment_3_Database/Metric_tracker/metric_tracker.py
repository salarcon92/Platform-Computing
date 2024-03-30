from selenium import webdriver
import time

# Function to get current timestamp
def get_timestamp():
    return time.strftime('%H:%M:%S')

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get("http://localhost:3000/")

# Starting timestamp
start_time = time.time()

# Initial scroll position
last_position = 0

try:
    while True:
        # Get current scroll position
        current_position = driver.execute_script("return window.scrollY")

        # Calculate scrolling distance
        scrolling_pixels = current_position - last_position

        # Update last position
        last_position = current_position

        # Print timestamp, presence time, and scrolling pixels
        print(f"Timestamp: {get_timestamp()}, Presence_time: {int(time.time() - start_time)} seconds, Scrolling: {scrolling_pixels} pixels")

        # Write data into a csv file 
        with open('metric_tracker.csv', 'w', newline='') as f: 
            writer = csv.DictWriter(f,fieldnames=metrictracker_dict.keys())
            writer.writeheader()
            writer.writerow(metrictracker_dict)

        # Sleep for 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    driver.quit()