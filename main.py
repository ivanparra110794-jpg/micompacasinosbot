import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Tu token real de BotFather
TOKEN = 'tu_token_generado_en_telegram_por_botfather'

# Configura logging (opcional, para debug)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Función para menú principal
def menu_principal():
    keyboard = [
        [InlineKeyboardButton("🎰 Casinos 1 (Tercera Categoría 🕉️🕉️🕉️🕉️)", callback_data='casinos1')],
        [InlineKeyboardButton("🎲 Casinos 2 (Segunda Categoría 🕉️🕉️🕉️🕉️🕉️)", callback_data='casinos2')],
        [InlineKeyboardButton("♦️ Casinos 3 (Primera Categoría 🕉️🕉️🕉️🕉️)", callback_data='casinos3')],
        [InlineKeyboardButton("💎 Casinos con bonos sin depósito", callback_data='bonos_sin_deposito')],
        [InlineKeyboardButton("🧠 TIPS Y CONSEJOS", callback_data='tips')],
        [InlineKeyboardButton("ℹ️ Información adicional", callback_data='info_adicional')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Función para volver al principal
def volver_principal():
    keyboard = [[InlineKeyboardButton("🏠 Volver al menú principal", callback_data='principal')]]
    return InlineKeyboardMarkup(keyboard)

# Descripción y submenú Casinos 1 (con enlace corregido para MXwin)
async def handle_casinos1(query):
    desc = """Casinos 1 (Tercera Categoría 🕉️🕉️🕉️🕉️)

Ventajas: Sin verificación de identidad, bonos por registro en la mayoría, retiros solo con un depósito mínimo, bonos diarios, retiros en menos de 5 min.

Desventajas: No circula con regularidad en México ni tiene los permisos de SEGOB, puede desaparecer en cualquier momento con tus fondos dentro del casino. La creación de multi cuentas produce una auditoría al querer retirar donde pueden ser confiscados los bonos y ganancias sin importar si depositas o no, usando como referencia la dirección IP, cuenta bancaria de depósitos y dispositivo."""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Winuno", url='http://www.winuno33.com/?r=tqv7346')],
        [InlineKeyboardButton("Oknew", url='http://yaoqing.oknew6.com/?referralCode=sor8686')],
        [InlineKeyboardButton("Mxwin", url='http://www.mxwin22.com/?r=ure9788')],  # Enlace corregido aquí
        [InlineKeyboardButton("Mxfun", url='http://rich88.mxfun.co/?referralCode=gho3279')],
        [InlineKeyboardButton("Afun", url='https://afun.mx/?ch=550514&ic=119834756')],
        [InlineKeyboardButton("Mxn777", url='http://wealth88.mxn777.org/?referralCode=imp2070')],
        [InlineKeyboardButton("Vipganer", url='http://vip9999.vipganer29.vip/?referralCode=dhd1159')],
        [InlineKeyboardButton("1996bet", url='http://www.1906bet.com/?r=wnb9612')],
        [InlineKeyboardButton("Mtm7777", url='http://www.mtm777.net/?r=xfk2659')],
        [InlineKeyboardButton("Mx52", url='http://ppdjdj1.mx52b.com/?referralCode=mvl5501')],
        [InlineKeyboardButton("Mx58", url='https://quanzhandaili.mx58a.com/?referralCode=ngo1669')],
        [InlineKeyboardButton("Mxjuegos", callback_data='casino1_mxjuegos')],
        [InlineKeyboardButton("Z97", url='http://z97fb2.z97.com/?referralCode=lhy7633')],
        [InlineKeyboardButton("Km88", url='http://km88km.km88m5.org/?referralCode=tmk6962')],
        [InlineKeyboardButton("33bm", url='http://www.33bm.club/?r=kiv8032')],
        [InlineKeyboardButton("Bonos777", callback_data='casino1_bonos777')],
        [InlineKeyboardButton("Mexok", callback_data='casino1_mexok')],
        [InlineKeyboardButton("Billion", url='https://www.djsbhbs.com?fid=91905724')],
        [InlineKeyboardButton("1234club", url='http://www.1234club22.com/?r=nmb1994')],
        [InlineKeyboardButton("33mex", url='http://rich88.33mex3.com/?referralCode=ffy9274')],
        [InlineKeyboardButton("G9game", callback_data='casino1_g9game')],
        [InlineKeyboardButton("JuegosT", url='http://juegostvip008.20juegost.com/?referralCode=ckj0697')],
        [InlineKeyboardButton("Ko555", callback_data='casino1_ko555')],
        [InlineKeyboardButton("Mxbo777", callback_data='casino1_mxbo777')],
        [InlineKeyboardButton("Mxbgb", callback_data='casino1_mxbgb')],
        [InlineKeyboardButton("Luckylife", callback_data='casino1_luckylife')],
        [InlineKeyboardButton("Rajajoy", url='http://rajajoy1.rajajoy.org/?referralCode=cty1038')],
        [InlineKeyboardButton("Wz777", callback_data='casino1_wz777')],
        [InlineKeyboardButton("Yypg", callback_data='casino1_yypg')],
        [InlineKeyboardButton("Winvov", callback_data='casino1_winvov')],
        [InlineKeyboardButton("Winto", callback_data='casino1_winto')],
        [InlineKeyboardButton("Winmcn", callback_data='casino1_winmcn')],
        [InlineKeyboardButton("🔙 Volver", callback_data='principal')]
    ])
    await query.edit_message_text(desc + "\n\nElige un casino:", reply_markup=keyboard)

