import base64
import urllib.parse

expected = (
    "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
    "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
    "JTM0JTVmJTY0JTMxJTM5JTM0JTM4JTY0JTM0JTY1"
)

# 1. Base64 decode
step1 = base64.b64decode(expected).decode()

# 2. URL decode
result = urllib.parse.unquote(step1)

print("picoCTF{"+ result+ "}")