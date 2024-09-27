import requests
from bs4 import BeautifulSoup

def crawl_website(url ,output_file , counter):
    try:
        counter[0] += 1
        
        response = requests.get(url)
        
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Open the output file in write mode
            with open(f"{output_file}-{counter}.txt", 'w', encoding='utf-8') as f:
                f.write(response.text) 
            
            print(f"HTML content saved to {output_file}-{counter}.txt")

            links = soup.find_all('a')

            for link in links:
                href = link.get('href')
                crawl_website(href, output_file , counter)
        else:
            print(f"Failed to retrieve {url}: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_url = 'https://github.com/Nikoo-Asadnejad' # Replace with your starting URL
    output_filename = "crawled_content"
    counter = [0]  
    
    crawl_website(start_url, output_filename,counter)