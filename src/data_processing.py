def count_data_by_segment_type(data_list: []):

    dict_result = {}
    for i in data_list:
        if i.segment_type in dict_result:
            dict_result[i.segment_type] +=1
        else:
            dict_result[i.segment_type] = 1

    return dict_result

def count_data_by_answer(data_list: []):

    dict_result = {}
    for i in data_list:
        if i.answer in dict_result:
            dict_result[i.answer] += 1
        else:
            dict_result[i.answer] = 1

    return dict_result

def count_percentage(data_list, segment_type, segment_description, answer):

    filtered_data = list(filter(lambda data: data.segment_type == segment_type and
                                             data.segment_description == segment_description and
                                             data.answer == answer, data_list))
    if len(filtered_data) == 0:
        return ("Data not found")
    else:
        return filtered_data

def total_count_by_answer(data_list):

    facebook_count = sum(x.count for x in list(filter(lambda data: data.answer == "Facebook", data_list)))
    instagram_count = sum(x.count for x in list(filter(lambda data: data.answer == "Instagram", data_list)))
    linkedin_count = sum(x.count for x in list(filter(lambda data: data.answer == "Linkedin", data_list)))
    snapchat_count = sum(x.count for x in list(filter(lambda data: data.answer == "Snapchat", data_list)))

    return [facebook_count, instagram_count, linkedin_count, snapchat_count]

def total_count_by_segment_type(data_list):

    mobile_count = sum(x.count for x in list(filter(lambda data: data.segment_type == "Mobile", data_list)))
    web_count = sum(x.count for x in list(filter(lambda data: data.segment_type == "Web", data_list)))
    gender_count = sum(x.count for x in list(filter(lambda data: data.segment_type == "Gender", data_list)))
    university_count = sum(x.count for x in list(filter(lambda data: data.segment_type == "University", data_list)))
    custom_count = sum(x.count for x in list(filter(lambda data: data.segment_type == "Custom", data_list)))

    return [mobile_count, web_count, gender_count, university_count, custom_count]
