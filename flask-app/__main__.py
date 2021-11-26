import os

from app import app
from config import configs


def main():
    port = int(os.environ.get('PORT', configs['default_port']))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
