from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    from app.routes.chatbot import chatbot_bp
    app.register_blueprint(chatbot_bp)

    return app
