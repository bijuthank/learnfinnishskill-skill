from mycroft import MycroftSkill, intent_file_handler


class LearnFinnishskill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('learnFinnishskill.intent')
    def handle_learnFinnishSkill(self, message):
        self.speak_dialog('learnfinnishskill')


def create_skill():
    return LearnFinnishSkill()

