from database.database import database
from libraries.Operation.do import assistantFunction, handerFunction


""" Sturucture of Horizon  
Identification: 
    <=>: Direct Connection 
    <->: Indirect Connection (with the help of main package)

                                            Assistant <-> Do <=> HORIZON <=> Database <-> Assistant   
                                            Hander    <->                             <->    Hander 
"""


if __name__ == "__main__":
    databaseHorizon = database()
    functionAssistant = assistantFunction(databaseHorizon)
    functionHander = handerFunction(databaseHorizon)
    while True:
        a = input("Enter Input:")
        if a == "exit":
            break
        elif a == "OpenCamera":
            functionAssistant.startHander()
        elif a == "CloseCamera":
            functionAssistant.stopHander()
