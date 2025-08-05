# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define fif = Character('фифинятко', color="#85de78")
define pidor = Character('п(ом)идорка', color="#62d4e3")

image blyadushnik = "bg/блядушник.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

image rfrfi1 = "rfrfi1@2.png"
image pomdorka = "pomdorka@2.png"

# Игра начинается здесь:
label start:

    scene blyadushnik

    show rfrfi1 at left
    show pomdorka at right

    fif "ааааа я люблю геншин"

    pidor "женщины дерьмо"

    return