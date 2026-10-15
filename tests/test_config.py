from datetime import time

from src.config import Settings


# Test parse_schedule()
def test_parse_schedule_with_string() -> None:
    result = Settings.parse_schedule("08:00, 18:00")
    assert result == [time(8, 0), time(18, 0)]
  

# Second method 
# Simula o .env na memória, sem arquivo real
def test_settings_env_mock():
    settings = Settings(
        DIGEST_SCHEDULE=("00:59, 23:59"),
        TELEGRAM_BOT_TOKEN="fake-token",
        TELEGRAM_CHAT_ID=201,
        GROQ_API_KEY="/fake-api/v1",
        DATABASE_URL="postgresql+asyncpg://fake",
        DIGEST_MAX_ARTICLES=22
    )

    assert settings.DIGEST_SCHEDULE == [time(0, 59), time(23, 59)]


def test_settings_negative_hours():
    settings = Settings(
        DIGEST_SCHEDULE=("-00:59, -23:59"),
        TELEGRAM_BOT_TOKEN="fake-token2",
        TELEGRAM_CHAT_ID=202,
        GROQ_API_KEY="/fake-api/v2",
        DATABASE_URL="postgresql+asyncpg://fake",
        DIGEST_MAX_ARTICLES=23

    )

    assert settings.DIGEST_SCHEDULE == [time(-0, 59), time(-23, 59)]