# Descripción y submenú Casinos 2
async def handle_casinos2(query):
    desc = """Casinos 2 (Segunda Categoría 🕉️🕉️🕉️🕉️🕉️)

Ventajas: Sin verificación de cuenta, rollover en los bonos, bono de bienvenida con depósito, retiros en menos de 10 min, traen claro quien patrocina y es el capitalista de los fondos.

Desventajas: Si no cumples cierta cantidad para retirar tus retiros no se procesan y tardan en rembolsarse a tu cuenta, no están regulados en México ni tienen licencias en SEGOB, pueden desaparecer con tus fondos en cualquier momento."""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Chillbet", callback_data='casino2_chillbet')],
        [InlineKeyboardButton("Granawin", url='https://granawin.mx/')],
        [InlineKeyboardButton("Hoy777", callback_data='casino2_hoy777')],
        [InlineKeyboardButton("Mexlucky", callback_data='casino2_mexlucky')],
        [InlineKeyboardButton("Casinuu", callback_data='casino2_casinuu')],
        [InlineKeyboardButton("Betmaster", url='https://betmaster.click?rsd=oDuRF7Dw')],
        [InlineKeyboardButton("🔙 Volver", callback_data='principal')]
    ])
    await query.edit_message_text(desc + "\n\nElige un casino:", reply_markup=keyboard)

# Descripción y submenú Casinos 3
async def handle_casinos3(query):
    desc = """Casinos 3 (Primera Categoría 🕉️🕉️🕉️🕉️)

Ventajas: Fondos 100% seguros, están totalmente regulados en México y con SEGOB, verificación KYC, retiros en menos de 24 horas solo las primeras veces después es en minutos, no desaparecerán con tus fondos en ningún momento a menos que así lo anuncien, no publicidad engañosa y la mayoría tienen códigos y bonos buenos que puedes cambiar por saldo real cumpliendo rollover y en otros todos los bonos son sin rollover como el caso de Novibet.

Desventajas: Prácticamente ninguna son casinos totalmente legal la única desventaja sería compartir los datos sensibles de identidad pero están totalmente regulados por SEGOB."""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Novibet", callback_data='casino3_novibet')],
        [InlineKeyboardButton("Luckydays", callback_data='casino3_luckydays')],
        [InlineKeyboardButton("🔙 Volver", callback_data='principal')]
    ])
    await query.edit_message_text(desc + "\n\nElige un casino:", reply_markup=keyboard)

