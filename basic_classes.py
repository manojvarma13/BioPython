#!/usr/bin/env python3
import math

class Circle:
    def __init__(self, color: str, radius: float):
        self.color = color
        self.radius = radius

    def diameter(self):
        """Function to calculate the diameter of the circle"""
        return 2 * self.radius

    def circumference(self):
        """Function to calculate the circumference of the circle"""
        return 2 * self.radius * math.pi

    def isRed(self):
        """Function to check if circle is red"""
        return self.color == 'red'


class GraduateStudent:
    def __init__(self, first_name: str, last_name: str, year: int, major: str):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major

    def year_matriculated(self):
        """Function to calculate the year of the student graduation"""
        if self.year == 1:
            return 2019
        else:
            return (2020 - self.year)


def main():
    circle_obj = Circle('red', 7)

    print('The diameter of the circle is:', circle_obj.diameter())
    print('The circumference of the circle is:', circle_obj.circumference())
    print('Is the circle red?', circle_obj.isRed())

    graduation_obj = GraduateStudent('Sai Manoj', 'Tekumalla', 5, 'Bioinformatics')
    print('The year the student matriculated is:', graduation_obj.year_matriculated())

if __name__ == '__main__':
    main()