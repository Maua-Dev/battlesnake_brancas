import random
from typing import List
from .Ponto import Ponto

from .frases_enum import FrasesEnum

musica1 = ['When my roommate comes into the room looking for his car keys', "I don't say it yet", 'And when he gets me off the couch to check underneath the couch cushions', "I don't say it yet, no", 'And then when he says out loud "I wonder where my car keys are"', "I still don't say it (I still don't say it yet)", 'But then he asks me "Do you know where my car keys are?"', 'I look at him in his face, and I say', 'HYCYBH?', 'Ski-dap, ba-dap, BH', "I have not seen your keys, but since you're askin' me", 'You better check up that BH', "Of course I'm not serious", "I don't think it's up inside your big brown business", "But a funny thing to say to someone who's lost their shit and is stressed out visibly", 'When I see the best man start to sweat', "I don't say it yet (Ski-dap, ba-dap)", 'When I see that little ring bearer cunt getting yelled at by his mum', "Oh, I still don't say it", 'When I see the groom asking the vicar if they can wait just another fifteen minutes', 'I do not say it (Ski-bap, ba-da)', 'And when the father of the bride starts organizing an ad-hoc emu bob of the courtyard area', 'I want to, but I do not say it', "It's the eleventh hour with three hundred congregates under God's roof", 'The vicar approaches the mic, and suddenly, all of the chatter goes mute', "He says that they've misplaced the rings", 'Could anyone possibly know where they are?', 'I know it\'s my time, and all heads turn as I stand and say, "Vicar!"', 'HYCYBH?', 'Ski-dap, ba-dap, BH', '"I have not seen your ring, but have you checked your ring?"', 'And by "ring, " I mean BH', 'Love is patient; love is kind', 
'But if you ask me where you can find', "Literally anything you've lost before", "I'm gonna suggest that it's up your BH", '"Where\'s my phone?" "Is it up your BH?"', '"I lost my loan." "Have you checked up your b-hole?"', '"I\'m losing my patience." "Check your anus"', '"Where is your class?" "I think it\'s stuck up your ass"', '"I just lost my grandma"', '"Oh my god, I\'m so sorry"', "Are you capable of not saying she's up my asshole?", 'Of course, my condolences', "I'm not looking for a silly joke right now", 'Yeah, yeah... what are you looking for?', 'Honestly, just like, a shoulder to crâ€”', 'HYCYBH?', 'Ski-dap, ba-dap, BH', "Maybe you'll find your dead grandma up there, too", "Oh, I fuckin' got you, BH", 'My family hate me', "This might be the reason that I've got no close friends", "Fuckin' worth it, bab"]

