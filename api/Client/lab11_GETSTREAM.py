import requests


def main():
    url = 'https://brandontgj2o.files.wordpress.com/2012/10/ocean-300.jpg'

    # To mantain the connection open when it request the resource
    # It's useful when is required to download large field
    with requests.get(url, stream=True) as response:
        with open('image.jpg', 'wb') as file:
            for chunk in response.iter_content():
                print('#', end='')
                file.write(chunk)


if __name__ == '__main__':
    main()
