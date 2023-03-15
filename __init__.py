from mycroft.skills.core import MycroftSkill, intent_handler, IntentBuilder
from mycroft.skills.intent_service import VocabularyIntentParser
from mycroft.util import create_daemon
from mycroft.util.log import LOG
import random
 
class GoodMorningSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.parser = None
        self.affirmations = [
            "You are loved",
            "You are deserving of a happy, fulfilling life, and you have the power to create that for yourself",
            "You are capable of achieving your goals and dreams",
            "You are doing your best, and that is enough",
            "You are not defined by your mistakes, and you have the power to learn and grow from them"
        ]
        self.other_options = [
            "What's the weather like today?",
            "Tell me a joke",
            "Play kiss FM"
        ]
 
    def initialize(self):
        self.parser = VocabularyIntentParser(self.handle_morning_good)
        self.register_vocab_intent("AffirmationIntent", self.handle_affirmation_intent)
        self.register_vocab_intent("YesIntent", self.handle_yes_intent)
        self.register_vocab_intent("NoIntent", self.handle_no_intent)
 
    @intent_handler('morning.good.intent')
def handle_morning_good(self, message):
    self.speak_dialog('morning.good')
    self.speak("Good morning, would you like to hear some words of affirmation?")
    self.parser.parse('AffirmationIntent', self.handle_affirmation_intent)
 
def handle_affirmation_intent(self, message):
    affirmation = random.choice(self.affirmations)
    self.speak_dialog("affirmation_response")
    self.speak(affirmation)
    self.speak("Would you like to hear more affirmations?")
    self.parser.parse('YesIntent', self.handle_yes_intent)
    self.parser.parse('NoIntent', self.handle_no_intent)
 
def handle_yes_intent(self, message):
    affirmation = random.choice(self.affirmations)
    self.speak(affirmation)
    self.speak("Would you like to hear more affirmations?")
    self.parser.parse('YesIntent', self.handle_yes_intent)
    self.parser.parse('NoIntent', self.handle_no_intent)
 
def handle_no_intent(self, message):
    self.speak_dialog("no-response")
    self.speak("Would you like to hear some other options?")
    self.parser.parse('YesIntent', self.handle_other_options)
    self.parser.parse('NoIntent', self.handle_exit_skill)
 
def handle_other_options(self, message):
    option = random.choice(self.other_options)
    self.speak(option)
    self.speak("Would you like to hear more options?")
    self.parser.parse('YesIntent', self.handle_other_options)
    self.parser.parse('NoIntent', self.handle_exit_skill)
 
def handle_exit_skill(self, message):
    self.speak("Okay, have a great day!")
    self.speak("Exiting the Good Morning Skill.")
    self.log.debug("Exiting the Good Morning Skill.")
    self.enclosure.skill_finished()
 
    @staticmethod
    def create_skill():
        return GoodMorningSkill()