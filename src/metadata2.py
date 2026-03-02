import json
import requests

url = "https://music.amazon.co.jp/embed/B0BQ71QYD6"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "text/plain;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
}


deeplink_obj = {
    "interface": "DeeplinkInterface.v1_0.DeeplinkClientInformation",
    "deeplink": "/albums/B0BQ6X67MS"
}

authentication_obj = {
    "interface": "ClientAuthenticationInterface.v1_0.ClientTokenElement",
    "accessToken": "***REMOVED***"
}

csrf_obj = {
    "interface": "CSRFInterface.v1_0.CSRFHeaderElement",
    "token": "LKH9oof4Gnb+6JYCzUUTI5bNzZC9M5nN7jE/pYGk/gk=",
    "timestamp": "1772419148",
    "rndNonce": "1901901484"
}

headers_obj = {
    "x-amzn-authentication": json.dumps({
        "interface":"ClientAuthenticationInterface.v1_0.ClientTokenElement",
        "accessToken": "***REMOVED***"
    }),
    "x-amzn-device-model": "WEBPLAYER",
    "x-amzn-device-width": "1920",
    "x-amzn-device-family": "WebPlayer",
    "x-amzn-device-id": "***REMOVED***",
    "x-amzn-user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "x-amzn-session-id": "357-9334536-5583055",
    "x-amzn-device-height": "1080",
    "x-amzn-request-id": "2c082208-441a-431b-8983-7eeaf7143a11",
    "x-amzn-device-language": "en_US",
    "x-amzn-currency-of-preference": "JPY",
    "x-amzn-os-version": "1.0",
    "x-amzn-application-version": "1.0.9527.0",
    "x-amzn-device-time-zone": "America/New_York",
    "x-amzn-timestamp": "1772419149227",
    "x-amzn-csrf": json.dumps({
        "interface": "CSRFInterface.v1_0.CSRFHeaderElement",
        "token": "LKH9oof4Gnb+6JYCzUUTI5bNzZC9M5nN7jE/pYGk/gk=",
        "timestamp": "1772419148",
        "rndNonce": "1901901484"
    }),
    "x-amzn-music-domain": "music.amazon.co.jp",
    "x-amzn-referer": "",
    "x-amzn-affiliate-tags": "",
    "x-amzn-ref-marker": "dm_sh_lsTk3BhcFKjVwRYoJgsPoTG1Y",
    "x-amzn-page-url": "https://music.amazon.co.jp/albums/B0BQ6X67MS?marketplaceId=A1VC38T7YXB528&musicTerritory=JP&ref=dm_sh_cRsy07bhxIFU5uglM182qQSy9",
    "x-amzn-weblab-id-overrides": "",
    "x-amzn-video-player-token": "",
    "x-amzn-feature-flags": "hd-supported,uhd-supported",
    "x-amzn-has-profile-id": "true",
    "x-amzn-age-band": ""
}

payload = {
    "deeplink": json.dumps(deeplink_obj),
    "headers": json.dumps(headers_obj)
}


response = requests.post(
    url,
    headers=headers,
)

print("payload:", payload)

with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Response saved to response.txt")