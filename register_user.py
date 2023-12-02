from telegram import Update, ReplyKeyboardMarkup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ
import psycopg2
import geopy

import user


def wait_for_answer(func):
    def wrapper(update, context):
        result = func(update, context)

        if result:
            return result

        buttons = [['Так', 'Ні']]
        reply_markup = ReplyKeyboardMarkup(buttons)

        update.message.reply_text("Не отримав відповідь. Ви ще хочете\
                                  продовжувати реєстрацію?",
                                  reply_markup=reply_markup)
        answer = update.message.text

        if answer == "Ні":
            update.message.reply_text("Реєстрація невдала,\
                                      чекатиму Вас іншим разом")
            return False
        else:
            return func(update, context)

    return wrapper


def get_coordinates(city):
    geolocator = geopy.Nominatim(user_agent="my_app")
    location = geolocator.geocode(city)
    # coordinates = location.latitude, location.longitude
    return location


@wait_for_answer
def get_user_id(update):
    return update.effective_user.id


@wait_for_answer
def name():
    update.message.reply_text("Вітаю! Яке Ваше ім'я?")
    answear = update.message.text
    return answear


@wait_for_answer
def born_year():
    update.message.reply_text("У якому році Ви народилися?")
    answear = update.message.text
    return answear


@wait_for_answer
def location():
    buttons = [['Так', 'Ні']]
    reply_markup = ReplyKeyboardMarkup(buttons)

    update.message.reply_text("Я можу використати Вашу геолокацію?",
                              reply_markup=reply_markup)
    answear = update.message.text
    if answear == 'Так':
        answear = update.message.location
    elif answear == 'Ні':
        update.message.reply_text("Введіть Ваше місто")
        answear = get_coordinates(update.message.text)
    return answear


@wait_for_answer
def domain():
    update.message.reply_text("Яка сфера Ваших занять?")
    answear = update.message.text
    return answear


@wait_for_answer
def position():
    update.message.reply_text("А яку посаду обіймаєте?")
    answear = update.message.text
    return answear


@wait_for_answer
def photo():
    update.message.reply_text("Завантажте фото")
    answear = update.message.photo[0]
    return answear


@wait_for_answer
def description():
    update.message.reply_text("Розкажіть трохи про себе")
    answear = update.message.text
    return answear


@wait_for_answer
def status():
    buttons = [['Активувати', 'Створити']]
    reply_markup = ReplyKeyboardMarkup(buttons)
    update.message.reply_text("Хочете активувати акаунт чи поки лише створити?"
                              ,reply_markup=reply_markup)
    answear = update.message.text
    if answear == 'Активувати':
        answear = 1
    elif answear == 'Створити':
        answear = 0
    return answear


database_url = environ.get("PG_DB_URL")
engine = psycopg2.connect(
        database=environ.get("PG_DB_NAME"), user=environ.get("PG_USER"),
        host="db", password=environ.get("PG_USER_PASSWORD"), port=5432
    )

Session = sessionmaker(bind=engine)
session = Session()

current_telegram_user_id = get_user_id(update)

already_users = session.query(User)\
    .filter(User.telegram_user_id == current_telegram_user_id)\
    .all()

if already_users is None:
    user_name = name()
    if user_name is not False:
        user_born_year = born_year()
        if user_born_year is not False:
            user_lacotaion_latitude = location().latitude
            user_lacotaion_longitude = location().longitude
            if user_lacotaion_latitude is not False:
                user_domain = domain()
                if user_domain is not False:
                    user_position = position()
                    if user_position is not False:
                        user_photo = photo()
                        if user_photo is not False:
                            user_description = description()
                            if user_description is not False:
                                user_status = status()
else:
    break

new_user = User(user_name=user_name,
                user_born_year=user_born_year,
                user_lacotaion=user_lacotaion,
                domain=user_domain,
                position=user_position,
                photo=user_photo,
                description=user_description,
                status=user_status,
                telegram_user_id=current_telegram_user_id,
                raiting=5.0
                )
session.add(new_user)
session.commit()
