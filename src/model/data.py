from src.model.segment_type import SegmentType
class Data():

    question = ""
    segment_type: SegmentType
    segment_description = ""
    answer = ""
    count = 0
    percentage = 0.0

    def __init__(self, question, segment_type, segment_description, answer, count, percentage):

        self.question = question
        self.segment_type = segment_type
        self.segment_description = segment_description
        self.answer = answer
        self.count = count
        self.percentage = percentage