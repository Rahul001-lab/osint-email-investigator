import subprocess

def sherlock_lookup(username):
    try:
        # Run the Sherlock command and capture the output
        result = subprocess.run(['sherlock', username], capture_output=True, text=True, timeout=60)

        if result.returncode == 0:
            return {
                "success": True,
                "sherlock_output": result.stdout
            }
        else:
            return {
                "success": False,
                "error": f"Sherlock command failed with return code {result.returncode}: {result.stderr}"
            }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Sherlock command timed out"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error running Sherlock: {str(e)}"
        }