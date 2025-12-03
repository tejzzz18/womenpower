from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "replace_this_in_production"

# Inject year globally
@app.context_processor
def inject_year():
    return {"current_year": datetime.utcnow().year}


# ---------------------------------------------------------
#                ENGLISH ROUTES
# ---------------------------------------------------------

@app.route("/")
def home():
    return render_template("ehome.html")


@app.route("/articles")
def articles():
    return render_template("earticle.html")


@app.route("/articles/physical")
def physical_article():
    return render_template("physical.html")


@app.route("/articles/digital")
def digital_article():
    # your screenshot shows "d.html" used in earticle.html
    return render_template("d.html")


@app.route("/articles/emotional")
def emotional_article():
    return render_template("emotional.html")


@app.route("/about")
def about():
    return render_template("eaboutus.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("Please fill in all required fields.", "error")
            return redirect(url_for("contact"))

        flash("Your message has been received!", "success")
        return redirect(url_for("contact"))

    return render_template("econtact.html")


@app.route("/help")
def help_page():
    return render_template("ehelp.html")


@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        flash("Report submitted successfully.", "success")
        return redirect(url_for("report"))

    return render_template("ereport.html")


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


@app.route("/stories")
def stories():
    return render_template("ytvideos.html")


@app.route("/selfdefence")
def selfdefence():
    return render_template("evideos.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        flash("Thank you for your feedback!", "success")
        return redirect(url_for("feedback"))

    return render_template("efeedback.html")


# ---------------------------------------------------------
#                KANNADA ROUTES
# ---------------------------------------------------------

@app.route("/kannada")
def kannada_home():
    return render_template("khome.html")


@app.route("/karticle")
def karticle():
    return render_template("karticle.html")


@app.route("/kabout")
def kabout():
    return render_template("kaboutus.html")


@app.route("/kcontact", methods=["GET", "POST"])
def kcontact():
    if request.method == "POST":
        flash("ನಿಮ್ಮ ಸಂದೇಶವನ್ನು ಸ್ವೀಕರಿಸಲಾಗಿದೆ!", "success")
        return redirect(url_for("kcontact"))
    return render_template("kcontact.html")


@app.route("/khelp")
def khelp():
    return render_template("khelp.html")


@app.route("/kreport", methods=["GET", "POST"])
def kreport():
    if request.method == "POST":
        flash("ಘಟನೆ ಯಶಸ್ವಿಯಾಗಿ ಸಲ್ಲಿಸಲಾಗಿದೆ.", "success")
        return redirect(url_for("kreport"))
    return render_template("kreport.html")


@app.route("/kselfdefence")
def kselfdefence():
    return render_template("kvideos.html")


@app.route("/kfeedback", methods=["GET", "POST"])
def kfeedback():
    if request.method == "POST":
        flash("ಪ್ರತಿಕ್ರಿಯೆಗೆ ಧನ್ಯವಾದಗಳು!", "success")
        return redirect(url_for("kfeedback"))
    return render_template("kfeedback.html")


# ---------------------------------------------------------
#            START APP
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
