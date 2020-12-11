

def get_coordinates(flat_number, stages, flat_per_stage):
    flats_per_block = stages * flat_per_stage
    if flat_number % flats_per_block:
        target_block = (flat_number // flats_per_block) + 1
    else:
        target_block = (flat_number // flats_per_block)
    temp_flats = flat_number - int(flat_number // flats_per_block) * flats_per_block
    if temp_flats == 0:
        return [target_block, stages]
    else:
        if temp_flats % flat_per_stage:
            target_stage = temp_flats // flat_per_stage + 1
        else:
            target_stage = temp_flats // flat_per_stage
    return [target_block, target_stage]



    # ----------------------------------
    # """Задание 1"""


if __name__ == '__main__':
	# flat_number = input("Enter your flat: ")
	# stages = input("Enter stages: ")
	# flat_per_stage = input("Enter flat on the floor: ")
    print(get_coordinates(40, 2, 10))

    # ----------------------------------
    """Задача 1. Курьер
    Вам известен номер квартиры, этажность дома и количество квартир на этаже. Задача: написать функцию, 
    которая по заданным параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.
    """

