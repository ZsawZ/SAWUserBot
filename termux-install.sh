if ! command -v termux-setup-storage; then
  echo This script can be executed only on Termux
  exit 1
fi

termux-wake-lock

apt update -y
apt install python3 git clang ffmpeg wget libjpeg-turbo libcrypt ndk-sysroot zlib -y || exit 2

python3 -m pip install -U pip
LDFLAGS="-L${PREFIX}/lib/" CFLAGS="-I${PREFIX}/include/" pip3 install --upgrade wheel pillow

if [[ -d "SAWUserBot" ]]; then
  cd SAWUserBot
elif [[ -f ".env.dist" ]] && [[ -f "main.py" ]] && [[ -d "modules" ]]; then
  :
else
  git clone https://github.com/ZsawZ/SAWUserBot|| exit 2
  cd SAWUserBot || exit 2
fi

if [[ -f ".env" ]] && [[ -f "my_account.session" ]]; then
  echo "Похоже, что SAWUserBot уже установлен. Выход..."
  exit

python3 -m pip install -U -r requirements.txt || exit 2

echo
echo "Просто нажми Enter"
read -r -p "API_ID > " api_id

if [[ $api_id = "" ]]; then
  api_id="2860432"
  api_hash="2fde6ca0f8ae7bb58844457a239c7214"
else
  read -r -p "API_HASH > " api_hash
fi

echo "Напиши "2", пожалуйста (без кавычек):"
read -r -p "> " db_type

if [[ $db_type = 1 ]]; then
  echo "Please enter db_url"
  echo "You can get it here -> https://telegra.ph/How-to-get-Mongodb-URL-and-login-in-telegram-08-01"
  read -r -p "> " db_url
  db_name=Dragon_Userbot
  db_type=mongodb
else
  db_name=db.sqlite3
  db_type=sqlite3
fi

cat > .env << EOL
API_ID=${api_id}
API_HASH=${api_hash}

# sqlite/sqlite3
DATABASE_TYPE=${db_type}
# file name for sqlite3
DATABASE_NAME=${db_name}

exit 3
echo
echo "============================"
echo "Отлично! SAWUserBot установлен yспешно!"
echo "Запустить: python bot.py""
echo "============================"