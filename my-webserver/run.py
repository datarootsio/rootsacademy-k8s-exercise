import uvicorn
import os


PORT = int(os.getenv("PORT", "8000"))


def main():
    uvicorn.run("my_webserver.webserver_app:app", host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
