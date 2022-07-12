import psutil
import ctypes
import os


class discord_audio_fixer:
    def __init__(self):
        self.admin = self.check_admin_rights()
        if self.admin:
            self.physical_count = psutil.cpu_count(logical=False)
            self.logical_count = psutil.cpu_count(logical=True)
            self.core_index = self.get_core_index()
            self.process = self.get_process()

            self.solution_001()

        else:
            print("Please run as Administrator!")

    def check_admin_rights(self):
        try:
            admin = os.getuid() == 0
        except AttributeError:
            admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        return admin

    def get_core_index(self):
        return int(self.logical_count / self.physical_count)

    def get_process(self, name="audiodg.exe"):
        for proc in psutil.process_iter():
            try:
                if proc.name() == name:
                    return proc

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

        return None

    def set_process_priority(self, process, priority):
        if priority < 0:
            priority = 0

        if priority > 5:
            priority = 5

        priority_classes = [
            psutil.IDLE_PRIORITY_CLASS,
            psutil.BELOW_NORMAL_PRIORITY_CLASS,
            psutil.NORMAL_PRIORITY_CLASS,
            psutil.ABOVE_NORMAL_PRIORITY_CLASS,
            psutil.HIGH_PRIORITY_CLASS,
            psutil.REALTIME_PRIORITY_CLASS
        ]

        process.nice(priority_classes[priority])

    def solution_001(self, priority=4):
        if self.process is not None:
            if self.process.cpu_affinity() != [self.core_index]:
                self.set_process_priority(self.process, priority)
                self.process.cpu_affinity([self.core_index])
                print(
                    f"Changed audiodg.exe to run on Core {self.core_index} with high priority!")

            else:
                print("audiodg.exe is already set up!")

        else:
            print("audiodg.exe not running!")


if __name__ == "__main__":
    try:
        discord_audio_fixer()

    except Exception as e:
        print(f"Error: {e}\nPlease report the Bug on https://github.com/M6D6M6A/DISCORD_AUDIO_FIX/issues")

    input("Press Enter to close...")
