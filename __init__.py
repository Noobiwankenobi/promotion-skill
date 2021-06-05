from mycroft import MycroftSkill, intent_file_handler


class Promotion(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('promotion.intent')
    def handle_promotion(self, message):
        self.speak_dialog('promotion')


def create_skill():
    return Promotion()

