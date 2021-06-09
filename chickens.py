class Chicken:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.total_eggs = 0

    @property
    def eggs_laid_today(self) -> int:
        """Number of eggs laid today"""
        return self.eggs_laid_today

    @property
    def days_left_to_live(self) -> int:
        """Days left to live as a chicken"""
        return self.days_left_to_live

    def add_egg_to_total(self, num_eggs: int) -> None:
        """ Add eggs laid to total eggs"""
        self.total_eggs += num_eggs

    def total_eggs_laid_per_age(self) -> float:
        """ How many total eggs has the chicken laid ?"""
        return self.total_eggs / self.age
