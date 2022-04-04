cat > .env << EOL
API_ID=${api_id}
API_HASH=${api_hash}

# sqlite/sqlite3
DATABASE_TYPE=${db_type}
# file name for sqlite3
DATABASE_NAME=${db_name}
EOL

echo "Юзербот запущен! Напишите python bot.py"
