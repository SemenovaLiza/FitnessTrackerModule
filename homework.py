from dataclasses import dataclass
from typing import Dict, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        sentence = (f'Тип тренировки: {self.training_type}; '
                    f'Длительность: {self.duration:.3f} ч.; '
                    f'Дистанция: {self.distance:.3f} км; '
                    f'Ср. скорость: {self.speed:.3f} км/ч; '
                    f'Потрачено ккал: {self.calories:.3f}.')
        return sentence


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance()
        return distance / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())
        return info


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        cal_1: int = 18
        cal_2: int = 20
        speed = self.get_mean_speed()
        time = self.duration * 60
        return (cal_1 * speed - cal_2) * self.weight / self.M_IN_KM * time


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        cal_1: float = 0.035
        cal_2: float = 0.029
        speed = self.get_mean_speed()
        time = self.duration * 60
        height = self.height
        weight = self.weight
        return (cal_1 * weight + (speed**2 // height) * cal_2 * weight) * time


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        M_IN_KM = self.M_IN_KM
        return self.length_pool * self.count_pool / M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        cal_1: float = 1.1
        cal_2: float = 2
        speed = self.get_mean_speed()
        return (speed + cal_1) * cal_2 * self.weight


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_code: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    show_data = (training_code[workout_type](*data))
    return show_data


def main(training: Training) -> None:
    """Главная функция."""
    show = training.show_training_info()
    print(show.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
