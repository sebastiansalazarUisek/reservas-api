def load_env_file():
    settings = {}

    try:
        file = open(".env", "r", encoding="utf-8")

        for line in file:
            line = line.strip()

            if line == "" or line.startswith("#"):
                continue

            if "=" in line:
                key, value = line.split("=", 1)
                settings[key] = value

        file.close()

    except FileNotFoundError:
        print("Archivo .env no encontrado")

    return settings


settings = load_env_file()


def get_setting(key, default=""):
    return settings.get(key, default)