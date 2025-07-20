def main():
        name = input("File name: ").lower()
        array = name.split(".")
        if array[1] == "gif":
                print("image/gif")
        elif array[1] == "jpg" or array[1] == "jpeg":
                print("image/jpeg")
        elif array[1] == "png":
                print("image/png")
        elif array[1] == "txt":
                print("text/plain")
        elif array[1] == "pdf":
                print("application/pdf")
        elif array[1] == "zip":
                print("application/zip")
        else:
                print("application/octet-stream")

main()
