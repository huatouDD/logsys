from flask import Flask

from logsys.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
