import requests

def github_lookup(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "github_info": {
                    "login": data.get("login"),
                    "name": data.get("name"),
                    "bio": data.get("bio"),
                    "company": data.get("company"),
                    "location": data.get("location"),
                    "public_repos": data.get("public_repos"),
                    "followers": data.get("followers"),
                    "following": data.get("following"),
                    "profile_url": data.get("html_url")
                }
            }

        elif response.status_code == 404:
            return {
                "success": False,
                "error": "User not found"
            }

        elif response.status_code == 403:
            return {
                "success": False,
                "error": "Rate limit exceeded or access denied"
            }

        elif response.status_code == 500:
            return {
                "success": False,
                "error": "Server Error"
            }

        else:
            return {
                "success": False,
                "error": f"Unexpected status code: {response.status_code}"
            }

    except requests.RequestException as e:
        return {
            "success": False,
            "error": f"Network error: {e}"
        }