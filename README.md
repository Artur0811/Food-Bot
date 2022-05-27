Описание
FoodBot – бот, выдающий различные рецепты при запросе.  Для хранения рецептов используется локальная база данных. Есть функция раздела рецептов на обед, завтрак и ужин. Можно составить меню на день или получить случайный рецепт. Также пользователь может самостоятельно добавить рецепт.
Описание кода:
Код можно разбить на 4 больших блока (класса)
1 class DATABASE – нужен для работы с базой данных. В свойства объекта передается клиент, имя клиента, название коллекции
Функции:
sert_document(data) – создаёт новый объект в базе данных
find_doc(data, mult = False ) - ищет объект(-ы)
del_doc(data) –  удаляет  объект в базе данных 
upd_doc(data, newe) – заменяет объект в базе данных
oll() – выводит все объекты базы данных
ush() – выводит максимальное id объекта типа ужин
zav() – выводит максимальное id объекта типа завтрак
ob() - выводит максимальное id объекта типа обед
2 class ret – нужен для вывода сообщения. При инициализации передается введенное пользователем сообщение; то, что нужно вывести, f – нужно ли выводить, как готовить блюдо (по умолчанию True) 
Функции:
sey() – выводит рецепт (картинку при наличии, имя, состав) и запрашивает нужно ли вывести, как готовить блюдо 
3 class commands – нужен для обработки при различных командах. При инициализации передается введенное пользователем сообщение.
Функции:
start_message() – выводит стартовое сообщение
add_massenge() – добавляет рецепт. Для этого у пользователя запрашивается категория (завтрак, обед, ужин), название блюда, картинка (не обязательный элемент), состав и как приготовить блюдо. Блюду присваивается совой id, в зависимости от категории:
завтрак – 1 - 10000
обед –  10001 - 20000
ужин-  >20000
Берется следующее значение максимального id.
Добавление нового рецепта можно прервать в любой момент
menu() - составляет меню на день из  завтрака, обеда и ужина
4 class log – логический блок, отвечающий за распределение действий. При инициализации передается введенное пользователем сообщение.
Функции:
message_reply()- определяет, что нужно сделать при введенном сообщении.
