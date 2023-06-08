from googletrans import Translator
translator=Translator(raise_exception=True);
ex=translator.detect('చీమ')
print(ex)
strr=translator.translate('చీమ','en')