# Descripción y submenú Bonos sin depósito
async def handle_bonos_sin_deposito(query):
    desc = """Casinos con bonos sin depósito

Estos casinos te otorgan un bono de regalo para que puedas probar los juegos de la plataforma, los bonos tienes varios términos y condiciones así como un rollover que es un requisito de apuestas necesarios que debes cumplir con el monto del bono para poder retirar ganancias obtenidas limitadas a las establecidas por el casino, todo viene especificado en cada casino, el bono en algunos casinos puede ser apostado en deportes o en slots ya es elección de cada usuario, se debe verificar número telefónico para recibirlo también debe ser solo una cuenta por IP, cuenta bancaria, nombre y dispositivo."""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("WINNER ($700)", callback_data='bono_winner')],
        [InlineKeyboardButton("CALIENTE ($1,000)", callback_data='bono_caliente')],
        [InlineKeyboardButton("STRENDUS ($500 o 50 giros)", callback_data='bono_strendus')],
        [InlineKeyboardButton("Foliati ($500)", callback_data='bono_foliati')],
        [InlineKeyboardButton("Mayapalace ($200)", callback_data='bono_mayapalace')],
        [InlineKeyboardButton("Spenbet ($200)", callback_data='bono_spenbet')],
        [InlineKeyboardButton("Betway ($200)", callback_data='bono_betway')],
        [InlineKeyboardButton("🔙 Volver", callback_data='principal')]
    ])
    await query.edit_message_text(desc + "\n\nElige un casino:", reply_markup=keyboard)

# Submenú TIPS Y CONSEJOS (sin "B1:", "B2:", etc.)
async def handle_tips(query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("RTP", callback_data='tip_rtp')],
        [InlineKeyboardButton("Volatilidad", callback_data='tip_volatilidad')],
        [InlineKeyboardButton("Tasa de éxito por cuenta", callback_data='tip_exito')],
        [InlineKeyboardButton("Multi cuentas", callback_data='tip_multi')],
        [InlineKeyboardButton("KYC", callback_data='tip_kyc')],
        [InlineKeyboardButton("Juegos mejor pagados con buen RTP", callback_data='tip_juegos')],
        [InlineKeyboardButton("Proveedores de juegos", callback_data='tip_proveedores')],
        [InlineKeyboardButton("Regresar al menú anterior", callback_data='tips_menu_anterior')],
        [InlineKeyboardButton("Regresar al inicio", callback_data='principal')]
    ])
    await query.edit_message_text("🧠 TIPS Y CONSEJOS\n\nElige un tema:", reply_markup=keyboard)

# Handler para /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '¡Hola! Bienvenido a Mi Compa Casinos Bot. Soy tu compa en casinos, hecho por jugadores para jugadores. Guías, bonos y tips para ganar como pro. 🎰💰 Elige una categoría en el menú abajo para empezar.',
        reply_markup=menu_principal()
    )

