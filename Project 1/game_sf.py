import numpy as np

def game():
    """Компьютер сам загадывает число и сам же его отгадывает

    Returns:
        количество попыток при отгадывании одного часла
        среднее количество попыток за 1000 повторений
    """
    
    def predict_number(num: int=1) -> int:
        """Угадывающая рандомное число

        Args:
            num (int, optional): загаданное число. Defaults to 1.

        Returns:
            int: количество попыток
        """
        count = 0
        min_ = 0
        max_ = 101
        
        while True:
            count += 1
            pred_number = round((min_ + max_) / 2)
            if pred_number > num:
                max_ = pred_number
            elif pred_number < num:
                min_ = pred_number
            else:
                break
        return count
    
    number = np.random.randint(1, 101) 
    count = predict_number(number)
    
    count_list = []
    num_list = np.random.randint(1, 101, size=1000) # Создаем список из 1000 чисел
    for i in num_list:
        count_list.append(predict_number(i))
    score = round(np.mean(count_list))
        
    return f'Число {number} было отгадано за {count} попыток. Среднее количество попыток за 1000 повторений {score}'

print(game())
    