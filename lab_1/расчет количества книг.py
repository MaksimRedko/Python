floppy_disk_volume = 1.44  # в Мб
number_of_page_in_books = 100
number_of_lines_per_page = 50
number_of_characters_per_line = 25
character_size = 4  # в байтах
res = 0
# расчитаем объем одной строки:
res += character_size * number_of_characters_per_line

# расчитаем объем страницы:
res *= number_of_lines_per_page

# расчитаем объем одной книги:
res *= number_of_page_in_books

# переведем объем книги из байт в Мб:
res = res / 1024 / 1024

nums_book = round(floppy_disk_volume // res)

print("Количество книг, помещающихся на дискету:", nums_book)
