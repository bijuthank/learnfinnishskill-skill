from mycroft import MycroftSkill, intent_file_handler


class Learnfinnishskill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('learnfinnishskill.intent')
    def handle_learnfinnishskill(self, message):
        self.speak_dialog('learnfinnishskill')


def create_skill():
    return Learnfinnishskill()