musica2 = ['Let me tell a little story about a man long time ago', "He was the quickest draw in the wild west by the name of Smokin' Joe", "It's Smokin' Joe!", 'Hit the floor', "But he didn't own no six-gun", "Lemme tell you what he'd do", 
'When the varmint rode into town', 'He\'d shoot \'em down with a big fat "f.y.!"', "Smokin' Joe! (it's Smokin' Joe Rudeboy!)", 'Lemme make sure I heard you right', '$7.50 for large soy cappucino', 'Lemme get my wallet', 'F.Y.!', "Smokin' Joe! (it's Smokin' Joe Rudeboy!)", 'Lemme make sure I heard you right', "Even though I'm not with Amazon you're calling me to tell me", 'That my profile has been hacked?', 'F.Y.!', 'And so Joe held the law in the town in which he lived', 'Yeah! Only stupid m.f.k. would talk s. around Rudeboy', 'With his whiplash wrist', "Gon' get it now!", 'Leroy "Two Gun" Jenkins thought that he could surely win', 'But before Leroy could blink he was told to sit and spin', "Why don't you take it for a ride now?", 'The Mongoose Mountain Gang played dirty with a twenty-man crew', 'But tales are told that Joe grew eighteen arms', 'That day as a gift from Vishnu', 'And as he rose in fame', 'Every quickdraw outlaw came to the man', 'They heard whose fists would burn when he flipped the bird', "Smokin' Joe! (it's Smokin' Joe Rudeboy!)", 'Lemme make sure I heard you right', 'You wanna refund the money that I spent', 'In your shop with a store credit?', 'F.Y.!', "Smokin' Joe! (it's Smokin' Joe Rudeboy!)", 'Lemme make sure I heard you right', 'Everybody brought a platter to my fancy birthday dinner', 'But you brought soda water?', 'F.Y.!', 'He got that name because his finger burns hot like the sun', "And leaves you smokin' when he's done", "It's just as well that Joe is fast as hell", "Cause in every duel he won I'm not sure", 'Joe knew that they had a literal gun', "I know that they're packing heat", "And I know that they know that I'm the man to beat", 'But when I step onto the street with a jingle in my feet', 'They know that I know that they know that they can', 'F. themself!', 'Some say many years ago', "Before Joseph Rudeboy was Smokin' Joe", 'He had a wife; her name was Bo', 'Bo was with child in a happy home', 'But into town an outlaw came', 'Who wore a velvet cloak like a bloodstain', "Now Bo didn't like Joe using no gun", 'So Bo told Joe to f.ing run', '"You gotta bring back help!" (Run fast Joe, fast Joe)', 'Lemme stay and fight!', 'But Bo said "No guns, you\'ve got to go!"', 'Joeseph Rudeboy was too slow', "For a child that he'd never know", "Joeseph Rudeboy you're too slow", 'Burning inside Joeseph died but from the ash the man who rose was', "Smokin' Joe! (it's Smokin' Joe Rudeboy!)", "He's a human pheonix", "Yes, that's the word", 'I heard he was born in a fire', "And rides a pair of flamin' birds", "Smokin' Joe! (it's Smokin' Joe Rudeboy!)", "I heard he's never shot no-one but he's", 'Still locked up half of the wild west', "Lookin' for a velvet-wearing son-of-a-gun", 'One day an outlaw came to town', "Come out here Smokin' Joe", "You're just as well already dead", 'He wore a velvet cloak but Joe saw red', 'And on the street the fateful pair did meet', 'All the townsfolk came to watch when they knew', 'Joe was gonna tell someone to fâ€”', 'Their eyes were locked what seemed like three eternities', 'To Joe the velvet man seemed different', 'From how he remembered him to be', "But it was all the same to Smokin' Joe, who'd been through hell", "He'd dreamt every night the last eighteen years", 'Of telling this guy to f. himself', "But when Joe went to ball his hand into a flamin' fist", 'The outlaw shot him first with a', 'Middle finger that looked just like his', "And as Joe fell he beheld the outlaw's face", "A young girl who'd seen it all", 'And grew up in a terrible place', 
'Whose mother once told Joeseph', 'To run and bring back help', 'A girl who thought her father had run out to save himself', "Smokin' Joe! (it's Smokin' Joe Rudeboy!)", 'Lemme make sure I heard you right', "You been telling everybody I'm a deadbeat daddy", "Didn't know I tried to save ya?", 'Yeah', 'F.Y., daughter!', "Smokin' Joe! (it's Smokin' Joe Rudeboy!)", 'Lemme make sure I heard you right', 'Now I found my father and I learnt the truth we can be reunited?', "That's right", 'F.Y., old man']

class Utils:
    @staticmethod
    def escolhe_frase():
        conjunto = Utils.escolhe_conjunto_de_frases()
        
        frase = random.choice(random.choice([musica1, musica2]))
        return frase
        

    @staticmethod
    def escolhe_conjunto_de_frases() -> str:   
        return random.choice(list(FrasesEnum)).value.lower()
    
    @staticmethod
    def ponto_uniq(l: List[Ponto]) -> List[Ponto]:
        l_str = list(set([str(ponto) for ponto in l]))
        return [Ponto(ponto_string=ponto) for ponto in l_str]
