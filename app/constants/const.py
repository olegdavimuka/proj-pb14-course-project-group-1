from enum import Enum
from os import getenv


class UserStatus(Enum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    PAUSED = "PAUSED"


BOT_TOKEN = getenv("BOT_TOKEN")

CITIES = [
    "Вінниця",
    "Дніпро",
    "Житомир",
    "Запоріжжя",
    "Івано-Франківськ",
    "Київ",
    "Кропивницький",
    "Луцьк",
    "Львів",
    "Миколаїв",
    "Одеса",
    "Полтава",
    "Рівне",
    "Суми",
    "Тернопіль",
    "Харків",
    "Херсон",
    "Хмельницький",
    "Черкаси",
    "Чернівці",
    "Чернігів",
]

HOBBIES = [
    "Відео ігри 🎮",
    "Настільні ігри 🎲",
    "Музика 🎶",
    "Спорт 🎾",
    "Подорожі ✈🛸",
    "Колекціонування 💎 ",
    "Фільми та серіали 🎬",
    "Малювання та живопис 🎨",
    "Кулінарія 🥘",
    "Медитація та йога 🧘",
    "Танці 💃",
    "Книги 📚",
    "Вивчення мов 🗣️",
    "Програмування 🖥️",
    "Садівництво 🪴",
    "Роботехніка 🤖",
] + ["Це все"]

DOMAINS = [
    "Advertising(реклама)",
    "Dev & Data Science",
    "Graphics",
    "Humanitarium",
    "Interface Design",
    "Management",
    "Marketing",
    "Visual Arts",
]

GOALS = [
    "Cтворення стартапу",
    "Навчання та обмін досвідом",
    "Пошук інвесторів",
    "Обмін ідеями",
    "Розширення кола контактів",
    "Дружні стосунки",
    "Розвиток освіти",
    "Участь у хакатонах",
]
