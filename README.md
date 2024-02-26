# 🤖 leortBot Discord

Welcome to leortBot, my first Discord bot! This bot has been developed to respond to messages for now and can be easily configured and expanded according to your needs.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/leort11/BotDiscord.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the `.env` file:**
   - Open the `.env` file in the root folder.
   - Insert your Discord token and other necessary information.
   - Save the file.

4. **Run the bot:**
   ```bash
   python src/main.py
   ```

## 🤝 Contribution

If you want to contribute, we'll be happy to receive your suggestions, bug reports, or pull requests. Please follow the contribution and code guidelines when submitting changes.

## 📜 Commands

1. **test**
   ```bash
   /test
   ```
   - Writes "Hello World" in the Discord chat.

2. **/cargos**
   ```
   /cargos
   ```
   - Shows an example of a box that adds positions based on reactions to the message.

3. **/moeda**
   ```
   /moeda
   ```
   - Flips a coin with a 50% chance of coming up heads or tails.

## ⚙️ Configuration
   - `.env`: Contains the bot configurations.
      ```bash
        TOKEN=YOUR_TOKEN_HERE
        PREFIX=/
        etc...
      ```
