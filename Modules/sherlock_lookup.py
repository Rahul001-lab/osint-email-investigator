import subprocess


def sherlock_lookup(username):

    try:
        result = subprocess.run(
        ["sherlock", username, "--timeout", "10", "--no-txt"],
         capture_output=True,
         text=True,
        timeout=600
        )

        output = result.stdout.strip()

        if output:
            return {
                "success": True,
                "sherlock_output": output
            }

        else:
            return {
                "success": False,
                "error": result.stderr.strip() or "Sherlock returned no results."
            }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Sherlock command timed out."
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Error running Sherlock: {str(e)}"
        }


if __name__ == "__main__":

    username = input("Enter Username: ")

    result = sherlock_lookup(username)

    if result["success"]:
        print(result["sherlock_output"])
    else:
        print(result["error"])