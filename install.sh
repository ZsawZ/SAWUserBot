cat > .env << EOL
API_ID=${2860432}
API_HASH=${2fde6ca0f8ae7bb58844457a239c7214}

# sqlite/sqlite3
DATABASE_TYPE=${db_type}
# file name for sqlite3
DATABASE_NAME=${db_name}
EOL

echo "Юзербот запущен! Напишите python bot.py"
