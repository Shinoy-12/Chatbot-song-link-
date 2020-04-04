# Installation

You can install Rasa Open Source using pip (requires Python 3.6 or 3.7).

$ pip3 install rasa

You also need to install a spaCy English language model. You can install it by running:

$ pip install rasa[spacy]
$ python -m spacy download en_core_web_md
$ python -m spacy link en_core_web_md en```

ref - https://rasa.com/docs/rasa/user-guide/installation/

# Chatbot-sends-you-song-
It's a funny ML based conversational chatbot which sends you list of song(link) based on your choice all these songs are stored in MySql Database . It is a very basic conversational bot but it will definitely help others to start building one.

RASA components for developing a ML based chatbot
RASA- An opensource bot building framework, is used to build this bot. RASA is divided into two major parts in terms of developing a chatbobt.

RASA NLU - Rasa NLU is an open-source natural language processing tool for intent classification, response retrieval and entity extraction in chatbots.

RASA CORE - It works as a dialogue management for bot and keeps track of a conversation with the user.

RASA NLU

nlu.md - is a file which contains the training data for Rasa NLU model. This data consists of the example user queries alongside the corresponding intents and entities.

     ref:-https://rasa.com/docs/rasa/nlu/training-data-format/

RASA CORE

stories.md - is a file which contains training data for the dialogue model. This data consists of stories — actual conversations between a user and an assistant written in a Rasa format, where user inputs are expressed as corresponding intents and entities, and the responses of the assistant are expressed as actions.


         ref:- https://rasa.com/docs/rasa/core/stories/

domain.yml -is a file which contains the configuration of the assistant’s domain. It consists of the following pieces:

1. Intents and Entities that are defined in Rasa NLU training data examples;

2. Slots which work like placeholders for saving the details that the assistant has to remember throughout the conversation

3. Templates which define the text responses that an assistant should return when the corresponding utterances are predicted

4. Actions which the assistant should be able to predict and execute.

         ref:- https://rasa.com/docs/rasa/core/domains/

configuration
config.yml - consists configuration pipeline for the training of NLU and CORE - Choosing an NLU and a CORE pipeline allows you to customize your model and finetune it on your dataset.

         nlu_config_reference:- https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/
         core_config_reference:- https://rasa.com/docs/rasa/core/policies/

## How to use this Project--
1. Clone or download this repo into your computer
2. Make sure to have all the dependency in your computer
3. Set your working directory to this downloaded folder in terminal
4. Open terminal.
5. Start your MySql Server
4. $ rasa train (trains your model) this will start a port on 5055 which will handl custom actions
5. $ rasa run actions (Starts an action server using the Rasa SDK.)
6. $ rasa shell --endpoints endpoints.yml

For more Command Line Interface ref- (https://rasa.com/docs/rasa/user-guide/command-line-interface/)


B00000M Are ready to freshen up!!!!!! Now you can talk to your chatbot.

## How to store your Data in MySql Database-
-> You can use the simple approach and do it manually by entering each links into your database.
-> Or you can create a csv file and then store in into mysql database
 
### PS- Ignore song links this bot is only for testing.

## Thank You!
