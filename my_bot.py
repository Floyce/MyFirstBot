from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters
import random

# Lists of jokes and facts
JOKES = [
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? It was two-tired.",
    "Why don’t eggs tell jokes? They might crack up.",
    "What do you call cheese that isn't yours? Nacho cheese.",
]
FACTS = [
    "A bolt of lightning is five times hotter than the surface of the sun.",
    "Sharks existed before trees were even a thing.",
    "Bananas are naturally radioactive due to their potassium content.",
    "Koalas have fingerprints that are almost identical to humans.",
    "Wombat poop is cube-shaped to prevent it from rolling away.",
]

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create inline buttons to guide the user
    keyboard = [
        [InlineKeyboardButton("Tell me a joke", callback_data='joke')],
        [InlineKeyboardButton("Share a fun fact", callback_data='fact')],
        [InlineKeyboardButton("How can you help?", callback_data='help')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Welcome message with inline buttons
    await update.message.reply_text(
        "Heeyy Lovelyy! You made it! 🌟 I'm your Mood Booster Bot.\n"
        "Do you need help with commands? Choose an option below to get started!",
        reply_markup=reply_markup
    )

# Handle button presses
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the button press

    if query.data == "joke":
        joke = random.choice(JOKES)
        await query.message.reply_text(f"Here’s a joke for you: {joke}")
    elif query.data == "fact":
        fact = random.choice(FACTS)
        await query.message.reply_text(f"Fun fact: {fact}")
    elif query.data == "help":
        await query.message.reply_text(
            "Here’s how I can help:\n"
            "🎭 `/joke` - Get a random joke.\n"
            "🔎 `/fact` - Learn a fun fact.\n"
            "🍽 `/eaten` - I’ll remind you to eat and suggest food ideas.\n"
            "📅 `/today` - Tell me about your day!\n"
            "💛 `/period` - I have self-care tips for that time of the month.\n"
            "Just type any of these commands or click the buttons!"
        )

# Define additional functions
async def random_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = random.choice(JOKES)
    await update.message.reply_text(f"Here’s a joke for you: {joke}")

async def random_fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fact = random.choice(FACTS)
    await update.message.reply_text(f"Fun fact: {fact}")

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    await update.message.reply_text(f"Nice to meet you, {name}! How can I assist you today?")

async def have_you_eaten(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Have you eaten yet? If not, remember to nourish yourself! Here's a suggestion: How about a warm bowl of soup or your favorite comfort food?"
    )

async def what_have_you_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What have you been up to today? Tell me all about it—I’d love to hear!")

async def period_care(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hang in there! Here’s a little self-care pack: \n\n"
        "- Drink plenty of water 💧\n"
        "- Apply a warm compress for cramps 🌡\n"
        "- Treat yourself to something sweet 🍫\n"
        "- Relax with a feel-good show or some music 🎶"
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here’s how I can help:\n"
        "/start - Greet you\n"
        "/joke - Share a random joke\n"
        "/fact - Share a random fun fact\n"
        "/eaten - Remind you to eat and suggest food\n"
        "/today - Ask about your day\n"
        "/period - Self-care tips during periods\n"
        "/help - Show this help message"
    )

# Initialize the bot with your API token
app = ApplicationBuilder().token("7725970864:AAEyloRi05lmFMLJx7dKpUhV-dk5gYaiYvU").build()

# Add command handlers to the bot
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("joke", random_joke))
app.add_handler(CommandHandler("fact", random_fact))
app.add_handler(CommandHandler("eaten", have_you_eaten))
app.add_handler(CommandHandler("today", what_have_you_done))
app.add_handler(CommandHandler("period", period_care))
app.add_handler(CommandHandler("help", help_command))

# Add handler for inline button presses
app.add_handler(CallbackQueryHandler(button_handler))

# Add message handler to handle user input (e.g., names)
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_name))

# Run the bot
print("Bot is running...")
app.run_polling()
