from LetterFactory import LetterFactory

class Client:

    letter_factory = LetterFactory()
    a = letter_factory.create_letter('a')
    a.display(1, 2)

    b = letter_factory.create_letter('b')
    b.display(5, 6)

    a2 = letter_factory.create_letter('b')
    a2.display(7, 0)