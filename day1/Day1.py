#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import nltk


# In[2]:


BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет', 'Добрый день', 'Шалом', 'Здравствуйте'],
            'responses': ['Привет, человек', 'Доброго времени суток']
        },
        'bye': {
            'examples': ['Пока', 'Досвидания', 'До свидания', 'Прощайте'],
            'responses': ['Счастливо', 'Еще увидимся', 'Если что, я тут. Возвращайтесь']
        }
    },
    
    'failure_phrases': [
        'Попробуйте написать по другому',
        'Что-то непонятно',
        'Я же всего лишь бот. Сформулируйте попроще'
    ]
}


# In[3]:


def filter_text(text):
    text = text.lower()
    text = [c for c in text if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- ']
    text = ''.join(text)
    return text

def get_intent(question):
    for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            filtered_example = filter_text(example)
            dist = nltk.edit_distance(filtered_example, filter_text(question))
            if dist / len(filtered_example) < 0.4:
                return intent


# In[4]:


def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        phrases = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(phrases)


# In[5]:


def generate_answer_by_text(question):
    return  # TODO 3th day


# In[6]:


def get_failure_phrase():
    phrases = BOT_CONFIG['failure_phrases']
    return random.choice(phrases)


# In[7]:


def bot(question):
    # NLU
    intent = get_intent(question)
    
    # Получение ответа
    
    # Ищем готовый ответ
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer
    
    # Генеруем подходящий по контексту ответ
    answer = generate_answer_by_text(question)
    if answer:
        return answer

    # Используем заглушку
    answer = get_failure_phrase()
    return answer


# In[8]:


question = None

while question not in ['exit', 'выход']:
    question = input()
    answer = bot(question)
    print(answer)


# In[ ]:




