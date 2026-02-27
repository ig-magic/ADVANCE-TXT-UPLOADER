from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Txt Bot</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', sans-serif;
            }

            body {
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364);
                background-size: 400% 400%;
                animation: gradientBG 10s ease infinite;
                color: white;
            }

            @keyframes gradientBG {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }

            .card {
                backdrop-filter: blur(15px);
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 0 30px rgba(0,0,0,0.4);
                width: 350px;
                animation: fadeIn 1.5s ease-in-out;
            }

            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(20px);}
                to {opacity: 1; transform: translateY(0);}
            }

            h1 {
                font-size: 32px;
                margin-bottom: 10px;
            }

            p {
                opacity: 0.8;
                margin-bottom: 20px;
            }

            .btn {
                display: inline-block;
                padding: 12px 25px;
                border-radius: 30px;
                text-decoration: none;
                font-weight: bold;
                color: white;
                margin: 8px;
                transition: 0.3s;
            }

            .start {
                background: linear-gradient(45deg, #ff416c, #ff4b2b);
                box-shadow: 0 0 15px rgba(255,75,43,0.6);
            }

            .channel {
                background: linear-gradient(45deg, #1e90ff, #00c6ff);
                box-shadow: 0 0 15px rgba(0,198,255,0.6);
            }

            .btn:hover {
                transform: scale(1.08);
                box-shadow: 0 0 25px rgba(255,255,255,0.5);
            }

            .status {
                margin-top: 15px;
                font-size: 14px;
                color: #00ffae;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🤖  Bot</h1>
            <p>Premium Telegram Automation Bot</p>
            
            <a href="https://t.me/YOUR_BOT_USERNAME" class="btn start">🚀 Start Bot</a>
            <a href="https://t.me/Magicxbots" class="btn channel">📢 Join Channel</a>
            
            <div class="status">
                ● Bot Status: Online
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
