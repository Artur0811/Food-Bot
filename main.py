import telebot
import pymongo, random

class DATABASE:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client["Art"]
        self.collection = self.db["Food"]

    def sert_document(self, data):
        return self.collection.insert_one(data).inserted_id

    def find_doc(self, data, mult = False, ):
        if mult:
            res = self.collection.find(data)
            return [*res]
        else:
            return self.collection.find_one(data)

    def del_doc(self, data):
        self.collection.delete_one(data)

    def upd_doc(self, data, newe):
        self.collection.update_one(data, {"$set" : newe})

    def oll(self):
        return list(self.collection.find({}))

    def ush(self):
        a = 20001
        while self.collection.find_one({"id": a +1}) != None:
            a+=1
        return a

    def zav(self):
        a = 1
        while self.collection.find_one({"id": a +1}) != None and a+1 < 10001:
            a+=1
        return a

    def ob(self):
        a = 10001
        while self.collection.find_one({"id": a +1}) != None and a+1 < 20001:
            a+=1
        return a


class ret:
    def __init__(self,message, b, f = True):
        self.message = message
        self.rec = b
        self.f = f

    def sey(self):
        if self.rec["photo"] != '':
            bot.send_photo(self.message.chat.id, self.rec["photo"])
        for i in self.rec:
            if i != "_id" and i != "id" and i != "photo" and i != "recipe":
                bot.send_message(self.message.chat.id, str(i) + ":" + ' \n' + ' \n' + str(self.rec[i]) + ' \n' + ' \n')

        if self.f:
            a = bot.send_message(self.message.chat.id, "Хотите ли вы узнать рецепт блюда?", reply_markup=keyboard5)

            @bot.message_handler(content_types='text')
            def da(message1):
                if message1.text.lower() == "да":
                    return bot.send_message(self.message.chat.id, self.rec["recipe"], reply_markup=keyboard1)
                else:
                    return bot.send_message(self.message.chat.id, "Ок", reply_markup=keyboard1)

            bot.register_next_step_handler(a, da)

class commands:
    def __init__(self,message):
        self.message = message

    def start_message(self):
        bot.send_message(self.message.chat.id, 'Привет')
        bot.send_message(self.message.chat.id, 'Вот что я могу:\nКоманды: \n/addarecipe \n/random"\nПри обычном вводе я буду искать рецепт.', reply_markup=keyboard1)

    def add_massenge(self):
        ap = {"photo": "", "name": "", "constituent": "", "recipe": "", "id": 0}
        a = bot.send_message(self.message.chat.id, "Ведите категорию: Завтрак, обед, ужин", reply_markup=keyboard4)

        @bot.message_handler(content_types='text')
        def kategoy(message):
            kat = message.text.lower()
            if kat == "прервать":
                bot.send_message(message.chat.id, "Добавление прервано", reply_markup=keyboard1)
                return None
            else:
                b = bot.send_message(message.chat.id, "Введите имя", reply_markup=keyboard2)
                if kat == 'завтрак':
                    ap["id"] = db.zav() + 1
                    bot.register_next_step_handler(b, name)
                elif kat == 'обед':
                    ap["id"] = db.ob() + 1
                    bot.register_next_step_handler(b, name)
                elif kat == 'ужин':
                    ap["id"] = db.ush() + 1
                    bot.register_next_step_handler(b, name)
                else:
                    pr = bot.send_message(message.chat.id, "Нет выбранной категории. Добавление прервано.",
                                          reply_markup=keyboard1)
                    bot.register_next_step_handler(pr, message_reply)

        @bot.message_handler(content_types='text')
        def name(message):
            name = message.text.lower()
            if name == "прервать":
                bot.send_message(message.chat.id, "Добавление прервано", reply_markup=keyboard1)
                return None
            else:
                ap["name"] = name
                b = bot.send_message(message.chat.id, "Добавьте фото", reply_markup=keyboard3)
                bot.register_next_step_handler(b, photo)

        @bot.message_handler(content_types='text')
        def photo(message):
            ph = message.text
            if ph.lower() == "прервать":
                bot.send_message(message.chat.id, "Добавление прервано", reply_markup=keyboard1)
                return None
            else:
                ap['photo'] = ph
                if ph == "пропустить":
                    ap['photo'] = ""
                b = bot.send_message(message.chat.id, "Ведите состав", reply_markup=keyboard2)
                bot.register_next_step_handler(b, constituent)

        @bot.message_handler(content_types='text')
        def constituent(message):
            constituent = message.text.lower()
            if constituent == "прервать":
                bot.send_message(message.chat.id, "Добавление прервано", reply_markup=keyboard1)
                return None
            else:
                ap["constituent"] = constituent
                c = bot.send_message(message.chat.id, "Ведите рецепт")
                bot.register_next_step_handler(c, recipe)

        @bot.message_handler(content_types='text')
        def recipe(message):
            recipe = message.text.lower()
            if recipe == "прервать":
                bot.send_message(message.chat.id, "Добавление прервано", reply_markup=keyboard1)
                return None
            else:
                ap["recipe"] = recipe
                db.sert_document(ap)
                bot.send_message(message.chat.id, "Рецепт добавлен!", reply_markup=keyboard1)

        bot.register_next_step_handler(a, kategoy)

    def menu(self):
        bot.send_message(self.message.chat.id, "Меню на сегодня:")
        bot.send_message(self.message.chat.id, "Завтрак:")
        zav = db.find_doc({"id": random.randrange(1, db.zav() + 1, 1)})
        b = ret(self.message, zav, f=False)
        b.sey()
        bot.send_message(self.message.chat.id, "Обед:")
        ob = db.find_doc({"id": random.randrange(10001, db.ob() + 1, 1)})
        c = ret(self.message, ob, f=False)
        c.sey()
        bot.send_message(self.message.chat.id, "Ужин:")
        ush = db.find_doc({"id": random.randrange(20001, db.ush() + 1, 1)})
        b = ret(self.message, ush, f=False)
        b.sey()

        @bot.message_handler(content_types='text')
        def da_menu(message):
            if message.text.lower() == "нет":
                return bot.send_message(message.chat.id, "Ок", reply_markup=keyboard1)
            else:
                if message.text.lower() == "рецепт завтрака":
                    bot.send_message(message.chat.id, zav["recipe"])
                elif message.text.lower() == "рецепт обеда":
                    bot.send_message(message.chat.id, ob["recipe"])
                elif message.text.lower() == "рецепт ужина":
                    bot.send_message(message.chat.id, ush["recipe"])
                a = bot.send_message(message.chat.id, "Хотите узнать подробнее?", reply_markup=keyboard6)
                return bot.register_next_step_handler(a, da_menu)

        a = bot.send_message(self.message.chat.id, "Хотите узнать подробнее?", reply_markup=keyboard6)

        bot.register_next_step_handler(a, da_menu)


