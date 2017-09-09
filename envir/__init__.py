
class Enviroment(object):
    def __init__(self, state):
        self.state = state
    
    def get_current_state(self):
        return self.state    

class NonIntAction(Exception):
    def __init__(self, action_i):
        action_type=str(type(action_i))
        msg='Action must be Integer '+action_type
        super(NonIntAction, self).__init__(msg)
       