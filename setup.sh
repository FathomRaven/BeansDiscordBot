#!/bin/bash

# Function to read user input and update .env file
update_env() {
    echo "$1=$2" >> .env
}

# Check if .env file exists, create if not
if [ ! -f .env ]; then
    touch .env
fi

# Create the virtual enviroment
python3 -m venv venv
source venv/bin/activate

# Install dependicies
pip install discord
pip install python-dotenv-vault
pip install requests

if [ ! -f .env ]; then
    # Ask for Discord API token
    read -p "Enter your Discord API token: " token
    update_env "TOKEN" "$token"

    # Ask for bot prefix
    read -p "Enter your bot prefix: " prefix
    update_env "PREFIX" "$prefix"
fi

echo "Setup complete"