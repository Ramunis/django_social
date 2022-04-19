from django import forms


class RegForm(forms.Form):
    F = forms.CharField(label="Фамилия")
    I = forms.CharField(label="Имя")
    O = forms.CharField(label="Отчество")
    UN = forms.CharField(label="Логин")
    PW = forms.CharField(widget=forms.PasswordInput(), label="Пароль")
    PW2 = forms.CharField(widget=forms.PasswordInput(), label="Повторите пароль")
    EM = forms.EmailField(label="Email")
    PH = forms.CharField(label="Телефон")
    DR = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label="День Рождения")
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    G = forms.CharField(label='Пол', widget=forms.RadioSelect(choices=CHOICES))
    FP = forms.ChoiceField(label="Семейное положение", choices=((1, "Не женат/Не жената"), (2, "Женат/Жената")))
    C = forms.CharField(label="Город")
    DE = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label="Год поступления")
    Pic = forms.CharField(label="Ссылка на изображение")


class SettForm(forms.Form):
    F = forms.CharField(label="Фамилия")
    I = forms.CharField(label="Имя")
    O = forms.CharField(label="Отчество")
    PH = forms.CharField(label="Телефон")
    DR = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label="День Рождения")
    FP = forms.ChoiceField(label="Семейное положение", choices=((1, "Не женат/Не жената"), (2, "Женат/Жената")))
    C = forms.CharField(label="Город")
    Pic = forms.CharField(label="Ссылка на изображение")
    Skype = forms.CharField()
    Telegram = forms.CharField()
    Discord = forms.CharField()
    Google = forms.CharField()
    About = forms.CharField(label="О себе", widget=forms.Textarea)
    Lang = forms.CharField(label="Иностранные языки", widget=forms.Textarea)
    Activ = forms.CharField(label="Деятельность", widget=forms.Textarea)
    Hobby = forms.CharField(label="Хобби", widget=forms.Textarea)
    Music = forms.CharField(label="Музыка", widget=forms.Textarea)
    Film = forms.CharField(label="Фильмы", widget=forms.Textarea)
    Book = forms.CharField(label="Книги", widget=forms.Textarea)
    Games = forms.CharField(label="Видеоигры", widget=forms.Textarea)


class ComForm(forms.Form):
    Name = forms.CharField(label="Название")
    Tem = forms.ChoiceField(label="Тема", choices=((1, "Программирование"), (2, "Железо"), (3, "Видеоигры"), (4, "Наука"), (5, "Иностранные языки"), (6, "Работа"), (7, "Путешествия"), (8, "СМИ"), (9, "Политика"), (10, "Красота и Здоровье"), (11, "Образование"), (12, "Спорт"), (13, "Стиль и мода"), (14, "Товары"), (15, "Философия"), (16, "Фото и Видео"), (17, "Юридическое"), (18, "Авто"), (19, "Бизнес"), (20, "Города и Страны"), (21, "Магия"), (22, "Развлечения"), (23, "Еда"), (24, "Животные и растения"), (25, "Искусство и Культура"), (26, "Юмор"), (27, "Знакомства"), (28, "+18")))
    About = forms.CharField(label="Описание", widget=forms.Textarea)
    Site = forms.CharField(label="Веб-сайт")
    Email = forms.EmailField(label="Email")
    Telegram = forms.CharField()
    Pic = forms.CharField(label="Ссылка на изображение")


class EvenForm(forms.Form):
    Name = forms.CharField(label="Название")
    Tem = forms.ChoiceField(label="Тематика", choices=((1, "Программирование"), (2, "Железо"), (3, "Видеоигры"), (4, "Наука"), (5, "Иностранные языки"), (6, "Работа"),
                                     (7, "Путешествия"), (8, "СМИ"), (9, "Политика"), (10, "Красота и Здоровье"), (11, "Образование"), (12, "Спорт"),
                                     (13, "Стиль и мода"), (14, "Товары"), (15, "Философия"), (16, "Фото и Видео"), (17, "Юридическое"), (18, "Авто"),
                                     (19, "Бизнес"), (20, "Города и Страны"), (21, "Магия"), (22, "Развлечения"), (23, "Еда"), (24, "Животные и растения"),
                                     (25, "Искусство и Культура"), (26, "Юмор"), (27, "Знакомства"), (28, "+18")))
    Adr = forms.CharField(label="Адрес")
    DT = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label="Дата")
    Sp = forms.CharField(label="Спонсор")
    About = forms.CharField(label="Описание", widget=forms.Textarea)
    Site = forms.CharField(label="Веб-сайт")
    Email = forms.EmailField(label="Email")
    Telegram = forms.CharField()
    Pic = forms.CharField(label="Ссылка на изображение")


class ConfForm(forms.Form):
    Name = forms.CharField(label="Название")
    About = forms.CharField(label="Описание", widget=forms.Textarea)
    Pic = forms.CharField(label="Ссылка на изображение")


class ChatForm(forms.Form):
    Con = forms.ChoiceField(label="Получатель", choices=((1, "Joe"), (2, "Rork")))
    Mes = forms.CharField(label="Сообщение", widget=forms.Textarea)


class MesForm(forms.Form):
    Mes = forms.CharField(label="Сообщение", widget=forms.Textarea)

