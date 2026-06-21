import sqlite3, os
from dotenv import load_dotenv
from flask import Flask, request, render_template, session

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("butao.html")

@app.route("/entrada/notas")
def entrada_notas():
    if not session.get("email"):
        return render_template("login.html", message="Faça login para acessar suas notas.")
    conn = sqlite3.connect("bancodados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notas WHERE nome = ?", (session["username"],))
    notas = cursor.fetchall()
    conn.close()
    return render_template("notas.html", username=session["username"], notas=notas)

@app.route("/admin")
def admin():
    session["username"] = session.get("username", "")
    conn = sqlite3.connect("bancodados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notas")
    notas = cursor.fetchall()
    if session.get("email") == "admin@admin.com":
        return render_template("admin.html", notas=notas)
    return render_template("login.html", message="Acesso restrito a administradores.", username=session["username"])

@app.route("/admin/users")
def admin_users():
    if session.get("email") != "admin@admin.com":
        return render_template("login.html", message="Acesso restrito a administradores.")
    conn = sqlite3.connect("bancodados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template("admin_users.html", usuarios=usuarios)

@app.route("/admin/users/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    conn = sqlite3.connect("bancodados.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (user_id,)
    )
    cursor.execute("DELETE FROM notas WHERE id = ?", (user_id,))
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conn.commit()
    conn.close()

    return render_template("admin_users.html", message="Usuário excluído com sucesso!", usuarios=usuarios)

@app.route("/admin/users/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    conn = sqlite3.connect("bancodados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
    usuario = cursor.fetchone()
    conn.close()
    return render_template("admin_users_edit.html", user_id=user_id, usuario=usuario)

@app.route("/admin/users/update/<int:user_id>", methods=["POST"])
def update_user(user_id):
    name = request.form.get("nome")
    email = request.form.get("email")
    password = request.form.get("senha").strip()
    if password == "":
        conn = sqlite3.connect("bancodados.db")
        cursor = conn.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE id = ?", (user_id,))
        password = cursor.fetchone()[0]
        conn.close()

    conn = sqlite3.connect("bancodados.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?", (name, email, password, user_id))
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.commit()
    conn.close()

    return render_template("admin_users.html", message="Usuário atualizado com sucesso!", usuarios=usuarios)

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

@app.route("/cadastrar/submited", methods=["POST"])
def cadastrar_submited():
    name = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    conn = sqlite3.connect("bancodados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    if cursor.fetchone():
        conn.close()
        return render_template("cadastrar.html", message="Email já cadastrado!")
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    conn.close()

    return render_template("login.html", message="Usuário cadastrado com sucesso!")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login/submited", methods=["POST"])
def login_submited():
    email = request.form.get("email")
    password = request.form.get("password")

    conn = sqlite3.connect("bancodados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        session["username"] = result[1]
        session["email"] = result[2]
        conn = sqlite3.connect("bancodados.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notas WHERE nome = ?", (session["username"],))
        notas = cursor.fetchall()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()
        if session["email"] == "admin@admin.com":
            conn = sqlite3.connect("bancodados.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notas")
            notas = cursor.fetchall()
            conn.close()
            return render_template("admin.html", username=session["username"], notas=notas, usuarios=usuarios)
        return render_template("entrada.html", username=session["username"], notas=notas)
    return render_template("login.html", message="Email ou senha incorretos!")
    
app.run(debug=True)
