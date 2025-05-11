from urllib import request

from base import Base

def download_file(url, save_path, iteration):
    print(f'Starting {iteration} iteration')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    requests = request.Request(url, headers=headers)

    try:
        with request.urlopen(requests) as response:
            with open(save_path, 'wb') as out_file:
                out_file.write(response.read())
        print(f"File downloaded successfully and saved as {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

function_objs = Base(10)
for i in range(100):
    priority = i % 10
    function_objs.add_function(download_file, args=("https://link.testfile.org/PDF10MB", f""
                                                           f"sample_{i}.mov", i), priority=priority)


function_objs.execute()


