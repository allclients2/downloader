import requests

url = "https://music.amazon.co.jp/config.json"


REQUIRED_ORDER = [
    "am-loader-experiment",
    "cwr_u",
    "session-id",
    "ubid-acbjp",
    "lc-acbjp",
    "sso-state-acbjp",
    "x-acbjp",
    "at-acbjp",
    "sess-at-acbjp",
    "sst-acbjp",
    "session-id-time",
    "am-token",
    "cwr_s",
    "session-token",
]

class Configs:

    @staticmethod
    def fetch_configs(cookieHeader: str):
        headers = {
            "Cookie": cookieHeader,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        }

        response = requests.get(
            url,
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()  # Parse JSON into Python dict
            
            # Access top-level fields
            # print("Field example:", data["field_name"])
            # Safely access (prevents KeyError)
            # print("Safe access:", data.get("field_name"))
            # Access nested fields
            # print("Nested value:", data["parent"]["child"])
            # Access list items
            # print("First item:", data["items"][0])
            # print("Item property:", data["items"][0]["name"])
            return data
        else:
            print("Error:", response.text)

# am-loader-experiment=***REMOVED***;
#  V cwr_u=***REMOVED***;
#  V session-id=***REMOVED***;
# ubid-acbjp=***REMOVED***;
# lc-acbjp=ja_JP;
# sso-state-acbjp=***REMOVED***;
# x-acbjp=***REMOVED***;
# at-acbjp=***REMOVED***;
# sess-at-acbjp=***REMOVED***;
# sst-acbjp=***REMOVED***;
#  V session-id-time=***REMOVED***;
# am-token=***REMOVED***;
#  V  cwr_s=***REMOVED***;
#  V session-token=***REMOVED***
