import environs

env = environs.Env()
env.read_env("./.env")

db_type = env.str("DATABASE_TYPE")
db_url = env.str("DATABASE_URL", "")
db_name = env.str("DATABASE_NAME")

test_server = env.bool("TEST_SERVER", False)
