from flask import request, session


def session_token_value():
    return f"snu-session-{abs(hash(request.remote_addr or 'anon'))}"


def ensure_session():
    session.permanent = True
    session.setdefault("session_token", session_token_value())
    session["message_count"] = int(session.get("message_count", 0)) + 1
    return session.get("session_token")


def initialize_session():
    session.clear()
    session.permanent = True
    session["session_token"] = session_token_value()
    session["message_count"] = 0
    return session.get("session_token")


def clear_session():
    session.clear()


def get_session_state():
    return {
        "session_token": session.get("session_token"),
        "is_active": True,
        "message_count": session.get("message_count", 0),
    }
