from flask import Flask, render_template, request, redirect, flash
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesario para usar flash

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_TO = os.getenv('EMAIL_TO')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        asunto = f"Mensaje de {nombre} ({correo})"
        cuerpo = f"Nombre: {nombre}\nCorreo: {correo}\n\nMensaje:\n{mensaje}"

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(EMAIL_USER, EMAIL_PASS)
                smtp.sendmail(EMAIL_USER, EMAIL_TO, f"Subject: {asunto}\n\n{cuerpo}")
            flash('Mensaje enviado correctamente.', 'success')
        except Exception as e:
            print(e)
            flash('Error al enviar el mensaje.', 'danger')

        return redirect('/contacto')

    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