# Handler principal para botones
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == 'principal':
        await query.edit_message_text('🏠 Menú principal de Mi Compa Casinos Bot:', reply_markup=menu_principal())
    elif data == 'casinos1':
        await handle_casinos1(query)
    elif data == 'casinos2':
        await handle_casinos2(query)
    elif data == 'casinos3':
        await handle_casinos3(query)
    elif data == 'bonos_sin_deposito':
        await handle_bonos_sin_deposito(query)
    elif data == 'tips':
        await handle_tips(query)
    elif data == 'info_adicional':
        await query.edit_message_text('ℹ️ Información adicional\n\nPróximamente más info. ¿Tienes alguna pregunta específica? Usa /start para volver al menú.', reply_markup=volver_principal())
    # Placeholders para casinos sin enlace (genérico para todos)
    elif any(data.startswith(prefix) for prefix in ['casino1_', 'casino2_', 'casino3_', 'bono_']):
        nombre = data.split('_')[-1].title()
        await query.edit_message_text(f'{nombre}\n\nEnlace de invitación próximamente disponible. Contacta al admin para más detalles o info exclusiva.', reply_markup=volver_principal())
    # TIPS detallados - RTP dividido en partes para evitar límite de chars
    elif data == 'tip_rtp':
        # Parte 1: Intro y definición
        parte1 = """🧠 RTP (Return to Player) - Parte 1/3

Sabías que comprender el significado del RTP puede marcar la diferencia entre una simple apuesta y una jugada estratégica? Este indicador es la herramienta perfecta para elegir los juegos de casino más rentables y aumentar tus posibilidades de ganar.

¿Cuál es el significado de RTP en el casino?
El término RTP (Return to Player), que en español significa “retorno al jugador”, es un indicador clave en los juegos de casino online que representa el porcentaje teórico de dinero que se devuelve a los jugadores a lo largo del tiempo.

Por ejemplo, si un juego tiene un RTP del 96%, significa que, en promedio, el juego devolverá 96 unidades por cada 100 apostadas. El restante 4% representa la ganancia de la casa.

Ten en cuenta que este porcentaje no se aplica en cada sesión de juego, sino en múltiples jugadas, garantizando resultados a largo plazo. Aquí es donde se vuelve fundamental comprender la diferencia entre RTP teórico y RTP real.

RTP teórico
Es el porcentaje establecido por el desarrollador del juego. Se calcula mediante simulaciones que analizan millones de jugadas, reflejando el rendimiento esperado a largo plazo.

RTP real
Es el porcentaje que efectivamente se devuelve a los usuarios durante las jugadas reales. Puede variar significativamente del RTP teórico debido a la imprevisibilidad y la cantidad limitada de partidas realizadas.

Ejemplo RTP teórico
Una tragamonedas con RTP teórico del 95% debería devolver, en promedio, $95 por cada $100 apostados a lo largo del tiempo.

Ejemplo RTP real
En un solo día, un jugador podría ganar una gran suma en un juego con un RTP del 95%, haciendo que el RTP real durante ese período supere el teórico, o a la inversa."""
        await query.edit_message_text(parte1, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver a TIPS", callback_data='tips')],
            [InlineKeyboardButton("🏠 Volver al inicio", callback_data='principal')]
        ]))

        # Envía Parte 2: Rol y cálculo (nuevo mensaje)
        parte2 = """🧠 RTP - Parte 2/3

El RTP juega un papel fundamental en los casinos por varios motivos:
- Ayuda a los jugadores a elegir juegos más rentables;
- Facilita la comparación de juegos;
- Permite a los usuarios gestionar su bankroll y ajustar sus estrategias de manera efectiva.

Ahora que conoces el significado de RTP, te explicaremos cómo se calcula correctamente en un juego.

¿Cómo calcular el RTP de un juego?
Para calcular el RTP real de un juego y compararlo con el RTP teórico, se dividen las ganancias por la facturación.

Supongamos que, después de un mes de operación, una tragamonedas diseñada con un RTP teórico del 91.68% ha generado las siguientes cifras:

Facturación total (dinero apostado): $24,000,000 MXN
Ganancias totales distribuidas a los jugadores: $21,700,000 MXN

La fórmula para calcular el RTP real (RTP real = ganancias totales / facturación total) quedaría de la siguiente manera:

RTP real = $21,700,000 / $24,000,000 = 0.9042

En este caso, el retorno real de la tragamonedas es del 90.42% y está por debajo del porcentaje teórico del 91.68%. Esto se debe a variaciones a corto plazo en los resultados del juego, ya que la cifra indicada por el proveedor es una proyección basada en simulaciones de millones de jugadas.

No obstante, los slots no son los únicos juegos donde interviene el retorno al jugador. Títulos de casino en vivo como el blackjack y la ruleta también tienen RTP.

En el primero, el porcentaje suele ser muy alto, oscilando entre el 97% y el 99%, según las reglas específicas de la variante y de las decisiones del jugador. Por ejemplo, el Infinite Blackjack de Evolution tiene un RTP teórico del 99.47%.

El RTP de la ruleta, en cambio, depende de la variante:

Ruleta europea: tiene un RTP del 97.3% ya que solo cuenta con un único cero (0) como ventaja de la casa.
Ruleta americana: su RTP es menor, del 94.74%, debido a la inclusión de un doble cero (00), que aumenta la ganancia del sitio.
Ruleta francesa: también tiene un RTP del 97.3%, pero algunas reglas como “La Partage” o “En Prison” pueden aumentar las probabilidades de recuperar una parte de las apuestas en ciertas condiciones."""
        await query.message.reply_text(parte2)

        # Envía Parte 3: Consejos (nuevo mensaje)
        parte3 = """🧠 RTP - Parte 3/3

En todos los casos, es importante regresar al significado del RTP y recordar que es un promedio basado en muchas jugadas y no garantiza resultados específicos a corto plazo. Sin embargo, conocerlo te ayudará a tomar decisiones más informadas al elegir en qué juegos participar.

¿Cómo aprovechar el RTP en tus apuestas?
Comprender el significado del RTP es fundamental a la hora de optimizar tus apuestas en los juegos de casino en línea. A continuación te brindamos una serie de consejos para utilizar de manera estratégica este indicador:

- Elige juegos con un RTP alto, en lo posible superior al 96%;
- Comprende las reglas del juego y aplica una buena estrategia para mejorar tus resultados;
- Combina tus apuestas en juegos con alto RTP con las promociones ofrecidas por la casa de apuestas para ampliar tus oportunidades.

¡Usa esto para ganar más, compa! 🎯"""
        await query.message.reply_text(parte3)

    elif data == 'tip_volatilidad':
        await query.edit_message_text("Volatilidad\n\nInformación próximamente...", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver a TIPS", callback_data='tips')],
            [InlineKeyboardButton("🏠 Volver al inicio", callback_data='principal')]
        ]))
    elif data == 'tip_exito':
        await query.edit_message_text("Tasa de éxito por cuenta\n\nInformación próximamente...", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver a TIPS", callback_data='tips')],
            [InlineKeyboardButton("🏠 Volver al inicio", callback_data='principal')]
        ]))
    elif data == 'tip_multi':
        await query.edit_message_text("Multi cuentas\n\nInformación próximamente...", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver a TIPS", callback_data='tips')],
            [InlineKeyboardButton("🏠 Volver al inicio", callback_data='principal')]
        ]))
    elif data == 'tip_kyc':
        await query.edit_message_text("KYC\n\nInformación próximamente...", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver a TIPS", callback_data='tips')],
            [InlineKeyboardButton("🏠 Volver al inicio", callback_data='principal')]
        ]))
    elif data == 'tip_juegos':
        juegos_text = """Juegos mejor pagados con buen RTP

Top 10 tragamonedas con mejor RTP
Las 10 tragamonedas online con mejor RTP del mercado están disponibles en Betsson México. A continuación, te brindamos el listado completo con sus respectivos porcentajes para que te diviertas hoy mismo:

Tragamoneda          RTP
Blood Suckers        98%
Big Bad Wolf         97.34%
Motorhead            96.98%
Immortal Romance     96.9%
Spiñata Grande       96.8%
Fruit Spin           96.8%
Secrets of Christmas 96.7%
Rise Of Olympus      96.5%
Big Bass Vegas Double Down  96.5%
Fire Joker           96.15%"""
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver a TIPS", callback_data='tips')],
            [InlineKeyboardButton("🏠 Volver al inicio", callback_data='principal')]
        ])
        await query.edit_message_text(juegos_text, reply_markup=keyboard)
    elif data == 'tip_proveedores':
        await query.edit_message_text("Proveedores de juegos\n\nInformación próximamente...", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver a TIPS", callback_data='tips')],
            [InlineKeyboardButton("🏠 Volver al inicio", callback_data='principal')]
        ]))
    elif data == 'tips_menu_anterior':
        await handle_tips(query)

# Main
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Mi Compa Casinos Bot iniciado correctamente. Presiona Ctrl+C para detener.")
    app.run_polling()

if __name__ == '__main__':
    main()
