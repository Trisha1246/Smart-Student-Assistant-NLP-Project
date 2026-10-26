from flask import Flask, render_template, request, jsonify, session, redirect

from app.chatbot import get_response
from app.database import (
    init_database,
    create_user,
    verify_user,
    get_user_by_id,
    save_chat_history,
    get_quiz_results,
    get_study_plans,
    get_chat_history,
    update_user_name,
    update_user_password
)


app = Flask(__name__)

app.secret_key = "smart-student-assistant-secret-key"

init_database()


@app.route("/")
def home():

    if "user_id" not in session:
        return redirect("/auth")

    return render_template("index.html")


@app.route("/auth")
def auth():

    if "user_id" in session:
        return redirect("/")

    return render_template("auth.html")


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip().lower()
    password = str(data.get("password", ""))


    if not name or not email or not password:

        return jsonify({
            "success": False,
            "message": "Please fill in all fields."
        }), 400


    if len(password) < 6:

        return jsonify({
            "success": False,
            "message": "Password must contain at least 6 characters."
        }), 400


    created = create_user(
        name,
        email,
        password
    )


    if not created:

        return jsonify({
            "success": False,
            "message": "An account with this email already exists."
        }), 409


    return jsonify({
        "success": True,
        "message": "Account created successfully."
    })


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json(silent=True) or {}

    email = str(data.get("email", "")).strip().lower()
    password = str(data.get("password", ""))


    if not email or not password:

        return jsonify({
            "success": False,
            "message": "Please enter email and password."
        }), 400


    user = verify_user(
        email,
        password
    )


    if user is None:

        return jsonify({
            "success": False,
            "message": "Invalid email or password."
        }), 401


    session.clear()

    session["user_id"] = user["id"]
    session["user_name"] = user["name"]
    session["user_email"] = user["email"]


    return jsonify({
        "success": True,
        "message": "Login successful."
    })


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/auth")


@app.route("/chat", methods=["POST"])
def chat():

    if "user_id" not in session:

        return jsonify({
            "response": "Please login first."
        }), 401


    data = request.get_json(silent=True) or {}

    question = str(
        data.get("question", "")
    ).strip()


    if not question:

        return jsonify({
            "response": "Please enter a question."
        }), 400


    context = {

        "last_topic":
            session.get("last_topic"),

        "last_question":
            session.get("last_question"),

        "last_subject":
            session.get("last_subject")
    }


    intent, confidence, response = get_response(
        question,
        context
    )


    session["last_topic"] = context.get(
        "last_topic",
        str(intent)
    )

    session["last_question"] = context.get(
        "last_question",
        question
    )

    session["last_subject"] = context.get(
        "last_subject",
        ""
    )


    save_chat_history(

        session["user_id"],

        question,

        response,

        str(intent),

        float(confidence)
    )


    session.modified = True


    return jsonify({

        "response": response,

        "intent": str(intent),

        "confidence": float(confidence)

    })


@app.route("/profile")
def profile():

    if "user_id" not in session:
        if request.accept_mimetypes.best_match(["application/json", "text/html"]) == "text/html":
            return redirect("/auth")
        return jsonify({
            "success": False,
            "message": "Please login first."
        }), 401

    user = get_user_by_id(session["user_id"])
    if user is None:
        session.clear()
        if request.accept_mimetypes.best_match(["application/json", "text/html"]) == "text/html":
            return redirect("/auth")
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    if request.accept_mimetypes.best_match(["application/json", "text/html"]) == "text/html":
        try:
            quizzes = get_quiz_results(user["id"])
            total_quizzes = len(quizzes)
            total_score = sum(q["score"] for q in quizzes)
            total_possible = sum(q["total_questions"] for q in quizzes)
            avg_score = round((total_score / total_possible) * 100) if total_possible > 0 else 0
        except Exception:
            total_quizzes = 0
            avg_score = 0

        try:
            plans = get_study_plans(user["id"])
            total_plans = len(plans)
            completed_plans = sum(1 for p in plans if p["status"] == "completed")
        except Exception:
            total_plans = 0
            completed_plans = 0

        try:
            chats = get_chat_history(user["id"])
            total_chats = len(chats)
        except Exception:
            total_chats = 0

        stats = {
            "total_quizzes": total_quizzes,
            "avg_score": avg_score,
            "total_plans": total_plans,
            "completed_plans": completed_plans,
            "total_chats": total_chats,
            "recent_quizzes": quizzes[:5] if quizzes else [],
            "recent_plans": plans[:5] if plans else [],
            "recent_chats": chats[:5] if chats else []
        }
        return render_template("profile.html", user=user, stats=stats)

    return jsonify({
        "success": True,
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "created_at": user["created_at"]
    })




@app.route("/update-profile", methods=["POST"])
def update_profile():
    if "user_id" not in session:
        return jsonify({"success": False, "message": "Please login first."}), 401

    data = request.get_json(silent=True) or {}
    new_name = str(data.get("name", "")).strip()
    if not new_name:
        return jsonify({"success": False, "message": "Name cannot be empty."}), 400

    ok, msg = update_user_name(session["user_id"], new_name)
    if ok:
        session["user_name"] = new_name
        return jsonify({"success": True, "message": msg, "name": new_name})
    return jsonify({"success": False, "message": msg}), 400


@app.route("/change-password", methods=["POST"])
def change_password():
    if "user_id" not in session:
        return jsonify({"success": False, "message": "Please login first."}), 401

    data = request.get_json(silent=True) or {}
    current_password = str(data.get("current_password", ""))
    new_password = str(data.get("new_password", ""))

    if not current_password or not new_password:
        return jsonify({"success": False, "message": "Please fill in all password fields."}), 400

    ok, msg = update_user_password(session["user_id"], current_password, new_password)
    if ok:
        return jsonify({"success": True, "message": msg})
    return jsonify({"success": False, "message": msg}), 400


@app.route("/api/profile")
def api_profile():

    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please login first."
        }), 401

    user = get_user_by_id(session["user_id"])
    if user is None:
        session.clear()
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    return jsonify({
        "success": True,
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "created_at": user["created_at"]
    })


if __name__ == "__main__":

    app.run(
        debug=True
    )