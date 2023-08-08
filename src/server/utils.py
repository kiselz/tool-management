"""Utility functions for server"""

def check_json(js, *keys):
    """
    Check whether all keys are in js

    Parameters:
    js (dict): JSON object
    *keys (list[str]): keys that have to be in js

    Returns:
    error message if the key is not in js
    True if all keys are in js
    """
    for key in keys:
        if key not in js:
            return {
                "status": "error",
                "message": f"Expected {key} key in JSON"
            }
    return True