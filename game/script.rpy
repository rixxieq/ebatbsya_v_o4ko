# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define fif = Character('фифинятко', color="#85de78")
define pidor = Character('п(ом)идорка', color="#62d4e3")
define rix = Character('rixxie', color="#41a6f3")

image blyadushnik = "bg/блядушник.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

transform sleva:
    zoom 1.3
    xalign .07
    yalign .55

transform sprava:
    zoom 1.3
    xalign .72
    yalign .55

image rfrfi1 = "characters/@2/rfrfi1.jpg"
image pomdorka = "characters/@2/pomdorka.jpg"

# Игра начинается здесь:
label start:

    "Короче деф день в блядушнике"
    with dissolve
    scene blyadushnik
    show rfrfi1 at sleva
    show pomdorka at sprava
    pause 1.0
    fif "я с одним господином дрочуном общалась"
    fif "который ноги любит"
    show pomdorka at sleva
    show rfrfi1 at sprava
    with ease
    pidor "прям щас общаешься"
    show rfrfi1 at sleva
    show pomdorka at sprava
    with ease
    fif "фу умри я не буду с тобой гулять"
    fif "я приду в хиджабе"
    show pomdorka at sleva
    show rfrfi1 at sprava
    with ease
    pidor "👍"
    "Ну и дауны"
    show rfrfi1 at sleva
    show pomdorka at sprava
    fif "фу хохлы"
    hide pomdorka
    show rixxieq at sleva
    show rfrfi1 at sprava
    with zoominout
    rix "ты лошара ебаная соси аххахааахаахахахахаха"

    return