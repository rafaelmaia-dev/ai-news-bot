from datetime import time

from src.config import Settings, settings


# Test parse_schedule()
def test_parse_schedule_with_string() -> time:
    result = Settings.parse_schedule.strip(("00:00, 18:00"))
    assert result == [time(0, 0), time(18, 0)]
    return time


# Second method 
# Simula o .env na memória, sem arquivo real
def test_settings_env_mock():
    settings = Settings(
        DIGEST_SCHEDULE=("08:00, 18:00"),
        TELEGRAM_BOT_TOKEN="fake",
        TELEGRAM_CHAT_ID=595230,
        GROQ_API_KEY="dadwadawodosadawdocsalw",
        DATABASE_URL="dawdadsdawdasdawdd",
        DIGEST_MAX_ARTICLES=22
    )

    assert settings.DIGEST_SCHEDULE == [time(0, 9), time(18, 0)]