import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to initialize Selenium with an existing Chrome session
def init_driver_existing_session():
    # Configure the options to connect to the existing browser session
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")  # Point to the existing browser

    # Connect to the existing session
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Function to extract the video URL and the title of the current page
def get_video_url_and_title(driver):
    try:
        # Wait for the video element to load (may need to adjust the wait time)
        time.sleep(2)
        
        # Locate the video element inside the div with id 'vjs_video_3' and extract the 'src' attribute
        try:
            video_element = driver.find_element(By.ID, 'vjs_video_3')
            video_tag = video_element.find_element(By.TAG_NAME, 'video')
            video_url = video_tag.get_attribute('src')  # Extracting the src of the video tag
            print(f"Found video element, video URL: {video_url}")  # Debugging print
            
        except Exception as e:
            print(f"Error locating video element: {e}")
            video_url = None

        # If no video URL found, check other possible places (e.g., other <video> elements)
        if not video_url:
            print("Video element not found or src is missing, checking other possible places.")
            video_elements = driver.find_elements(By.TAG_NAME, 'video')
            for video in video_elements:
                video_url = video.get_attribute('src')
                if video_url:
                    print(f"Found video in another element: {video_url}")  # Debugging print
                    break

        # Extract the video title from the current URL (current page URL)
        current_url = driver.current_url  # Get the current page URL
        title = current_url.split('/')[-2]  # Extract the second last part of the URL path
        title = title.replace('-', '_').lower()  # Replace hyphens with underscores and convert to lowercase

        # Print the extracted title for debugging
        print(f"Extracted Video Title: {title}")
        
        # Locate the 'Next →' button's parent <a> element and extract its href URL
        next_button_link = driver.find_element(By.XPATH, "//a[button[contains(text(), 'Next →')]]")
        next_button_url = next_button_link.get_attribute('href')  # Extract the URL from the <a> tag
        
        # Print the extracted 'Next →' button URL for debugging
        print(f"Extracted 'Next →' Button URL: {next_button_url}")
        
        return video_url, title, next_button_url
    except Exception as e:
        print(f"Error getting video URL and title: {e}")
        return None, None, None

# Function to download a video using requests and save it with a custom filename
def download_video(video_url, filename):
    try:
        print(f"Downloading {filename} from {video_url}")
        
        # Send a GET request to the video URL
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # Check if the request was successful
        
        # Save the video file
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading video: {e}")

# Function to scrape the course pages and download videos
def scrape_and_download_videos(start_url):
    driver = init_driver_existing_session()
    driver.get(start_url)

    video_count = 1

    while True:
        # Get the video URL, title, and the 'Next →' button URL from the current page
        video_url, title, next_button_url = get_video_url_and_title(driver)
        if video_url and title:
            # Create the filename: '1_video_title.mp4'
            filename = f"{video_count}_{title}.mp4"
            
            # Download the video
            download_video(video_url, filename)
            
            # Increment the video count
            video_count += 1
        else:
            print("Video URL or title not found on this page.")
        
        # Directly navigate to the next page using the 'Next →' URL
        if next_button_url:
            try:
                print(f"Navigating to next page: {next_button_url}")
                driver.get(next_button_url)  # Navigate to the next URL
                
                # Wait for the next page to load
                time.sleep(3)  # You can adjust the wait time if necessary
            except Exception as e:
                print(f"Error navigating to the next page: {e}")
                print("No 'Next' button found or unable to navigate. Exiting...")
                break
        else:
            print("No 'Next' button found or unable to navigate. Exiting...")
            break
    
    driver.quit()

# Entry point: start scraping from the given URL
if __name__ == '__main__':
    start_url = 'https://www.jointaro.com/course/crash-course-data-structures-and-algorithms-concepts/course-welcome/'
    scrape_and_download_videos(start_url)
