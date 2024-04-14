import requests

def fetch_photo(query):
    api_key = '1aF95swx5m4RhCBYc6AJWKgcBI4wzUVERvYLI684D9hi6UyAUJjBmrAd' 

    url = 'https://api.pexels.com/v1/search'
    headers = {
        'Authorization': api_key,
    }

    params = {
        'query': query,
        'per_page': 1,
    }

    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos', [])
        if photos:
            src_original_url = photos[0]['src']['original']
            return [0,src_original_url]
        else:
            return [1,"No photos found for the given query."]
    else:
        return [2,f"Error: {response.status_code}, {response.text}"]


# Example usage of the function
# query = 'Social Network'
# src_original_url = fetch_photo(query)
# if src_original_url:
#     print(f"Original URL for query '{query}': {src_original_url}")

 