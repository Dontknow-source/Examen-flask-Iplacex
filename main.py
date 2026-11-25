from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/ejercicio1", methods=["GET", "POST"])
def Ejer1():
    resultado = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros = int(request.form["tarros"])

        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro

        if edad < 18:
            porc_descuento = 0
        elif edad <= 30:
            porc_descuento = 0.15
        else:
            porc_descuento = 0.25

        monto_descuento = total_sin_descuento * porc_descuento
        total_a_pagar = total_sin_descuento - monto_descuento

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "monto_descuento": monto_descuento,
            "total_a_pagar": total_a_pagar,
        }
    return render_template("Ejer1.html", resultado=resultado)
@app.route("/ejercicio2", methods=["GET", "POST"])
def Ejer2():
    mensaje = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        contrasena = request.form["contrasena"]

        if nombre == "juan" and contrasena == "admin":
            mensaje = "Bienvenido administrador juan"
        elif nombre == "pepe" and contrasena == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("Ejer2.html", mensaje=mensaje)
if __name__ == '__main__':
    app.run(debug=True)