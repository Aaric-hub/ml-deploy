from typing import List, Union


def ml_trails(air_temp,process_temp,rotational_speed,torque,tool_wear,tool_wear_time):
    try:
        air_temp = float(air_temp)
        process_temp = float(process_temp)
        rotational_speed = int(rotational_speed)
        torque = float(torque)
        tool_wear = int(tool_wear)
        tool_wear_time = int(tool_wear_time)
        rotational_speed_for_pwf = (rotational_speed * 0.1042)

        temp = (air_temp - process_temp)
        pwf = (torque * rotational_speed_for_pwf)
        osf = (tool_wear * torque)

        values = []

        if tool_wear_time in range(199, 241):
            values.append(1)
        else:
            values.append(0)

        if temp < 8.6:
            if rotational_speed < 1380:
                values.append("1")
            else:
                values.append(0)
        else:
            values.append(0)

        if pwf in range(3499, 9001):
            values.append(1)
        else:
            values.append(0)

        if osf > 11000 or osf > 12000 or osf > 13000:
            values.append(1)
        else:
            values.append(0)
    except Exception as e:
        raise Exception(f"(ml_trails): Something went wrong: "+str(e))
    return list(values)



