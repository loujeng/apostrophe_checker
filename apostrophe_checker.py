import re

class ApostropheChecker:
    def __init__(self):
        self.rules = [
            (re.compile(r"\b([бпвмф])(?=[яюєї])", re.IGNORECASE), r"\1'"),
            (re.compile(r"\b([рР])(?=[яюєї])", re.IGNORECASE), r"\1'"),
            (re.compile(r"\bЛук(?=[яюєї])", re.IGNORECASE), r"Лук'"),
            (re.compile(r"\b(під|об|роз|над|з|між)(?=[яюєї])", re.IGNORECASE), r"\1'"),
            (re.compile(r"([бвгґджзклмнпрстфхцчшщ][бпвмф])'(?=[яюєї])", re.IGNORECASE), r"\1"),
        ]

    def validate_input(self, text):
        if not text or not text.strip():
            raise ValueError("Помилка: Текст не введено або він порожній!")

    def find_errors(self, text):
        self.validate_input(text)
        errors = []
        for pattern, _ in self.rules:
            for match in pattern.finditer(text):
                errors.append((match.start(), match.end(), match.group()))
        return errors

    def correct_text(self, text):
        self.validate_input(text)
        corrected_text = text
        for pattern, correction in self.rules:
            corrected_text = pattern.sub(correction, corrected_text)
        return corrected_text

    def highlight_errors(self, text):
        self.validate_input(text)
        errors = self.find_errors(text)
        highlighted_text = ""
        last_pos = 0
        for start, end, word in errors:
            highlighted_text += (
                text[last_pos:start]
                + f'<span style="color: red; font-weight: bold;">{word}</span>'
            )
            last_pos = end
        highlighted_text += text[last_pos:]
        return highlighted_text