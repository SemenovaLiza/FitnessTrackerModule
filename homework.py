from dataclasses import dataclass
from typing import ClassVar, Dict, Type


@dataclass
class InfoMessage:
    """Represents an informational message about a training session.

    Attributes:
        training_type (str): Name of the training class.
        duration (float): Duration of the training in hours.
        distance (float): Distance(km) covered by user.
        speed (float): User's average speed in km/h.
        calories (float): Total number of calories burned during the training.
    """
    SENTENCE: ClassVar[str] = (
        'Training type: {0}; '
        'Duration: {1:.3f} h.; '
        'Distance: {2:.3f} km; '
        'Speed: {3:.3f} km/h; '
        'Calories: {4:.3f}.')
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        """This method generates a message summarizing the training 
            
        Returns:
            str: A formatted string containing training details.
        """
        return self.SENTENCE.format(self.training_type,
                                    self.duration,
                                    self.distance,
                                    self.speed,
                                    self.calories)


class Training:
    """Base class representing a generic training session.
    This class serves as a parent for specific types of training, 
    providing common attributes and methods.

    Attributes:
        action (int): Number of actions performed(steps or strokes).
        duration (float): Duration of the training in hours.
        weight(float): User's weight in kg.

    Constants:
        LEN_STEP (float): Distance covered per action (step or stroke).
        M_IN_KM (int): Conversion factor from meters to kilometers.
    """
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
        """Calculates the total distance covered during training.

        Returns:
            float: Distance covered in km.
        """
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Calculates the average speed during training.

        Returns:
            float: Average speed in km/h.
        """
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Calculates the number of calories burned during training.
        This method must be overridden in subclasses.

        Raises:
            NotImplementedError: If called directly from the base class.

        Returns:
            float: The number of calories burned.
        """
        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """Creates an information message about the completed training.

        Returns:
            InfoMessage: An object containing details of the training session.
        """
        info = InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())
        return info


class Running(Training):
    """Represents a running training session.

    Attributes:
        Inherits all attributes from the Training class.

    Constants:
        CAL_1 (int): Multiplier used for calorie calculation.
        CAL_2 (int): Subtractor used for calorie calculation.
    """
    CAL_1: int = 18
    CAL_2: int = 20

    def get_spent_calories(self) -> float:
        """Calculates calories burned during a running session.

        Returns:
            float: The number of calories burned.
        """
        return ((self.CAL_1 * self.get_mean_speed() - self.CAL_2)
                * self.weight / self.M_IN_KM * self.duration * 60)


class SportsWalking(Training):
    """Represents a sports walking training session.

    Attributes:
        Inherits all attributes from the Training class.
        height (float): User's height in cm.

    Constants:
        CAL_1 (float): First multiplier for calorie calculation.
        CAL_2 (float): Second multiplier for calorie calculation.
    """
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
        """Calculates calories burned during a walking session.

        Returns:
            float: The number of calories burned.
        """
        return ((self.CAL_1 * self.weight
                + (self.get_mean_speed()**2 // self.height)
                * self.CAL_2 * self.weight) * (self.duration * 60))


class Swimming(Training):
    """Represents a swimming training session.

    Attributes:
        Inherits all attributes from the Training class.
        length_pool (float): Length of the pool in meters.
        count_pool (int): Number of times the pool was crossed.

    Constants:
        LEN_STEP (float): Distance covered per swimming stroke.
        CAL_1 (float): First multiplier for calorie calculation.
        CAL_2 (float): Second multiplier for calorie calculation.
    """
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
        """Calculates the average swimming speed.

        Returns:
            float: The average speed in km/h.
        """
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Calculates calories burned during a swimming session.

        Returns:
            float: The number of calories burned.
        """
        return (self.get_mean_speed() + self.CAL_1) * self.CAL_2 * self.weight * self.duration


def read_package(workout_type: str, data: tuple) -> Training:
    """Creates a training object based on the given workout type and data.

    Arguments:
        workout_type (str): Key representing the type of training.
        data (tuple): Tuple containing attributes for the corresponding training class.

    Returns:
        Training: An instance of the corresponding training class.
    """
    training_code: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    show_data = (training_code[workout_type](*data))
    return show_data


def main(training: Training) -> None:
    """Displays training details.

    Calls `show_training_info()` for the given training instance 
    and prints the formatted training message.

    Arguments:
        training (Training): A training instance.
    """
    show = training.show_training_info()
    print(show.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', (720, 1, 80, 25, 40)),
        ('RUN', (15000, 1, 75)),
        ('WLK', (9000, 1, 75, 180)),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

# Add later: validation and errors handling