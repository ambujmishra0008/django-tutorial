from djchoices import DjangoChoices, ChoiceItem


class AuthorStatus(DjangoChoices):
    ACTIVE = ChoiceItem("active")
    INACTIVE = ChoiceItem("inactive")
    CLOSE = ChoiceItem("close")