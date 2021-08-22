import requests as re
import telegram
import json
from telegram import Update
from random import randint
import os.path as pt
from telegram.ext import (
    CallbackContext, 
    CommandHandler, 
    Updater, 
    MessageHandler , 
    Filters,
    ConversationHandler,
    )

def getPhotos(info:dict) -> list :

    count = len(info)
    index = randint(1,count)
    result = info[str(index)]

    return result

def start(update: Update , context : CallbackContext) : 
    
    info = {
        "1": ["https://outmaxshop.ru/images/testimonials/16272388848014539411296026360614_1627239027.jpg", "https://outmaxshop.ru/images/testimonials/16272389048578615475529187656811_1627239027.jpg", "https://outmaxshop.ru/images/testimonials/16272389271302373432481685482990_1627239027.jpg"],
        "2": ["https://outmaxshop.ru/images/testimonials/img-20210723-143630_1627037489.jpg", "https://outmaxshop.ru/images/testimonials/img-20210723-143609_1627037489.jpg", "https://outmaxshop.ru/images/testimonials/img-20210723-143543_1627037489.jpg"],
        "3": ["https://outmaxshop.ru/images/testimonials/20210723-085643_1627019963.jpg", "https://outmaxshop.ru/images/testimonials/20210723-085650_1627019964.jpg", "https://outmaxshop.ru/images/testimonials/20210723-085656_1627019964.jpg"],
        "4": ["https://outmaxshop.ru/images/testimonials/p-20210719-122936_1626686589.jpg", "https://outmaxshop.ru/images/testimonials/p-20210719-121349-bf_1626686589.jpg"],
        "5": ["https://outmaxshop.ru/images/testimonials/img-20210717-145220_1626515549.jpg"],
        "6": ["https://outmaxshop.ru/images/testimonials/img-20210713-123510_1626370999.jpg"],
        "7": ["https://outmaxshop.ru/images/testimonials/image-15-07-21-11-13-2_1626330012.jpeg"], "8": ["https://outmaxshop.ru/images/testimonials/d5c426e3-3b57-46fe-96ea-bafed95a738c_1628263667.jpeg", "https://outmaxshop.ru/images/testimonials/f510ff7a-7adf-4f95-82a1-5e9751117776_1628263667.jpeg", "https://outmaxshop.ru/images/testimonials/c0eedc77-ce33-4c1b-8634-fcfeaa2b2e51_1628263667.jpeg"],
        "9": ["https://outmaxshop.ru/images/testimonials/1d3269bc-39bf-4bfa-87c1-0627d972dade_1628262872.jpeg", "https://outmaxshop.ru/images/testimonials/f9b74d44-95b0-450c-8625-07db2712b293_1628262872.jpeg", "https://outmaxshop.ru/images/testimonials/529ce169-5855-4d9d-85e9-3485756662c8_1628262872.jpeg"],
        "10": ["https://outmaxshop.ru/images/testimonials/1628247588634136256772_1628247610.jpg"],
        "11": ["https://outmaxshop.ru/images/testimonials/img-20210806-172434_1628242173.jpg", "https://outmaxshop.ru/images/testimonials/img-20210806-172344_1628242173.jpg", "https://outmaxshop.ru/images/testimonials/img-20210806-172355_1628242173.jpg"],
        "12": ["https://outmaxshop.ru/images/testimonials/img-20210805-202722_1628184754.jpg", "https://outmaxshop.ru/images/testimonials/img-20210805-202749_1628184754.jpg"],
        "13": ["https://outmaxshop.ru/images/testimonials/bbb97ca0-c225-40ea-bf88-e5c016182f23_1628173493.jpeg", "https://outmaxshop.ru/images/testimonials/ea65a5db-379f-4f9d-9297-9d1e80095303_1628173493.jpeg", "https://outmaxshop.ru/images/testimonials/2b28aad6-3484-49cd-b436-d78e75d79b89_1628173493.jpeg"],
        "14": ["https://outmaxshop.ru/images/testimonials/image_1628166134.jpg"],
        "15": ["https://outmaxshop.ru/images/testimonials/20210804-175534_1628089013.jpg", "https://outmaxshop.ru/images/testimonials/20210804-175600_1628089013.jpg", "https://outmaxshop.ru/images/testimonials/20210804-175611_1628089013.jpg"],
        "16": ["https://outmaxshop.ru/images/testimonials/376d9c37-5300-4b5d-b5ea-c7eacf51a7be_1628081332.jpeg", "https://outmaxshop.ru/images/testimonials/a2b29ef9-de4a-4338-adf0-670a1752e489_1628081332.jpeg", "https://outmaxshop.ru/images/testimonials/ef134341-f152-40d0-b702-5eea9ed63741_1628081332.jpeg"],
    }

    photosForReview = getPhotos(info)

    firstMessage = 'Привет. Тебе нужно оставить отзыв в группе ВК - https://vk.com/topic-206536297_48088233 По следующему ТЗ : Почему вы выбрали именно нас? Почему вы купили у нас?  Что вы купили у нас? Какое качество? Все ли у вас было хорошо с доставкой. ОТЗЫВЫ ДОЛЖНЫ БЫТЬ ПОЛОЖИТЕЛЬНЫМИ! К ОТЗЫВУ ОБЯЗАТЕЛЬНО ПРИКРЕПИТЬ ФОТОГРАФИИ КОТОРЫЕ СЕЙЧАС ВАМ ПРИДУТ'
    photoMessage = 'ЕСЛИ ОТЗЫВ С ТАКИМ ФОТО УЖЕ ЕСТЬ, ПОЛУЧИТЕ НОВЫЕ ФОТО НАЖАТИЕМ НА /start'
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=firstMessage)

    for item in photosForReview :
        context.bot.send_document(chat_id=update.effective_chat.id, document=item)
    context.bot.send_message(chat_id=update.effective_chat.id, text=photoMessage)

if __name__ == '__main__' :

    updater = Updater('1981681842:AAGa8DKSFXsTaxe4_3DqcVdb02HtSW5c6Y0')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
