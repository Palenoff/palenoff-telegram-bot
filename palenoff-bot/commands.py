import responses
import re
#professional_qualities = {"образование":responses.education,"навыки":responses.skills,"опыт":responses.skills,"проекты":responses.projects,"назад":main}
#personal_qualities = {"хобби":responses.hobbies,"языки":responses.languages,"личные качества":responses.personality,"назад":main}
#main = ["помощь","профессиональные качества", "персональные качества", "о боте"]
question_patterns = {
    "учёба":"образование",
    "(какое)?\s*у?\s*(\s*палёнова|\s*кирилла)*образование\s*у?\s*(\s*палёнова|\s*кирилла)*\?*":"образование",
    "где\s*(\s*палёнов|\s*кирилл)*учился\s*(\s*палёнов|\s*кирилл)*\?*":"РГГУ, Отделение интеллектуальных систем в гуманитарной сфере",
    "когда\s*(\s*палёнов|\s*кирилл)*учился\s*(\s*палёнов|\s*кирилл)*\?*":"2014-2018 года",
    "где\s*(\s*палёнов|\s*кирилл)*работал\s*(\s*палёнов|\s*кирилл)*\?*":"РГГУ, Управление по информатизации и информационным технологиям",
    "кем\s*(\s*палёнов|\s*кирилл)*работал\s*(\s*палёнов|\s*кирилл)*\?*":"Инженером (системным администратором)",
    "когда\s*(\s*палёнов|\s*кирилл)*работал\s*(\s*палёнов|\s*кирилл)*\?*":"Май 2017-Июнь 2018",
    "сколько\s*(\s*палёнов|\s*кирилл)*работал\s*(\s*палёнов|\s*кирилл)*\?*":"1 год 2 месяца",
    "работа":"опыт",
    "опыт\sработы":"опыт",
    "(какой)?\s*опыт\s*(работы)?\s*(есть)?\s*у?\s*(\s*палёнова|\s*кирилла)*\?*":"опыт",
    "что\s*(\s*палёнов|\s*кирилл)*умеет\s*(\s*палёнов|\s*кирилл)*(делать)*\?*":"навыки",
    "(какие)?\s*навыки\s*(есть)?\s*у?\s*(\s*палёнова|\s*кирилла)*\?*":"навыки",
    "c\+\+|html|css|javascript|jquery|php|sql|git":"навыки",
    "(\s*палёнов|\s*кирилл)*\s*(знает|пишет|программирует|владеет|кодит)?\s*(ли)*\s*(\s*палёнов|\s*кирилл)*\s*(на)*\s*(c#|с\sшарп|си\sшарп|шарп|шарпы|шарпе)\?*":"c#",
    "(\s*палёнов|\s*кирилл)*\s*(знает|пишет|программирует|владеет|кодит)?\s*(ли)*\s*(\s*палёнов|\s*кирилл)*\s*(на)*\s*(java|джава|джаву)\?*":"java",
    "(\s*палёнов|\s*кирилл)*\s*(знает|пишет|программирует|владеет|кодит)?\s*(ли)*\s*(\s*палёнов|\s*кирилл)*\s*(на)*\s*(python|питон|питоне|пайтон|пайтоне)\?*":"python",
    "(\s*палёнов|\s*кирилл)*\s*(знает|пишет|программирует|владеет|кодит)?\s*(ли)*\s*(\s*палёнов|\s*кирилл)*\s*(на)*(с\+\+|html|css|javascript|jquery|php|sql|git)\?*":"Определённые знания в этом у Кирилла есть😇",
    "(какие)?\s*проекты\s*(есть)?\s*у?\s*(\s*палёнова|\s*кирилла)*\?*":"проекты",
    "в\s*каких\s*проектах\s*участвовал\s*(\s*палёнов|\s*кирилл)*\?*":"проекты",
    "(какие)?\s*хобби\s*(есть)?\s*у?\s*(\s*палёнова|\s*кирилла)*\?*":"хобби",
    "чем\s*любит\s*заниматься\s*(\s*палёнов|\s*кирилл)*\sв\s*свободное\s*время\?*":"хобби",
    "что\s*любит\s*(\s*палёнов|\s*кирилл)*\?*":"хобби",
    "что\s*нравится\s*(\s*палёнову|\s*кириллу)*\?*":"хобби",
    "любимые\s*занятия\?*":"хобби",
    "какие\s*языки\s*(знает)*\s*(\s*палёнов|\s*кирилл)*(знает)*\?*":"языки",
    "какими\s*языками\s*владеет\s*(\s*палёнов|\s*кирилл)*\?*":"языки",
    "на\s*каких\s*языках\s*(говорит)*\s*(\s*палёнов|\s*кирилл)*\?*":"языки",
    "английский\?*":"Уровень C1/Advanced",
    "французский\?*":"Уровень B2/Niveau avancé",
    "уровень\s*английского\?*":"Уровень C1/Advanced",
    "уровень\s*французского\?*":"Уровень B2/Niveau avancé",
    "(какой)?\s*(\s*палёнов|\s*кирилл)*\s*(человек)*\s*(\s*палёнов|\s*кирилл)*\?*":"личные качества",
    "(что)?\s*(\s*палёнов|\s*кирилл)*\s*(за)*\s*(человек)*\s*(\s*палёнов|\s*кирилл)*\?*":"личные качества"
    }

def parse_text(text):
	for key in question_patterns:
		if re.match(key,text):
			return question_patterns[key]
	return None