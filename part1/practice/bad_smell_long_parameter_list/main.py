# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field: any, unit_type: str, speed: int | float = 1):
        self._field = field
        self._type = unit_type
        self._speed = speed

    def move(self, x_coord: int | float, y_coord: int | float, direction: str):
        speed = self._get_speed()

        if direction == 'UP':
            self._field.set_unit(x=x_coord, y=y_coord + speed, unit=self)
        elif direction == 'DOWN':
            self._field.set_unit(x=x_coord, y=y_coord - speed, unit=self)
        elif direction == 'LEFT':
            self._field.set_unit(x=x_coord - speed, y=y_coord, unit=self)
        elif direction == 'RIGTH':
            self._field.set_unit(x=x_coord + speed, y=y_coord, unit=self)

    def _get_speed(self) -> float | Exception:
        if self._type == 'fly':
            return self._speed * 1.2
        elif self._type == 'crawl':
            return self._speed * 0.5
        else:
            return ValueError('Рожденный ползать летать не должен!')
