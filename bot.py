import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# ▶️ Token del bot
TOKEN = "8290258052:AAF6WfYLHuAR6tBHyqtuqWImPLQJFN2BcZk"
bot = telebot.TeleBot(TOKEN)

# 📁 Ruta persistente para el archivo de usuarios
DATA_DIR = "/app/sspaaambot2026-volume"
DATA_FILE = os.path.join(DATA_DIR, "usuarios.txt")

# Garantizar que el directorio exista
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR, exist_ok=True)

# 👑 Lista de administradores
ADMINS = [5504611412]


# ===========================
# /start
# ===========================
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
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
        bot.send_message(call.message.chat.id, "📌 Ya estás registrado en el sistema.")
    else:
        with open(DATA_FILE, "a") as f:
            f.write(f"{user_id},{username},0\n")
        bot.send_message(call.message.chat.id, "🎉 Registro completado. Tienes 0 créditos.")


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
        bot.send_message(call.message.chat.id, "❌ No estás registrado. Usa /start para registrarte.")


# ===========================
# 🔘 Botón: BOTSPAM MAIL
# ===========================
@bot.callback_query_handler(func=lambda call: call.data == "botspam_mail")
def handle_botspam_mail(call):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    registrado = False
    creditos = 0

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 3 and str(user_id) == parts[0]:
                    registrado = True
                    creditos = int(parts[2])
                    break

    if not registrado:
        bot.send_message(call.message.chat.id, "❌ No estás registrado. Pulsa 'Registrarme' primero.")
        return

    if creditos < 2:
        bot.send_message(call.message.chat.id, f"❌ Necesitas al menos 2 créditos. Actualmente tienes: {creditos}.")
        return

    # Envía mensaje y usa esa respuesta para registrar el siguiente paso
    msg = bot.send_message(call.message.chat.id, "📧 Ingresa el mail al que quieres enviar el BOTSPAM MAIL:")
    bot.register_next_step_handler(msg, procesar_botspam_mail)


def procesar_botspam_mail(message):
    email = message.text.strip()
    if "@" not in email or "." not in email:
        bot.send_message(message.chat.id, "❌ Ingresa un correo válido.")
        return

    msg = bot.send_message(
        message.chat.id,
        "🔢 ¿Cuántas veces deseas repetir el proceso de mail?\n\n⚠️ Recuerda: cada repetición cuesta 2 créditos."
    )
    bot.register_next_step_handler(msg, procesar_repeticiones_mail, email)


def procesar_repeticiones_mail(message, email):
    user_id = message.from_user.id
    try:
        repeticiones = int(message.text.strip())
        if repeticiones <= 0:
            bot.send_message(message.chat.id, "❌ Ingresa un número mayor a 0.")
            return
    except ValueError:
        bot.send_message(message.chat.id, "❌ Ingresa un número entero válido.")
        return

    costo_total = repeticiones * 2
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
            f"❌ Créditos insuficientes.\nTienes {creditos_actuales}, pero necesitas {costo_total}."
        )
        return

    actualizar_creditos(user_id, -costo_total)
    bot.send_message(
        message.chat.id,
        f"💳 Se descontaron {costo_total} créditos. Iniciando BOTSPAM email {repeticiones} veces a {email}..."
    )
    ejecutar_proceso_mail(message.chat.id, email, repeticiones)


def ejecutar_proceso_mail(chat_id, email, repeats=1):
    bot.send_message(chat_id, "📡 Enviando Spam Mail...")
    for i in range(repeats):
        try:
            os.system(f'python mialspamer2026.py "{email}"')
            bot.send_message(chat_id, f"✅ MAIL {i + 1} completado.")
        except Exception as e:
            bot.send_message(chat_id, f"❌ Error en MAIL {i + 1}: {e}")
    bot.send_message(chat_id, "🎉 ¡Proceso completado!")


# ===========================
# 🔘 Botón: BOTSPAM SMS
# ===========================
@bot.callback_query_handler(func=lambda call: call.data == "botspam_sms")
def handle_botspam_sms(call):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    registrado = False
    creditos = 0

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 3 and str(user_id) == parts[0]:
                    registrado = True
                    creditos = int(parts[2])
                    break

    if not registrado:
        bot.send_message(call.message.chat.id, "❌ No estás registrado. Pulsa 'Registrarme' primero.")
        return

    if creditos < 2:
        bot.send_message(call.message.chat.id, f"❌ Necesitas al menos 2 créditos. Actualmente tienes: {creditos}.")
        return

    msg = bot.send_message(call.message.chat.id, "📱 Ingresa el número al que quieres enviar el BOTSPAM SMS:")
    bot.register_next_step_handler(msg, procesar_botspam_sms)


