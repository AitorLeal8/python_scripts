import urllib.request as urllib

def check_url(url):
    print("\nChecking URL...")
    
    try:
        res = urllib.urlopen(url)
        print("Connection to", url, "successful")
        print("Response code:", res.getcode())
    
    except urllib.URLError as e:
        print("Error, connection failed", e.reason)
    
    except ValueError as e:
        print("Error, invalid URL", e)

user_url = input("Enter a URL: ")
check_url(user_url)