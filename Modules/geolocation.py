import requests

def get_geolocation(ip):

    url = f"http://ip-api.com/json/{ip}"

    try:
        response = requests.get(url,timeout=10)
        data = response.json()

        if data["status"] == "success":
            return {
                "success": True,
                "country": data.get("country"),
                "region": data.get("regionName"),
                "city": data.get("city"),
                "zip": data.get("zip"),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "timezone": data.get("timezone"),
                "isp": data.get("isp")
            }
        else:
            return {
                "success": False,
                "error": "Unable to fetch geolocation information : " + data.get("message")
            }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error fetching geolocation information: {str(e)}"
        }