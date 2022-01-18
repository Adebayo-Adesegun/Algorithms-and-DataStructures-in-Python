
"""

"Interviewer:
- work_start : datetime
- work_end : datetime
- booked_events: Event[]

Event:
- start: datetime
- duration: int # seconds"
"Create a interviewer.book(event) function that will try to book an event that is within working times and does not intersect with already booked events

Cover the solution with unit tests"

"""

from datetime import datetime, timedelta

class Event(object):
  def __init__(self, start, duration):
    self.start = start
    self.duration = duration #int in seconds
    


class Interviewer(object):
    def __init__(self, work_start, work_end):
        self.work_start = work_start
        self.work_end = work_end
        self.booked_events = []
    
    def add_event(self, event: Event):
          print(f'the event starts at {event.start} and lasts for {event.duration} seconds')
      
          # Make sure the event is within the working time
          if event.start >= self.work_start and event.start + timedelta(seconds=event.duration) <= self.work_end:
            
            print('valid event')
            
            print(f'len of booked event {len(self.booked_events)}')
            
            if len(self.booked_events) > 0:
              for existing_event in self.booked_events:
                
                existing_event_start = existing_event.start
                exisying_event_end = existing_event + timedelta(seconds=existing_event.duration)
                
                
                if event.start > existing_event_start and event.start < exisying_event_end:
                    return False
                else:
                    self.booked_events.append(event)
                    return True
            else:
                self.booked_events.append(event)
                print('event added to booked event')
                print(f'new length of booked event {len(self.booked_events)}')
                return True
                
          else:
              print('invalid event')
              return False
            
          
import unittest 

class TestInterviewEvent(unittest.TestCase):
  
    def setUp(self):
        # Event lasts for 10 seconds and starts 9:25:10
        #self.event = Event()
        
        self.interviewer = Interviewer(datetime(2022, 1, 17, 9, 0,0), datetime(2022, 1, 19, 9, 0,0))
        
    def test_event_within_working_hours(self):
      
        new_event = Event(datetime(2022, 1, 18, 9, 25,10), 10)
        
        self.setUp()
        
        self.assertTrue(self.interviewer.add_event(new_event))   

if __name__ == '__main__':
    unittest.main() 