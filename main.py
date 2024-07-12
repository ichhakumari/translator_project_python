import translators

q_text = "Hello, how are you?"

print(translators.translate_text(q_text, translator="google", to_language="hi"))

print(translators.translate_text(q_text, translator="google", to_language="zh"))
