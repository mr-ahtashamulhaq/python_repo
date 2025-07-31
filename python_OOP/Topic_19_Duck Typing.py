# Create 3 classes: PDF, Word, and Excel
# Each class should have a method export()
# Write a function export_file(file) that uses duck typing
# Call export_file() with each object

class PDF:
    def export(self):
        print("Exporting PDF file...")

class Word:
    def export(self):
        print("Exporting Word document...")

class Excel:
    def export(self):
        print("Exporting Excel spreadsheet...")
def export_file(file):
    file.export()

export_file(PDF())
export_file(Word())
export_file(Excel())


# Create three classes: YouTube, Spotify, and Radio. Each should have a method play().
# Write a function start_audio(player) that uses duck typing to call play().
# Then pass objects of all three classes to start_audio().
class YouTube:
    def play(self):
        print("Playing video from YouTube")

class Spotify:
    def play(self):
        print("Playing music from Spotify")

class Radio:
    def play(self):
        print("Playing music from Radio")

def start_audio(player):
    player.play()

start_audio(YouTube())
start_audio(Spotify())
start_audio(Radio())
