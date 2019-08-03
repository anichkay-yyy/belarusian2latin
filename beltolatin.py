import re

def beltolatin(source):

    txt = source
    txt = re.sub(r'(?<=[а-яіўёА-ЯІЎЁ])([СсЦц])([Кк])([Іі]|[Іі][МмЯяХхМі]|[Іі][Мм][Іі])\b', r'\1◊\2\3', txt) # словы кшталту «беларускіх»: «с» не памягчаецца перад «к'». Усе магчымасці: {с,ц}кі{_,м,я,х,мі} на прыканцы слова
    txt = re.sub(r'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])я', r'йа', txt)
    txt = re.sub(r'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])ё', r'йо', txt)
    txt = re.sub(r'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])е', r'йэ', txt)
    txt = re.sub(r'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])ю', r'йу', txt)
    txt = re.sub(r'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])Я', r'Йа', txt)
    txt = re.sub(r'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])Ё', r'Йо', txt)
    txt = re.sub(r'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])Е', r'Йэ', txt)
    txt = re.sub(r'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])Ю', r'Йу', txt)
    txt = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])І', r'¤І', txt)
    txt = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])і', r'¤і', txt)
    txt = re.sub(r"'І", r'ЙІ', txt)
    txt = re.sub(r"'і", r'йі', txt)
    txt = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])і', r'¤і', txt)
    txt = re.sub(r'я', r'¤а', txt)
    txt = re.sub(r'ё', r'¤о', txt)
    txt = re.sub(r'ю', r'¤у', txt)
    txt = re.sub(r'е', r'¤э', txt)
    txt = re.sub(r'Я', r'¤А', txt)
    txt = re.sub(r'Ё', r'¤О', txt)
    txt = re.sub(r'Ю', r'¤У', txt)
    txt = re.sub(r'Е', r'¤Э', txt)
    txt = re.sub(r"[']", r'', txt)
    txt = re.sub(r'[ьЬ]', r'¤', txt)
    txt = re.sub(r'Й', r'Й¤', txt)
    txt = re.sub(r'й', r'й¤', txt)
    txt = re.sub(r'Д[Зз]', r'Ð', txt)
    txt = re.sub(r'дз', r'ð', txt)
    txt = re.sub(r'Д[Жж]', r'Ŧ', txt)
    txt = re.sub(r'дж', r'ŧ', txt)
    txt = re.sub(r'дð', r'ðð', txt)
    txt = re.sub(r'Д[Ðð]', r'ÐÐ', txt)
    txt = re.sub(r'дŧ', r'ŧŧ', txt)
    txt = re.sub(r'Д[Ŧŧ]', r'ŦŦ', txt)
    txt = re.sub(r'([СсЗзЦцÐð])([бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШÐðŦŧйЙ]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([Нн])([Нн]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([Лл])([Лл]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([СсЗзЦцÐð])([бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШÐðŦŧйЙ]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([Нн])([Нн]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([Лл])([Лл]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([СсЗзЦцÐð])([бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШÐðŦŧйЙ]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([Нн])([Нн]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([Лл])([Лл]¤)', r'\1¤\2', txt)
    txt = re.sub(r'([СсЗзЦцÐð])([бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШÐðŦŧйЙ]¤)', r'\1¤\2', txt)
    txt = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШÐðŦŧйЙ])¤І', r'І', txt)
    txt = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШÐðŦŧйЙ])¤і', r'і', txt)
    txt = re.sub(r'Ð¤[Ðð]', r'Dð', txt)
    txt = re.sub(r'ð¤ð', r'dð', txt)
    txt = re.sub(r'Ŧ[Ŧŧ]', r'Dŧ', txt)
    txt = re.sub(r'ŧŧ', r'dŧ', txt)
    txt = re.sub(r'Л¤(?![аоэуыіАОЭУЫІ])', r'Ĺ', txt)
    txt = re.sub(r'Н¤(?![аоэуыіАОЭУЫІ])', r'Ń', txt)
    txt = re.sub(r'С¤(?![аоэуыіАОЭУЫІ])', r'Ś', txt)
    txt = re.sub(r'З¤(?![аоэуыіАОЭУЫІ])', r'Ź', txt)
    txt = re.sub(r'Ц¤(?![аоэуыіАОЭУЫІ])', r'Ć', txt)
    txt = re.sub(r'Ð¤(?![аоэуыіАОЭУЫІ])', r'Dź', txt)
    txt = re.sub(r'л¤(?![аоэуыіАОЭУЫІ])', r'ĺ', txt)
    txt = re.sub(r'н¤(?![аоэуыіАОЭУЫІ])', r'ń', txt)
    txt = re.sub(r'с¤(?![аоэуыіАОЭУЫІ])', r'ś', txt)
    txt = re.sub(r'з¤(?![аоэуыіАОЭУЫІ])', r'ź', txt)
    txt = re.sub(r'ц¤(?![аоэуыіАОЭУЫІ])', r'ć', txt)
    txt = re.sub(r'ð¤(?![аоэуыіАОЭУЫІ])', r'dź', txt)
    txt = re.sub(r'Й¤', r'Й', txt)
    txt = re.sub(r'й¤', r'й', txt)
    txt = re.sub(r'ð', r'dz', txt)
    txt = re.sub(r'Ð', r'Dz', txt)
    txt = re.sub(r'Ŧ', r'Dž', txt)
    txt = re.sub(r'ŧ', r'dž', txt)
    txt = re.sub(r'а', r'a', txt)
    txt = re.sub(r'б', r'b', txt)
    txt = re.sub(r'в', r'v', txt)
    txt = re.sub(r'г', r'h', txt)
    txt = re.sub(r'д', r'd', txt)
    txt = re.sub(r'ж', r'ž', txt)
    txt = re.sub(r'з', r'z', txt)
    txt = re.sub(r'і', r'i', txt)
    txt = re.sub(r'й', r'j', txt)
    txt = re.sub(r'к', r'k', txt)
    txt = re.sub(r'л', r'l', txt)
    txt = re.sub(r'м', r'm', txt)
    txt = re.sub(r'н', r'n', txt)
    txt = re.sub(r'о', r'o', txt)
    txt = re.sub(r'п', r'p', txt)
    txt = re.sub(r'р', r'r', txt)
    txt = re.sub(r'с', r's', txt)
    txt = re.sub(r'т', r't', txt)
    txt = re.sub(r'у', r'u', txt)
    txt = re.sub(r'ў', r'ŭ', txt)
    txt = re.sub(r'ф', r'f', txt)
    txt = re.sub(r'х', r'ch', txt)
    txt = re.sub(r'ц', r'c', txt)
    txt = re.sub(r'ч', r'č', txt)
    txt = re.sub(r'ш', r'š', txt)
    txt = re.sub(r'ы', r'y', txt)
    txt = re.sub(r'э', r'e', txt)
    txt = re.sub(r'А', r'A', txt)
    txt = re.sub(r'Б', r'B', txt)
    txt = re.sub(r'В', r'V', txt)
    txt = re.sub(r'Г', r'H', txt)
    txt = re.sub(r'Д', r'D', txt)
    txt = re.sub(r'Ж', r'Ž', txt)
    txt = re.sub(r'З', r'Z', txt)
    txt = re.sub(r'І', r'I', txt)
    txt = re.sub(r'Й', r'J', txt)
    txt = re.sub(r'К', r'K', txt)
    txt = re.sub(r'Л', r'L', txt)
    txt = re.sub(r'М', r'M', txt)
    txt = re.sub(r'Н', r'N', txt)
    txt = re.sub(r'О', r'O', txt)
    txt = re.sub(r'П', r'P', txt)
    txt = re.sub(r'Р', r'R', txt)
    txt = re.sub(r'С', r'S', txt)
    txt = re.sub(r'Т', r'T', txt)
    txt = re.sub(r'У', r'U', txt)
    txt = re.sub(r'Ў', r'Ŭ', txt)
    txt = re.sub(r'Ф', r'F', txt)
    txt = re.sub(r'Х', r'Ch', txt)
    txt = re.sub(r'Ц', r'C', txt)
    txt = re.sub(r'Ч', r'Č', txt)
    txt = re.sub(r'Ш', r'Š', txt)
    txt = re.sub(r'Ы', r'Y', txt)
    txt = re.sub(r'Э', r'E', txt)
    txt = re.sub(r'¤', r'i', txt)
    txt = re.sub(r'◊', r'', txt)

    return txt
