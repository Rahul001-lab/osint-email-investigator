import requests

def gitlab_lookup(username):

    url = f"https://gitlab.com/api/v4/users?username={username}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200 and data:
            user_data = data[0]  # Assuming the first result is the most relevant
            return {
                "success": True,
                "gitlab_info": {
                    "id": user_data.get("id"),
                    "username": user_data.get("username"),
                    "name": user_data.get("name"),
                    "state": user_data.get("state"),
                    "avatar_url": user_data.get("avatar_url"),
                    "web_url": user_data.get("web_url")
                }
            }

        else:
            return {
                 "success": False,
                  "error": "User not found"
                   }

    except Exception as e:
        return {
            "success": False,
            "error": f"Error fetching username information: {str(e)}"
        }