from translate import Translator

# Membuat penerjemah dari Bahasa Spanyol ke Bahasa Inggris
translator = Translator(from_lang="fr", to_lang="en")

# Menerjemahkan teks
translation = translator.translate("Comment le saurais-tu ?")
print(translation)  # Hello, how are you?