from datetime import datetime
class Call(object):
    num_calls = 0
    def __init__(self, caller_name, caller_phone, time, reason):
        self.caller_id = Call.num_calls
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time = datetime.now()
        self.reason = reason

        Call.num_calls += 1

    def display_info(self):
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)

    def add(self, a_call):
        self.calls.append(new_call)

    def remove(self, r_call):
        self.calls.remove(r_call)

    def info(self):
        for call in self.calls:
            call.display_info()
