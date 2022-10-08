from database.database import database
from libraries.Assistant.Assistant import Assistant
from libraries.Hander.Hander import Hander
from libraries.Connector.Connector import Connector
from libraries.Operation.Operation import Do
from threading import Thread
""" Sturucture of Horizon  
Identification: 
    <=>: Direct Connection 
    <->: Indirect Connection (with the help of main package)

                             Connector <=>  Assistant <-> Do <=> HORIZON <=> Database <-> Assistant   
                                            Hander    <->                             <->    Hander 
"""


if __name__ == "__main__":
    # Object Creation
    databaseHorizon = database()  # Database Object Creation
    assistant = Assistant(databaseHorizon)
    hander = Hander(databaseHorizon)
    connector = Connector(databaseHorizon)
    do = Do(databaseHorizon)
    handerThread = Thread(target=hander.main)
    handerThread.start()
    assistantThread = Thread(target=assistant.main)
    assistantThread.start()
    oldtext = ""
    while True:
        if databaseHorizon.shutdownProgram == 1:
            break
        if databaseHorizon.text == oldtext:
            print(databaseHorizon.text)
        oldtext = databaseHorizon.text
