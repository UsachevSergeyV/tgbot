

#хранилище состояний
State= {}



#функция возвращает информацию их хранилища состояний
def getStete(user_id):
    if user_id in State:
        return State[user_id]
    else:
        return None

#добавляем информацию о состоянии
#если пользователь такой не существует то добавим его в пул,
#Установим ему в соответствующее состояние значение
def setStete(user_id,state,value):
    if user_id not in State:
        State[user_id] = {}
    State[user_id][state] = value

