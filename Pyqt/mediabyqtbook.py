def __init__(self):
    QMainWindow.__init__(self)
    self.mediaSource = None
    self.audioPath = ''
    self.addedEffects = {}
    self.effectsDict = {}

    # Initialize some other variables.
    self._filePath = ''
    self._dirPath = ''
    self._dialog = None
    # Create media object , audio sink and path
    self.mediaObj = phonon.Phonon.MediaObject(self)
    self.audioSink = Phonon.AudioOutput(
    Phonon.MusicCategory,
    self)
    self.audioPath = Phonon.createPath(self.mediaObj,
    self.audioSink)

    # Create self._dialog instance and call
    # necessary methods to create a user interface
    self._createUI()

    # Connect slots with signals.
    self._connect()

    # Show the Audio player.
    self.show()
