import random

BOT_CONFIG = {
    'intents': {
        'hello': {
            'example': ['Привет', 'Добрый день', ' Шалом', 'здраствуйте'],
            'responses': ['хвй человек', ' доброго времени', 'привет чел', 'челлллл']
        },
        'bye': {
            'example': ['ПОка', 'Покедова', ' покашки'],
            'responses': ['Покка человек', ' ели что я тут', 'доброй ночи']
        }
    },
    'get_failure_phrase': [
        'ПОпробуйте написать по другому',
        'Что-то непонятно,?',
        'Я же всего лишь бот'
    ]
}

def filter_text(text):
    text = text.lower()
    text = [c for c in text if c in 'абвгдеёжзийклмнопрстуфхцчшщэъыьюя- ']
    text = ''.join(text)
    return text

def get_intent(question):
    for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['example']:
            if filter_text(example) == filter_text(question):
                return intent


def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        phrases = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(phrases)


def generate_answer_by_text(question):
    return


def get_failure_phrase():
    phrases = BOT_CONFIG['get_failure_phrase']
    return random.choice(phrases)


def bot(question):
    intent = get_intent(question)
    if intent:
        answer = get_answer_by_intent(intent)
        if intent:
            return answer

    answer = generate_answer_by_text(question)
    if answer:
        return answer

    answer = get_failure_phrase()
    return answer


question = ''

while question not in ['exit', 'выход']:
    question = input()
    answer = bot(question)
    print(answer)
