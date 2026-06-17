import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import json


# ▶️ Token del bot (NO LO COMPARTAS EN PÚBLICO)
TOKEN = "8290258052:AAF6WfYLHuAR6tBHyqtuqWImPLQJFN2BcZk"
bot = telebot.TeleBot(TOKEN)

# 📁 Archivo donde se guardan los usuarios
DATA_FILE = "/data/usuarios.txt"

# 👑 Lista de administradores por ID de Telegram
ADMINS = [5504611412]  # Reemplaza con tu ID


# ===========================
# /start
# ===========================
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "SinUsername"
    registrado = False

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if str(user_id) in line:
                    registrado = True
                    break

    markup = InlineKeyboardMarkup()

    if not registrado:
        btn_registrar = InlineKeyboardButton("📥 Registrarme", callback_data="registrar")
        markup.add(btn_registrar)

    btn_creditos = InlineKeyboardButton("💰 Ver mis créditos", callback_data="ver_creditos")
    markup.add(btn_creditos)

    btn_mail = InlineKeyboardButton("BOTSPAM MAIL", callback_data="botspam_mail")
    btn_sms = InlineKeyboardButton("BOTSPAM SMS", callback_data="botspam_sms")
    markup.add(btn_mail, btn_sms)

    btn_comprar = InlineKeyboardButton("Comprar créditos", url="https://t.me/JUANPER33Z")
    markup.add(btn_comprar)

    bot.send_message(message.chat.id, "👋 ¡Hola! Usa los botones de abajo:", reply_markup=markup)


# ===========================
# 🔘 Botón: Registrarme
# ===========================
@bot.callback_query_handler(func=lambda call: call.data == "registrar")
def handle_register(call):
    bot.answer_callback_query(call.id)

    user_id = call.from_user.id
    username = call.from_user.username or "SinUsername"

    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").close()

    already_registered = False
    with open(DATA_FILE, "r") as f:
        for line in f:
            if str(user_id) in line:
                already_registered = True
                break

    if already_registered:
        bot.edit_message_text("📌 Ya estás registrado en el sistema.",
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id)
    else:
        with open(DATA_FILE, "a") as f:
            f.write(f"{user_id},{username},0\n")
        bot.edit_message_text("🎉 Registro completado. Tienes 0 créditos.",
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id)


# ===========================
# 🔘 Botón: Ver mis créditos
# ===========================
@bot.callback_query_handler(func=lambda call: call.data == "ver_creditos")
def handle_ver_creditos(call):
    bot.answer_callback_query(call.id)

    user_id = call.from_user.id
    encontrado = False

    if not os.path.exists(DATA_FILE):
        bot.send_message(call.message.chat.id, "⚠️ No hay usuarios registrados aún.")
        return

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 3 and str(user_id) == parts[0]:
                creditos = parts[2]
                bot.send_message(call.message.chat.id, f"💰 Tienes {creditos} créditos.")
                encontrado = True
                break

    if not encontrado:
        bot.send_message(call.message.chat.id, "❌ No estás registrado.")


# ===========================
# 🔘 Botón: BOTSPAM MAIL
# ===========================
@bot.callback_query_handler(func=lambda call: call.data == "botspam_mail")
def handle_botspam_mail(call):
    bot.answer_callback_query(call.id)

    user_id = call.from_user.id
    encontrado = False

    # Verificar si el usuario está registrado y tiene al menos 2 créditos
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if str(user_id) == parts[0]:
                    if len(parts) >= 3:
                        creditos = int(parts[2])
                        if creditos >= 2:
                            encontrado = True
                    break

    if not encontrado:
        bot.send_message(call.message.chat.id, "❌ Necesitas estar registrado y tener al menos 2 créditos.")
        return

    bot.send_message(call.message.chat.id, " Ingresa el mail al que quieres enviar el BOTSPAM MAIL:")
    bot.register_next_step_handler(call.message, procesar_botspam_mail)

# ===========================
#  Procesar número para BOTSPAM MAIL
# ===========================
def procesar_botspam_mail(message):
    email = message.text.strip()
    user_id = message.from_user.id

    # Validar formato mail básico
    if "@" not in email or "." not in email:
        bot.send_message(message.chat.id, "❌ Ingresa un correo válido.")
        return

    bot.send_message(
        message.chat.id,
        "🔢 ¿Cuántas veces deseas repetir el proceso de mail?\n\n"
        "⚠️ Recuerda: cada repetición cuesta 2 créditos."
    )
    bot.register_next_step_handler(message, procesar_repeticiones_mail, email)

