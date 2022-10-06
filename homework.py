from dataclasses import dataclass
from typing import ClassVar, Dict, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    SENTENCE: ClassVar[str] = (
        'Тип тренировки: {0}; '
        'Длительность: {1:.3f} ч.; '
        'Дистанция: {2:.3f} км; '
        'Ср. скорость: {3:.3f} км/ч; '
        'Потрачено ккал: {4:.3f}.')
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return self.SENTENCE.format(self.training_type,
                                    self.duration,
                                    self.distance,
                                    self.speed,
                                    self.calories)


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
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError

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
    CAL_1: int = 18
    CAL_2: int = 20

    def get_spent_calories(self) -> float:
        return ((self.CAL_1 * self.get_mean_speed() - self.CAL_2)
                * self.weight / self.M_IN_KM * self.duration * 60)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CAL_1: float = 0.035
    CAL_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.CAL_1 * self.weight
                + (self.get_mean_speed()**2 // self.height)
                * self.CAL_2 * self.weight) * (self.duration * 60))


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    CAL_1: float = 1.1
    CAL_2: float = 2

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
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + self.CAL_1) * self.CAL_2 * self.weight


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
