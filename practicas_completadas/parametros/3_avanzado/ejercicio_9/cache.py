"""Cache"""

import time


USER_CACHE: dict[int, dict] = {}
CACHE_TTL = 60


def get_cached_user(user_id: int):
    """get cache user"""
    cached = USER_CACHE.get(user_id)

    if not cached:
        return None

    if time.time() - cached["timestamp"] > CACHE_TTL:
        del USER_CACHE[user_id]
        return None

    return cached["data"]


def set_user_cache(user_id: int, data: dict):
    """set cache user"""
    USER_CACHE[user_id] = {"data": data, "timestamp": time.time()}
