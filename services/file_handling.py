import logging
import os

logger = logging.getLogger(__name__)


# Функция, возвращающая строку с текстом страницы и её размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    symbols = [",", ".", "!", ":", ";", "?"]
    
    # 1. Задаем максимальную границу среза
    end = start + (page_size-1)
    
    if end > len(text)-1:
        end = len(text)-1
    
    if text[end] in symbols and text[end-1] in symbols:
        while start < end and text[end] in symbols:
            end -= 1
            
    while start < end and text[end] not in symbols:
        end -= 1
        
    page_text = text[start:end+1]
        
    
    return page_text, len(page_text)


# Функция, формирующая словарь книги
def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    with open(path, "r", encoding="utf-8") as file:
        text = file.read().lstrip()
    
    book = {}
    start = 0
    i = 1
    while start < len(text):
        page_text, length = _get_part_text(text, start, page_size)
        book[i] = page_text.lstrip()
        start += length
        i += 1
    
    return book

