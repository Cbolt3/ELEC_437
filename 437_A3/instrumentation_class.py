import time
from datetime import datetime

class Instrumentation:
    instance = None


    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.activation = False
            cls.instance.level = 0
            cls.instance.buffer = []
            cls.instance.timeStack = []

        return cls.instance

    def startTiming(self, comment):
        #  Start timing a method, or block of code
        if self.activation:
            self.timeStack.append(time.perf_counter())
            text = "|   " * self.level + "STARTTIMING: " + comment
            self.buffer.append(text)
            self.level += 1

    def stopTiming(self, comment):
        #  Stop timing a method, or block of code
        if self.activation:
            self.level -= 1
            currTime = time.perf_counter()
            startTime = self.timeStack.pop()
            elapsedTime = (currTime - startTime) * 1000000
            text = "|   " * self.level + "STOPTIMING: " + comment + ' ' + f"{elapsedTime:.2f}" + 'us'
            self.buffer.append(text)


    def comment(self, comment):
        #  Place an additional comment in the output of the instrumentation log file
        if self.activation:
            text = "|   " * self.level + "COMMENT: " + comment
            self.buffer.append(text)

    def dump(self, filename=None):
        # Write to file

        if self.activation:
            if filename is None:
                timestamp = datetime.now().strftime("%d%y%m%d%H%M%S")
                filename = f"instrumentation{timestamp}.log"

            with open(filename, "w") as file:
                file.write("\n".join(self.buffer))

    def activate(self, active: bool):
        #  activates/deactivates instrumentation.
        self.activation = active