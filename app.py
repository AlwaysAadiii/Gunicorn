from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Reelogram'

# Health check endpoint
@app.route('/health')
def health_check():
    return 'OK'

if __name__ == "__main__":
    app.run()
