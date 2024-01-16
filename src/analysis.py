def extractData(carver_data, prev_carver_data):
    extracted_data = {'working': False, 'working_realm': ''}
    last_carver_area = ''
    next_carevr_area = ''
    last_carver_time = None
    next_carevr_time = None
    current_time = carver_data['current_time']

    difference = 0
    working_status_change = False
    
    for key, value in carver_data.items():
        if key == 'current_time':
            continue  # Skip 'current_time' dictionary

        if 'away_until' in value:
            away_until = value['away_until']
        else:
            print(f"Warning: 'away_until' key not found in {key} dictionary.")
            continue

        if 'working_until' in value:
            working_until = value['working_until']
        else:
            print(f"Warning: 'working_until' key not found in {key} dictionary.")
            continue

        if away_until < current_time or current_time < working_until:
            extracted_data['working'] = True
            extracted_data['working_realm'] = key
            last_carver_area = key
            difference = value['working_until'] - current_time
        elif last_carver_time is None and last_carver_area == '':
            last_carver_area = key
            last_carver_time = value['working_until']
        elif last_carver_time < value['working_until']:
            last_carver_area = key
            last_carver_time = value['working_until']

        if not extracted_data['working']:
            if next_carevr_area == '':
                next_carevr_area = key
                next_carevr_time = value['working_until']
            elif next_carevr_time > value['working_until']:
                next_carevr_area = key
                next_carevr_time = value['working_until']

        if difference == 0:
            difference = away_until - current_time

    extracted_data['time_left'] = difference
    days = int(difference / 60 / 60 / 24) 
    difference = difference - (days * 60 * 60 * 24)
    hours = int(difference / 60 / 60)
    difference = difference - (hours * 60 * 60)
    minutes = int(difference / 60)
    difference = difference - (minutes * 60)
    seconds = int(difference)

    extracted_data['days'] = days
    extracted_data['hours'] = hours
    extracted_data['minutes'] = minutes
    extracted_data['seconds'] = seconds

    working_status_change = True
    if not (prev_carver_data is None or prev_carver_data == {}):
        working_status_change = extracted_data['working'] != prev_carver_data['working']

    extracted_data['last_carver'] = last_carver_area
    extracted_data['next_carver_area'] = next_carevr_area
    extracted_data['status_change'] = working_status_change
    
    return extracted_data


def timeMessage(data):
    message = ''

    if data['days'] > 0:
        message = message + str(data['days'])
        if data['days'] > 1:
            message = message + ' days '
        else:
            message = message + ' day '

    if data['hours'] > 0:
        message = message + str(data['hours'])
        if data['hours'] > 1:
            message = message + ' hours '
        else:
            message = message + ' hour '

    if data['minutes'] > 0:
        message = message + str(data['minutes'])
        if data['minutes'] > 1:
            message = message + ' minutes '
        else:
            message = message + ' minute '

    if data['seconds'] > 0:
        message = message + str(data['seconds'])
        if data['seconds'] > 1:
            message = message + ' seconds'
        else:
            message = message + ' second'
    return message
