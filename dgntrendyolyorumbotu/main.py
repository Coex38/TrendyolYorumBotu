import requests

api_url = "http://127.0.0.1:5500/"


def test_api_with_url(url):
    try:
        response = requests.post(api_url, json={"url": url})
        if response.status_code == 200:
            data = response.json()
            print("API Response:", data)
        else:
            print("Error:", response.json())
    except Exception as e:
        print("An error occurred while connecting to the API:", e)


if __name__ == "__main__":
    test_url = ("https://www.trendyol.com/dgn/2020-erkek-snakers-ayakkabi-20y-p-42433050/yorumlar?boutiqueId=61"
                "&merchantId=107703&v=42")
    test_api_with_url(test_url)
