from os import getenv


class TestEnvironment:
    def test_environment_variables(self):
        assert getenv("PG_DB_NAME") not in ("", None)
        assert getenv("PG_USER") not in ("", None)
        assert getenv("PG_USER_PASSWORD") not in ("", None)
        assert getenv("PG_DB_URL") not in ("", None)
        assert getenv("BOT_TOKEN") not in ("", None)
        assert getenv("GPT_KEY") not in ("", None)
