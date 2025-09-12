class LibraryBook:
    def __init__(self, title, secret_code):
        self.title = title
        self._is_taken =False
        self.__secret_code = secret_code

    def take_book(self, code):
        if code == self.__secret_code and not self._is_taken:
            self._is_taken = True
            return f"Книга '{self.title}' успешно взята!"
        elif code != self.__secret_code:
            return "Неверный секретный код!"
        elif self._is_taken:
            return f"Книга '{self.title}' уже занята."

    def return_book(self):
        if self._is_taken:
            self._is_taken = False
            return f"Книга '{self.title} возвращена."
        else:
            return f"Книга '{self.title} свободна."

from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentSystem):
    def pay(self, amount):
        return f"Оплата {amount} сом. произведена через банковскую карту."

    def refund(self, amount):
        return f"Возврат {amount} сом через банковскую карту."

class CryptoPayment(PaymentSystem):
    def pay(self, amount):
        return f"Оплата {amount} USDT произведена через криптовалюту."

    def refund(self, amount):
        return f"Возврат {amount} USDT через криптовалюту."

book = LibraryBook("Грозный перевал", "secret123")


print(book.take_book("wrong"))      # Неверный секретный код
print(book.take_book("secret123"))  # Успешно взята
print(book.take_book("secret123"))
print(book.return_book())
print(book.return_book())

card = CardPayment()
crypto = CryptoPayment()

print(card.pay(500))
print(card.refund(200))
print(crypto.pay(100))
print(crypto.refund(50))
