from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking, play_mp3
import os


class LearnFinnishskill(MycroftSkill):

    path_tranlated_file = "/tmp/finnish.mp3"

    def translated_to_finnish(self, text):
        translated = translate(text, "fi")
        self.speak_finnish(translated)

    def speak_finnish(self, sentence):
        wait_while_speaking()
        get_sentence = 'wget -q -U Mozilla -O ' + self.path_translated_file + \
                       '"https://translate.google.com/translate_tts?ie=UTF-8&tl=pt&q=' + \
                       str(sentence) + '&client=tw-ob' + '"'

        os.system(get_sentence)
        play_mp3(self.path_tranlated_file)

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('learnFinnishskill.intent')
    def handle_learnFinnishSkill(self, message):
        # wait = True makes Mycroft wait until speech is finished playing before continuing
        self.speak_dialog('learnfinnishskill', wait=True)
        self.speak_finnish("moi")


def create_skill():
    return LearnFinnishSkill()

