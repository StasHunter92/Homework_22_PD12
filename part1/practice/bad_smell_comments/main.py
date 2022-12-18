# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move_on_field(self, field: any, x_coordinate: int, y_coordinate: int, direction: str, can_fly: bool,
                      can_creep: bool, speed: int = 1):

        if can_fly and can_creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if can_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coordinate + speed
                new_x = x_coordinate
            elif direction == 'DOWN':
                new_y = y_coordinate - speed
                new_x = x_coordinate
            elif direction == 'LEFT':
                new_y = y_coordinate
                new_x = x_coordinate - speed
            elif direction == 'RIGHT':
                new_y = y_coordinate
                new_x = x_coordinate + speed

        if can_creep:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coordinate + speed
                new_x = x_coordinate
            elif direction == 'DOWN':
                new_y = y_coordinate - speed
                new_x = x_coordinate
            elif direction == 'LEFT':
                new_y = y_coordinate
                new_x = x_coordinate - speed
            elif direction == 'RIGHT':
                new_y = y_coordinate
                new_x = x_coordinate + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
