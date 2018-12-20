favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

print("\n")

#遍历字典中的键
for name in favorite_languages.keys():
    print(name)

print("\n")
#遍历字典中的值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is  " +
              favorite_languages[name].title() + "!")

print("\n")

#按排序的顺序输出字典中的值
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you fro taking the poll.")

print("\n")
#使用set去除重复项
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())