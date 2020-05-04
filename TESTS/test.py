import os
import sys
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'DAL'))

from chatbot.trainAI import TrainAI

ai = TrainAI()
ai.train()

definition = "Coronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19. COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019."
transmision = "The virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, sneezes, or speaks. These droplets are too heavy to hang in the air. They quickly fall on floors or surfaces. You can be infected by breathing in the virus if you are within 1 metre of a person who has COVID-19, or by touching a contaminated surface and then touching your eyes, nose or mouth before washing your hands."
symptoms = "Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  People above 60, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness. Common symptoms include: fever; tiredness; and, dry cough. Other symptoms include: shortness of breath; aches and pains; sore throat; and, sometimes, diarrhoea, nausea, or a runny nose."
prevention = "To prevent infection and to slow transmission of COVID-19, do the following: wash your hands regularly with soap and water, or clean them with alcohol-based hand rub; maintain at least 1 metre distance between you and people coughing or sneezing; avoid touching your face; cover your mouth and nose when coughing or sneezing; stay home if you feel unwell; refrain from smoking and other activities that weaken the lungs; and, practice physical distancing by avoiding unnecessary travel and staying away from large groups of people."
treatment = "To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. However, those affected should receive care to relieve symptoms. People with serious illness should be hospitalized. Most patients recover thanks to supportive care. While some western, traditional or home remedies may provide comfort and alleviate symptoms of COVID-19, there is no evidence that current medicine can prevent or cure the disease. WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19. However, there are several ongoing clinical trials that include both western and traditional medicines. WHO will continue to provide updated information as soon as clinical findings are available."
probability = "The risk depends on where you  are - and more specifically, whether there is a COVID-19 outbreak unfolding there. For most people in most locations the risk of catching COVID-19 is still low. However, there are now places around the world (cities or areas) where the disease is spreading. For people living in, or visiting, these areas the risk of catching COVID-19 is higher. Governments and health authorities are taking vigorous action every time a new case of COVID-19 is identified. Be sure to comply with any local restrictions on travel, movement or large gatherings. Cooperating with disease control efforts will reduce your risk of catching or spreading COVID-19. COVID-19 outbreaks can be contained and transmission stopped, as has been shown in China and some other countries. Unfortunately, new outbreaks can emerge rapidly. It’s important to be aware of the situation where you are or intend to go. WHO publishes daily updates on the COVID-19 situation worldwide. You can see these at https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/"
worry = "Illness due to COVID-19 infection is generally mild, especially for children and young adults. However, it can cause serious illness: about 1 in every 5 people who catch it need hospital care. It is therefore quite normal for people to worry about how the COVID-19 outbreak will affect them and their loved ones. We can channel our concerns into actions to protect ourselves, our loved ones and our communities. First and foremost among these actions is regular and thorough hand-washing and good respiratory hygiene. Secondly, keep informed and follow the advice of the local health authorities including any restrictions put in place on travel, movement and gatherings. Learn more about how to protect yourself at https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public"
critical = "While we are still learning about how COVID-2019 affects people, older persons and persons with pre-existing medical conditions (such as high blood pressure, heart disease, lung disease, cancer or diabetes)  appear to develop life-threatening illness more often than others."
antibiotics = "No. Antibiotics do not work against viruses, they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. Antibiotics should not be used as a means of prevention or treatment of COVID-19. They should only be used as directed by a physician to treat a bacterial infection. "
incubation = "The 'incubation period' means the time between catching the virus and beginning to have symptoms of the disease. Most estimates of the incubation period for COVID-19 range from 1-14 days, most commonly around five days. These estimates will be updated as more data become available."
origin = "Currently, the source of SARS-CoV-2, the coronavirus (CoV) causing COVID-19 is unknown. All available evidence suggests that SARS-CoV-2 has a natural animal origin and is not a constructed virus. SARS-CoV-2 virus most probably has its ecological reservoir in bats. SARS-CoV-2, belongs to a group of genetically related viruses, which also include SARS-CoV and a number of other CoVs isolated from bats populations. MERS-CoV also belongs to this group, but is less closely related."
airborne = "The virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, sneezes, or speaks. These droplets are too heavy to hang in the air. They quickly fall on floors or surfaces. You can be infected by breathing in the virus if you are within 1 metre of a person who has COVID-19, or by touching a contaminated surface and then touching your eyes, nose or mouth before washing your hands."