# ===========================
# 🔢 Procesar cantidad de repeticiones (mail)
# ===========================
def procesar_repeticiones_mail(message, email):
    user_id = message.from_user.id

    try:
        repeticiones = int(message.text.strip())
        if repeticiones <= 0:
            bot.send_message(message.chat.id, "❌ Ingresa un número válido mayor a 0.")
            return
    except:
        bot.send_message(message.chat.id, "❌ Ingresa un número válido.")
        return

    costo_total = repeticiones * 2

    # Leer créditos del usuario
    creditos_actuales = 0
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 3 and str(user_id) == parts[0]:
                    creditos_actuales = int(parts[2])
                    break

    if creditos_actuales < costo_total:
        bot.send_message(
            message.chat.id,
            f"❌ No tienes suficientes créditos.\n"
            f"💰 Tienes {creditos_actuales}, pero necesitas {costo_total}."
        )
        return

    # Descontar créditos
    actualizar_creditos(user_id, -costo_total)

    bot.send_message(
        message.chat.id,
        f"💳 Se descontaron {costo_total} créditos. Iniciando BOTSPAM email {repeticiones} veces al mail {email}..."
    )

    ejecutar_proceso_mail(message.chat.id, email, repeticiones)

# ===========================
# 🚀 Ejecutar proceso mail
# ===========================
def ejecutar_proceso_mail(chat_id, email, repeats=1):
    bot.send_message(chat_id, "📡 Enviando Spam Mail...")

    for i in range(repeats):
        try:
            # Ejecuta el archivo email.py (debe estar en la misma carpeta)
            os.system(f'python mialspamer2026.py "{email}"')

            bot.send_message(chat_id, f"✅ MAIL {i + 1} completado.")
        except Exception as e:
            bot.send_message(chat_id, f"❌ Error en MAIL {i + 1}: {e}")

    bot.send_message(chat_id, "🎉 ¡Proceso de MAIL completado! Autor: @Juanper33z")

# ===========================
# 🔘 Botón: BOTSPAM SMS
# ===========================
@bot.callback_query_handler(func=lambda call: call.data == "botspam_sms")
def handle_botspam_sms(call):
    bot.answer_callback_query(call.id)

    user_id = call.from_user.id
    encontrado = False

    # Verificar si el usuario está registrado y tiene al menos 2 créditos
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if str(user_id) == parts[0]:
                    if len(parts) >= 3:
                        creditos = int(parts[2])
                        if creditos >= 2:
                            encontrado = True
                    break

    if not encontrado:
        bot.send_message(call.message.chat.id, "❌ Necesitas estar registrado y tener al menos 2 créditos.")
        return

    bot.send_message(call.message.chat.id, "📱 Ingresa el número al que quieres enviar el BOTSPAM SMS:")
    bot.register_next_step_handler(call.message, procesar_botspam_sms)


# ===========================
# 📱 Procesar número para BOTSPAM SMS
# ===========================
def procesar_botspam_sms(message):
    numero = message.text.strip()
    user_id = message.from_user.id

    # Validar formato numérico básico
    if not numero.isdigit() or len(numero) < 8:
        bot.send_message(message.chat.id, "❌ Ingresa un número válido (solo dígitos, mínimo 8).")
        return

    bot.send_message(
        message.chat.id,
        "🔢 ¿Cuántas veces deseas repetir el proceso de SMS?\n\n"
        "⚠️ Recuerda: cada repetición cuesta 2 créditos."
    )
    bot.register_next_step_handler(message, procesar_repeticiones_sms, numero)


# ===========================
# 🔢 Procesar cantidad de repeticiones (SMS)
# ===========================
def procesar_repeticiones_sms(message, numero):
    user_id = message.from_user.id

    try:
        repeticiones = int(message.text.strip())
        if repeticiones <= 0:
            bot.send_message(message.chat.id, "❌ Ingresa un número válido mayor a 0.")
            return
    except:
        bot.send_message(message.chat.id, "❌ Ingresa un número válido.")
        return

    costo_total = repeticiones * 2

    # Leer créditos del usuario
    creditos_actuales = 0
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 3 and str(user_id) == parts[0]:
                    creditos_actuales = int(parts[2])
                    break

    if creditos_actuales < costo_total:
        bot.send_message(
            message.chat.id,
            f"❌ No tienes suficientes créditos.\n"
            f"💰 Tienes {creditos_actuales}, pero necesitas {costo_total}."
        )
        return

    # Descontar créditos
    actualizar_creditos(user_id, -costo_total)

    bot.send_message(
        message.chat.id,
        f"💳 Se descontaron {costo_total} créditos. Iniciando BOTSPAM SMS {repeticiones} veces al número {numero}..."
    )

    ejecutar_proceso_sms(message.chat.id, numero, repeticiones)


# ===========================
# 🚀 Ejecutar proceso SMS
# ===========================
def ejecutar_proceso_sms(chat_id, numero, repeats=1):
    bot.send_message(chat_id, "📡 Enviando SMS...")

    for i in range(repeats):
        try:
            # Ejecuta el archivo SMS.py (debe estar en la misma carpeta)
            os.system(f'python SMS.py "{numero}"')

            bot.send_message(chat_id, f"✅ SMS {i + 1} completado.")
        except Exception as e:
            bot.send_message(chat_id, f"❌ Error en SMS {i + 1}: {e}")

    bot.send_message(chat_id, "🎉 ¡Proceso de SMS completado! Autor: @Juanper33z")

