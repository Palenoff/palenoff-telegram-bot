from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
start_markup = ReplyKeyboardMarkup(True)
start_markup.row("Профессиональные качества","Персональные качества");
start_markup.row("Помощь","О боте");

professional_qualities_markup = InlineKeyboardMarkup()
education_callback_button = InlineKeyboardButton(text="Образование", callback_data="образование")
skills_callback_button = InlineKeyboardButton(text="Навыки", callback_data="навыки")
experience_callback_button = InlineKeyboardButton(text="Опыт", callback_data="опыт")
projects_callback_button = InlineKeyboardButton(text="Проекты", callback_data="проекты")
professional_qualities_markup.row(education_callback_button,skills_callback_button)
professional_qualities_markup.row(experience_callback_button, projects_callback_button)


personal_qualities_markup = InlineKeyboardMarkup()
hobbies_callback_button = InlineKeyboardButton(text="Хобби", callback_data="хобби")
languages_callback_button = InlineKeyboardButton(text="Языки", callback_data="языки")
personality_callback_button = InlineKeyboardButton(text="Личные качества", callback_data="личные качества")
personal_qualities_markup.row(hobbies_callback_button,languages_callback_button)
personal_qualities_markup.row(personality_callback_button)
#personal_qualities_markup.row("","");
#personal_qualities_markup.row("","Назад");

skills_markup = InlineKeyboardMarkup()
c_sharp_skills_button = InlineKeyboardButton(text="C#", callback_data="c#")
java_skills_button = InlineKeyboardButton(text="Java", callback_data="java")
python_skills_button = InlineKeyboardButton(text="Python", callback_data="python")
skills_markup.row(c_sharp_skills_button,java_skills_button,python_skills_button)