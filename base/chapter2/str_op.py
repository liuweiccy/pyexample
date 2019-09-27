# 在屏幕中央且宽度合适的方框内打印一个句子

sentence = input("Sentence:")

screen_with = 100
text_width = len(sentence)
box_width = text_width + 6
left_width = (screen_with - box_width) // 2

print()
print(' ' * left_width + '+' + '-' * (box_width - 2) + '+')
print(' ' * left_width + '|' + ' ' * (box_width - 2) + '|')
print(' ' * left_width + '|' + ' ' * 2 + sentence + ' ' * 2 + '|')
print(' ' * left_width + '|' + ' ' * (box_width - 2) + '|')
print(' ' * left_width + '+' + '-' * (box_width - 2) + '+')