def procesar_botspam_sms(message):
    numero = message.text.strip()
    if not numero.isdigit() or len(numero) < 8:
        bot.send_message(message.chat.id, "❌ Ingresa un número válido (mínimo 8 dígitos).")
        return

    msg = bot.send_message(
        message.chat.id,
        "🔢 ¿Cuántas veces deseas repetir el proceso de SMS?\n\n⚠️ Recuerda: cada repetición cuesta 2 créditos."
    )
    bot.register_next_step_handler(msg, procesar_repeticiones_sms, numero)


def procesar_repeticiones_sms(message, numero):
    user_id = message.from_user.id
    try:
        repeticiones = int(message.text.strip())
        if repeticiones <= 0:
            bot.send_message(message.chat.id, "❌ Ingresa un número mayor a 0.")
            return
    except ValueError:
        bot.send_message(message.chat.id, "❌ Ingresa un número entero válido.")
        return

    costo_total = repeticiones * 2
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
            f"❌ Créditos insuficientes.\nTienes {creditos_actuales}, pero necesitas {costo_total}."
        )
        return

    actualizar_creditos(user_id, -costo_total)
    bot.send_message(
        message.chat.id,
        f"💳 Se descontaron {costo_total} créditos. Iniciando BOTSPAM SMS {repeticiones} veces a {numero}..."
    )
    ejecutar_proceso_sms(message.chat.id, numero, repeticiones)


def ejecutar_proceso_sms(chat_id, numero, repeats=1):
    bot.send_message(chat_id, "📡 Enviando SMS...")
    for i in range(repeats):
        try:
            os.system(f'python SMS.py "{numero}"')
            bot.send_message(chat_id, f"✅ SMS {i + 1} completado.")
        except Exception as e:
            bot.send_message(chat_id, f"❌ Error en SMS {i + 1}: {e}")
    bot.send_message(chat_id, "🎉 ¡Proceso completado!")


# ===========================
# Utilidades de Créditos y Comandos Admin
# ===========================
def actualizar_creditos(user_id, cantidad):
    if not os.path.exists(DATA_FILE):
        return False
    lineas = []
    actualizado = False
    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 3 and str(user_id) == parts[0]:
                username = parts[1]
                creditos = max(0, int(parts[2]) + cantidad)
                lineas.append(f"{user_id},{username},{creditos}\n")
                actualizado = True
            else:
                lineas.append(line)
    if actualizado:
        with open(DATA_FILE, "w") as f:
            f.writelines(lineas)
    return actualizado


@bot.message_handler(commands=["sumar_creditos", "restar_creditos"])
def modificar_creditos(message):
    if message.from_user.id not in ADMINS:
        bot.reply_to(message, "⛔ No tienes permiso.")
        return

    partes = message.text.split()
    if len(partes) != 3:
        bot.reply_to(message, "❌ Uso:\n/sumar_creditos @usuario 10\n/sumar_creditos ID 10")
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
            nuevas_lineas.append(f"{uid},{uname},{nuevo_credito}\n")
            actualizado = True
        else:
            nuevas_lineas.append(line)

    with open(DATA_FILE, "w") as f:
        f.writelines(nuevas_lineas)

    if actualizado:
        bot.send_message(message.chat.id, f"✅ Créditos actualizados correctamente.")
    else:
        bot.send_message(message.chat.id, f"❌ Usuario u ID '{objetivo}' no encontrado.")


@bot.message_handler(commands=["mis_creditos"])
def ver_creditos_cmd(message):
    handle_ver_creditos_msg(message)

def handle_ver_creditos_msg(message):
    user_id = message.from_user.id
    if not os.path.exists(DATA_FILE):
        bot.reply_to(message, "⚠️ No hay usuarios registrados.")
        return

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 3 and str(user_id) == parts[0]:
                bot.reply_to(message, f"💰 Tienes {parts[2]} créditos.")
                return
    bot.reply_to(message, "❌ No estás registrado.")


@bot.message_handler(commands=["usuarios"])
def listar_usuarios(message):
    if message.from_user.id not in ADMINS:
        return
    if not os.path.exists(DATA_FILE):
        bot.reply_to(message, "⚠️ Sin usuarios.")
        return
    texto = "📋 Usuarios registrados:\n"
    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                texto += f"• @{parts[1]} ({parts[0]}) - {parts[2]} créditos\n"
    bot.reply_to(message, texto)


@bot.message_handler(commands=["id"])
def mostrar_id(message):
    bot.reply_to(message, f"🆔 Tu ID: {message.from_user.id}\n👤 Usuario: @{message.from_user.username}")


# ===========================
# 🟢 Iniciar el bot
# ===========================
print("🤖 Bot en marcha...")
bot.remove_webhook()
bot.infinity_polling(skip_pending=True)
