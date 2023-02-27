from mycroft import MycroftSkill, intent_file_handler


class Generatemessage(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('generatemessage.intent')
    def handle_generatemessage(self, message):
        self.speak_dialog('generatemessage')


def create_skill():
    return Generatemessage()

