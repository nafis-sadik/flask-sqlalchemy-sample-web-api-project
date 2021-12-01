import os

from WebApplication import app

if __name__ == '__main__':
    port: int = int(os.environ.get("PORT", 5000))
    app.run('0.0.0.0', port=5000)