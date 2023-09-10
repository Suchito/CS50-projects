def extensions():
    file = input("File name ").lower().strip()
    if ".gif" in file:
        print("image/gif")
    elif ".jpg" in file:
        print("image/jpeg")
    elif ".jpeg" in file:
        print("image/jpeg")
    elif ".zip" in file:
        print("application/zip")
    elif ".pdf" in file:
        print("application/pdf")
    elif ".png" in file:
        print("image/png")
    elif ".txt" in file:
        print("text/plain")
    else:
        print("application/octet-stream")

extensions()