class TestResponse(unittest.TestCase):
    
    def test_name(self):

        self.assertEqual(ai.chat("what is your name"), "I am Covid Chatbot :)", "Wrong response on 'who' tag")

    def test_definition(self):
        self.assertEqual(ai.chat("What is COVID-19?"), definition, "Wrong response on 'definition' tag")
        self.assertEqual(ai.chat("What is coronavirus?"), definition, "Wrong response on 'definition' tag")
        
    def test_transmision(self):
        self.assertEqual(ai.chat("How do you catch Coronavirus?"), transmision, "Wrong response on 'transmision' tag")
        self.assertEqual(ai.chat("How is COVID-19 transmitted?"), transmision, "Wrong response on 'transmision' tag")
        self.assertEqual(ai.chat("How does it spread?"), transmision, "Wrong response on 'transmision' tag")

    def test_symptoms(self):
        self.assertEqual(ai.chat("What are the symptoms?"), symptoms, "Wrong response on 'symptoms' tag")
        self.assertEqual(ai.chat("How can I know that I have it?"), symptoms, "Wrong response on 'symptoms' tag")
        self.assertEqual(ai.chat("What are the symptoms of COVID-19?"), symptoms, "Wrong response on 'symptoms' tag")

    def test_prevention(self):
        self.assertEqual(ai.chat("How do I avoid COVID-19?"), prevention, "Wrong response on 'prevention' tag")
        self.assertEqual(ai.chat("How do I prevent COVID-19?"), prevention, "Wrong response on 'prevention' tag")

    def test_treatment(self):
        self.assertEqual(ai.chat("Is there a cure?"), treatment, "Wrong response on 'treatment' tag")
        self.assertEqual(ai.chat("How do I treat Coronavirus?"), treatment, "Wrong response on 'treatment' tag")
        self.assertEqual(ai.chat("Is there a vaccine for COVID-19?"), treatment, "Wrong response on 'treatment' tag")

    def test_probability(self):
        self.assertEqual(ai.chat("How likely am I to catch COVID-19?"), probability, "Wrong response on 'probability' tag")

    def test_worry(self):
        self.assertEqual(ai.chat("Should I worry about COVID-19?"), worry, "Wrong response on 'worry' tag")

    def test_critical(self):
        self.assertEqual(ai.chat("Who is more likely to die from COVID-19?"), critical, "Wrong response on 'critical' tag")
        self.assertEqual(ai.chat("How likely will one survive COVID-19?"), critical, "Wrong response on 'critical' tag")

    def test_antibiotics(self):
        self.assertEqual(ai.chat("Are antibiotics effective on COVID-19?"), antibiotics, "Wrong response on 'antibiotics' tag")
        self.assertEqual(ai.chat("Can I use antibiotics to treat COVID-19?"), antibiotics, "Wrong response on 'antibiotics' tag")

    def test_incubation(self):
        self.assertEqual(ai.chat("How long does it take before symptoms show up?",), incubation, "Wrong response on 'incubation' tag")

    def test_origin(self):
        self.assertEqual(ai.chat("Where did COVID-19 come from?"), origin, "Wrong response on 'origin' tag")
        self.assertEqual(ai.chat("What is the origin of COVID-19?"), origin, "Wrong response on 'origin' tag")

    def test_airborne(self):
        self.assertEqual(ai.chat("Can you catch COVID-19 by air?"), airborne, "Wrong response on 'airborne' tag")


if __name__ == "__main__":
    unittest.main()