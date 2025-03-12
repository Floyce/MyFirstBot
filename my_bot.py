from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

# Lists of 100 jokes and facts
JOKES = [
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? It was two-tired.",
    "Why don’t eggs tell jokes? They might crack up.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why can’t your nose be 12 inches long? Because then it’d be a foot!",
    "Why did the scarecrow win an award? He was outstanding in his field.",
    "What do you call a factory that makes okay products? A satisfactory.",
    # Continue adding jokes here up to 100...
]

FACTS = [
    "A bolt of lightning is five times hotter than the surface of the sun.",
    "Sharks existed before trees were even a thing.",
    "Bananas are naturally radioactive due to their potassium content.",
    "Koalas have fingerprints that are almost identical to humans.",
    "Wombat poop is cube-shaped to prevent it from rolling away.",
    "The Amazon rainforest produces 20% of the world's oxygen.",
    "A blue whale’s heart is so big that a human could swim through its arteries.",
    "Jellyfish have been around for more than 500 million years.",
    # Continue adding facts here up to 100...
]

# Greet the user and ask their name
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there! What's your name?")

# Handle when the user sends their name
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    await update.message.reply_text(f"Nice to meet you, {name}! How are you feeling today?")

# Send a random joke
async def random_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = random.choice(JOKES)
    await update.message.reply_text(f"Here’s a joke for you: {joke}")

# Send a random fact
async def random_fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fact = random.choice(FACTS)
    await update.message.reply_text(f"Here’s a fun fact for you: {fact}")

# Ask if they've eaten and suggest food
async def have_you_eaten(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Have you eaten yet? If not, remember to nourish yourself! Here's a suggestion: How about a warm bowl of soup or your favorite comfort food?"
    )

# Ask what they've done today and respond supportively
async def what_have_you_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What have you been up to today? Tell me all about it—I’d love to hear!")

# Period care tips
async def period_care(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hang in there! Here’s a little self-care pack: \n\n"
        "- Drink plenty of water 💧\n"
        "- Apply a warm compress for cramps 🌡\n"
        "- Treat yourself to something sweet 🍫\n"
        "- Relax with a feel-good show or some music 🎶"
    )

# Help command listing all the bot's features
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

# Add message handler to get the user's name
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_name))

# Run the bot
print("Bot is running...")
app.run_polling()
