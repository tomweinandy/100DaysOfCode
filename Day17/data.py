# Data comes from https://opentdb.com

question_data_sample = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

question_data_geography = {"response_code": 0, "results": [
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Seoul is the capital of North Korea.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The flag of South Africa features 7 colours.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "easy",
                                      "question": "A group of islands is called an &#039;archipelago&#039;.",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Greenland is covered with grass and Iceland covered with ice.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "medium",
                                      "question": "The surface area of Russia is slightly larger than that of the dwarf planet Pluto.",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "The Republic of Malta is the smallest microstate worldwide.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "medium",
                                      "question": "There are no roads in\/out of Juneau, Alaska.",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy", "question": "Vatican City is a country.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "San Marino is the only country completely surrounded by another country.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "easy",
                                      "question": "There is a city called Rome in every continent on Earth.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The longest place named in the United States is Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, located near Webster, MA.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Alaska is the largest state in the United States.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Geography", "type": "boolean", "difficulty": "medium",
                                       "question": "The Southeast Asian island of Borneo is politically divided among 3 countries.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Vietnam is the only country in the world that starts with V. ", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "medium",
                                      "question": "Gothenburg is the capital of Sweden.", "correct_answer": "False",
                                      "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy", "question": "Ottawa is the capital of Canada.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "There exists an island named &quot;Java&quot;.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy", "question": "There are no deserts in Europe.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "&quot;Mongolia&quot; was a part of the now non-existent U.S.S.R.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "easy",
                                      "question": "Toronto is the capital city of the North American country of Canada.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The Sonoran Desert is located in eastern Africa.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "medium",
                                      "question": "The capital of the US State Ohio is the city of Chillicothe.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "St. Louis is the capital of the US State Missouri.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "medium",
                                      "question": "Antarctica is the largest desert in the world.",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "You could walk from Norway to North Korea while only passing through Russia.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "hard",
     "question": "Switzerland has four national languages, English being one of them.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "medium",
                                      "question": "Japan has left-hand side traffic.", "correct_answer": "True",
                                      "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Liechtenstein does not have an airport.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy", "question": "California is larger than Japan.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Norway has a larger land area than Sweden.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy", "question": "Tokyo is the capital of Japan.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Hungary is the only country in the world beginning with H.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "easy",
                                      "question": "New Haven is the capital city of the state of Connecticut in the United States.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Nova Scotia is on the east coast of Canada.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Geography", "type": "boolean", "difficulty": "hard",
                                       "question": "The two largest ethnic groups of Belgium are Flemish and Walloon. ",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Rhode Island is actually located on the US mainland, despite its name.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Geography", "type": "boolean", "difficulty": "medium",
                                       "question": "The title of the 1969 film &quot;Krakatoa, East_of Java&quot; is incorrect, as Krakatoa is in fact west of Java.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "There is an island in Japan called \u014ckunoshima, A.K.A. &quot;Rabbit Island&quot;, so named because of it&#039;s huge population of rabbits.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "hard",
     "question": "Only one country in the world starts with the letter Q.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium", "question": "Is Tartu the capital of Estonia?",
     "correct_answer": "False", "incorrect_answers": ["True"]}]}

question_data_film = {"response_code": 0, "results": [{"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "Han Solo&#039;s co-pilot and best friend, &quot;Chewbacca&quot;, is an Ewok.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "The movie &quot;The Nightmare before Christmas&quot; was all done with physical objects.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "Leonardo DiCaprio won an Oscar for Best Actor in 2004&#039;s &quot;The Aviator&quot;.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "The film &quot;2001: A Space Odyssey&quot; was released on December 31st, 2000.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "Matt Damon played an astronaut stranded on an extraterrestrial planet in both of the movies Interstellar and The Martian.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                                  "question": "There aren&#039;t any live-action clones in &quot;Star Wars: Episode III - Revenge of the Sith&quot;.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "The 2010 film &quot;The Social Network&quot; is a biographical drama film about MySpace founder Tom Anderson.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "The word &quot;Inception&quot; came from the 2010 blockbuster hit &quot;Inception&quot;.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                                  "question": "The colour of the pills in the Matrix were Blue and Yellow.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "In the original script of &quot;The Matrix&quot;, the machines used humans as additional computing power instead of batteries.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                                  "question": "The Xenomorph from the science fiction film &quot;Alien&quot; has acidic blood.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "Shaquille O&#039;Neal appeared in the 1997 film &quot;Space Jam&quot;.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "Ewan McGregor did not know the name of the second prequel film of Star Wars during and after filming.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "Samuel L. Jackson had the words, &#039;Bad Motherf*cker&#039; in-scripted on his lightsaber during the filming of Star Wars.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "In Alfred Hitchcock&#039;s film &#039;Psycho&#039; it is said he used chocolate syrup to simulate the blood in the famous shower scene from ",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "In the original Star Wars trilogy, David Prowse was the actor who physically portrayed Darth Vader.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "In the original Star Wars trilogy, Alec Guinness provided the voice for Darth Vader.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "hard",
                                  "question": "&quot;Cube&quot;, &quot;Cube 2: Hypercube&quot; and &quot;Cube Zero&quot; were directed by the same person.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                                  "question": "Sean Connery wasn&#039;t in &quot;Indiana Jones and the Kingdom of the Crystal Skull&quot; because he found retirement too enjoyable.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "In the movie The Revenant, DiCaprio&#039;s character hunts down the killer of his son.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "Brandon Routh plays the titular character in the movie &quot;John Wick&quot;.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "George Lucas directed the entire original Star Wars trilogy.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                                  "question": "Joan Cusack starred in the 2009 disaster movie, &quot;2012&quot;.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "&quot;Minions&quot; was released on the June 10th, 2015.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "hard",
                                  "question": "The weapon Clint Eastwood uses in &quot;Dirty Harry&quot; was a .44 Automag.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "Actor Tommy Chong served prison time.", "correct_answer": "True",
                                  "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                                  "question": "&quot;Foodfight!&quot; earned less than $80,000 at box office.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                                  "question": "The movie &quot;Tron&quot; received an Oscar nomination for Best Visual Effects.",
                                  "correct_answer": "False", "incorrect_answers": ["True"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "hard",
                                  "question": "YouTube personality Jenna Marbles served as an executive producer of the film Maximum Ride (2016).",
                                  "correct_answer": "True", "incorrect_answers": ["False"]},
                                 {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                                  "question": "The original ending of &quot;Little Shop Of Horrors&quot; has the plants taking over the world.",
                                  "correct_answer": "True", "incorrect_answers": ["False"]}]}
