# -*- coding: utf-8 -*-
import sys
import datetime
import threading
import queue
import traceback

class Message(object):
    def __init__(self, *args, **kw):
        self.args = args
        self.kw = kw


class Task(threading.Thread):
    def __init__(self, *args, **kw):
        super(Task, self).__init__(name="%s:%x"%(self.__class__.__name__,id(self)),args=args,kwargs=kw)
        self.created_time_stamp=datetime.datetime.now()
        self.message_queue = queue.Queue()
        self.running = False

        self.quit_on_no_message = False
        self.quit_on_error = False
        self.gracefully_quitted = False
        self.prologue = None
        self.eplilogue = None

    def show_timestamped_message(self, contents, new_line=True):
        sys.stdout.write("***%s:%s:%s"%(
            datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S"),
            self.name,
            contents))
            
        if new_line:
                sys.stdout.write("\n")
            
        sys.stdout.flush()



    def put_message(self, message):
        if not isinstance(message,Message):
            raise ValueError("'%s'is not instance of Message class." % message)
        else:
            self.message_queue.put(message)

    def run(self, *args,**kw):
        self.running = True
        if self.prologue and callable(self.prologue):
            self.prologue(self, *args, **kw)
            
        while self.running:
            try:
                message = self.message_queue.get(timeout=1)
            except queue.Empty as exc:
                if self.quit_on_no_message is True:
                    self.running = False
                    break
                else:
                    continue

            try:
                target_method = getattr(self, ("handle_%s" % message.__class__.__name__))
                target_method(*message.args, **message.kw)
            except Exception as exc:
                self.show_timestamped_message(traceback.format_exc())
                if self.quit_on_error is True:  
                    break
                else:
                    continue
        
        if self.epilogue and callable(self.epilogue):
            self.epilogue(self)
        
        self.gracefully_quitted = True
        return None