class log:
    def __init__(self, message):
        self.message = message

    def message_reply(self):
        a = self.message.text.lower()
        if a == "что ты можешь":
            bot.send_message(self.message.chat.id,
                             "При обычном вводе я буду искать рецепт.\n Команды: \n/addarecipe - добавить рецепт\n/random - рандомный рецепт\n/createmenu- составить меню на день")
        elif a == "случайный рецепт":
            bot.send_message(self.message.chat.id, "Возможно вы искали это:")
            randomn(self.message)
        elif a == "ужин":
            b = ret(self.message, db.find_doc({"id": random.randrange(20001, db.ush() + 1, 1)}))
            b.sey()
        elif a == "обед":
            b = ret(self.message, db.find_doc({"id": random.randrange(10001, db.ob() + 1, 1)}))
            b.sey()
        elif a == "завтрак":
            b = ret(self.message, db.find_doc({"id": random.randrange(1, db.zav() + 1, 1)}))
            b.sey()
        elif a == "создать меню":
            menu(self.message)
        else:
            try:
                b = db.find_doc({"name": self.message})
                b.sey()
            except:
                bot.send_message(self.message.chat.id, "Ничего не найдено")


db = DATABASE()

token = '5298156959:AAFdbzvldtqmUI4vnM5yWGulTPI88eA5Nwk'
bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Случайный рецепт', "что ты можешь", "Завтрак", "Обед", "Ужин", "Создать меню")
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Прервать')
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard3.row('Прервать', "Пропустить")
keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard4.row('Прервать', "Завтрак", "Обед", "Ужин")
keyboard5 = telebot.types.ReplyKeyboardMarkup()
keyboard5.row('Нет', "Да")
keyboard6 = telebot.types.ReplyKeyboardMarkup()
keyboard6.row('Нет', "Рецепт завтрака", "Рецепт обеда", "Рецепт ужина")

@bot.message_handler(commands=['start'])
def start_message(message):
    b = commands(message)
    b.start_message()

@bot.message_handler(commands=["addarecipe"])
def add_massenge(message):
    b = commands(message)
    b.add_massenge()

@bot.message_handler(commands=["random"])
def randomn(message):
    b = ret(message, random.choice(db.oll()))
    b.sey()

@bot.message_handler(commands=["createmenu"])
def menu(message):
    b = commands(message)
    b.menu()

@bot.message_handler(content_types = 'text')
def message_reply(message):
    b = log(message)
    b.message_reply()

bot.infinity_polling()