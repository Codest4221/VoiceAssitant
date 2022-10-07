from database.database import database
from libraries.Operation.do import assistantFunction,handerFunction


""" Sturucture of Horizon  
Identification: 
    <=>: Direct Connection 
    <->: Indirect Connection (with the help of main package)

                                            Assistant <-> Do <=> HORIZON <=> Database <-> Assistant   
                                            Hander    <->                             <->    Hander 
"""




if __name__ == "__main__":
    databaseHorizon = database()
    functionAssistant = assistantFunction()
    functionHander = handerFunction()