# ===========================
# /mis_creditos
# ===========================
@bot.message_handler(commands=["mis_creditos"])
def ver_creditos(message):
    user_id = message.from_user.id
    encontrado = False

    if not os.path.exists(DATA_FILE):
        bot.reply_to(message, "⚠️ No hay usuarios registrados aún.")
        return

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 3 and str(user_id) == parts[0]:
                creditos = parts[2]
                bot.reply_to(message, f"💰 Tienes {creditos} créditos.")
                encontrado = True
                break

    if not encontrado:
        bot.reply_to(message, "❌ No estás registrado. Usa /start para registrarte.")


# ===========================
# 🧮 Función para modificar créditos
# ===========================
def actualizar_creditos(user_id, cantidad):
    lineas = []
    actualizado = False

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 3 and str(user_id) == parts[0]:
                username = parts[1]
                creditos = int(parts[2]) + cantidad
                if creditos < 0:
                    creditos = 0
                lineas.append(f"{user_id},{username},{creditos}\n")
                actualizado = True
            else:
                lineas.append(line)

    if actualizado:
        with open(DATA_FILE, "w") as f:
            f.writelines(lineas)
    return actualizado



# ===========================
# /sumar_creditos y /restar_creditos (solo admins)
# ===========================
@bot.message_handler(commands=["sumar_creditos", "restar_creditos"])
def modificar_creditos(message):

    if message.from_user.id not in ADMINS:
        bot.reply_to(message, "⛔ No tienes permiso para usar este comando.")
        return

    partes = message.text.split()

    if len(partes) != 3:
        bot.reply_to(
            message,
            "❌ Uso:\n/sumar_creditos @usuario 10\n/sumar_creditos 5504611412 10"
        )
        return

    objetivo = partes[1].replace("@", "")

    try:
        cantidad = int(partes[2])
    except ValueError:
        bot.reply_to(message, "❌ Cantidad inválida.")
        return

    if message.text.startswith("/restar_creditos"):
        cantidad = -cantidad

    if not os.path.exists(DATA_FILE):
        bot.reply_to(message, "⚠️ No hay usuarios registrados aún.")
        return

    with open(DATA_FILE, "r") as f:
        lineas = f.readlines()

    nuevas_lineas = []
    actualizado = False

    for line in lineas:
        parts = line.strip().split(",")

        if len(parts) < 3:
            nuevas_lineas.append(line)
            continue

        uid, uname, creditos = parts

        if uid == objetivo or uname.lower() == objetivo.lower():

            nuevo_credito = max(0, int(creditos) + cantidad)

            nuevas_lineas.append(
                f"{uid},{uname},{nuevo_credito}\n"
            )

            actualizado = True

        else:
            nuevas_lineas.append(line)

    with open(DATA_FILE, "w") as f:
        f.writelines(nuevas_lineas)

    if actualizado:
        signo = "+" if cantidad > 0 else ""

        bot.send_message(
            message.chat.id,
            f"✅ Créditos actualizados ({signo}{cantidad})."
        )
    else:
        bot.send_message(
            message.chat.id,
            f"❌ Usuario o ID '{objetivo}' no encontrado."
        )


# ===========================
# /usuarios (solo admins)
# ===========================
@bot.message_handler(commands=["usuarios"])
def listar_usuarios(message):
    if message.from_user.id not in ADMINS:
        bot.reply_to(message, "⛔ No tienes permiso para ver la lista.")
        return

    if not os.path.exists(DATA_FILE):
        bot.reply_to(message, "⚠️ No hay usuarios registrados aún.")
        return

    texto = "📋 Usuarios registrados:\n"
    with open(DATA_FILE, "r") as f:
        for line in f:
            uid, uname, cred = line.strip().split(",")
            texto += f"• @{uname} - {cred} créditos\n"

    bot.reply_to(message, texto)

# ===========================
# /broadcast (solo admins)
# ===========================
@bot.message_handler(commands=["broadcast"])
def broadcast(message):

    if message.from_user.id not in ADMINS:
        bot.reply_to(message, "⛔ No tienes permiso para usar este comando.")
        return

    bot.reply_to(message, "✍️ Escribe el mensaje que deseas enviar a TODOS los usuarios registrados:")
    bot.register_next_step_handler(message, enviar_broadcast)


def enviar_broadcast(message):

    texto = message.text

    if not os.path.exists(DATA_FILE):
        bot.reply_to(message, "⚠️ No hay usuarios registrados.")
        return

    enviados = 0
    errores = 0

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")

            if len(parts) >= 1:
                user_id = parts[0]

                try:
                    bot.send_message(user_id, f"📢 MENSAJE DEL ADMIN\n\n{texto}")
                    enviados += 1
                except:
                    errores += 1

    bot.reply_to(
        message,
        f"✅ Mensaje enviado.\n\n📤 Enviados: {enviados}\n❌ Errores: {errores}"
    )

# ===========================
# /id
# ===========================
@bot.message_handler(commands=["id"])
def mostrar_id(message):

    user_id = message.from_user.id
    username = message.from_user.username or "SinUsername"

    bot.reply_to(
        message,
        f"🆔 Tu ID es:\n\n{user_id}\n\n👤 Usuario: @{username}"
    )
    
# ===========================
# 🟢 Iniciar el bot
# ===========================
print("🤖 Bot en marcha...")
bot.infinity_polling(skip_pending=True)
