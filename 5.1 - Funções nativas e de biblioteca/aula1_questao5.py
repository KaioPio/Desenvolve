import emoji

print(f"❤️ - {emoji.demojize('❤️')}")
print(f"👍 - {emoji.demojize('👍')}")
print(f"🤔 - {emoji.demojize('🤔')}")
print(f"🥳 - {emoji.demojize('🥳')}")
x = str(input("Digite uma frase (pode usar emojis com códigos como :red_heart:): "))

print(emoji.emojize(x, use_aliases=True))