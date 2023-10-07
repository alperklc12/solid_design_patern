from abc import ABC, abstractmethod


class IMessageServerCls(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass


class EmailServiceCls(IMessageServerCls):
    def send(self, massage, receiver):
        return f'Sending email: {massage} to {receiver}'


class SmsServiceCls(IMessageServerCls):
    def send(self, massage, receiver):
        return f'Sending email: {massage} to {receiver}'


class NotificationService:
    def __init__(self, message_service: IMessageServerCls):
        self.message_service = message_service

    def send_notification(self, message, receiver):
        return self.message_service.send(message, receiver)

