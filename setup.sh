#!/bin/bash

# Function to read user input and update .env file
update_env() {
    echo "$1=$2" >> .env
}

# Check if .env file exists, create if not
if [ ! -f .env ]; then
    touch .env
fi

# Ask for Discord API token
read -p "Enter your Discord API token: " token
update_env "TOKEN" "$token"

# Ask for bot prefix
read -p "Enter your bot prefix: " prefix
update_env "PREFIX" "$prefix"

echo "Config setup complete"
