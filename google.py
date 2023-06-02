import googletrans
from googletrans import Translator

t = Translator()
a = t.translate("dit me may", src="vi", dest="en")
print(a.text)
