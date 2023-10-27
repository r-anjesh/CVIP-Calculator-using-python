import tkinter as tk
import os
import pyaudio
import wave

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.audio = pyaudio.PyAudio()
        self.is_recording = False

        self.record_button = tk.Button(root, text="Record", command=self.toggle_recording)
        self.record_button.pack()

        self.save_button = tk.Button(root, text="Save", command=self.save_recording)
        self.save_button.pack()
        self.save_button.config(state=tk.DISABLED)

        self.recording_stream = None
        self.frames = []

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.record_button.config(text="Stop Recording")
            self.start_recording()
        else:
            self.is_recording = False
            self.record_button.config(text="Record")
            self.stop_recording()
            self.save_button.config(state=tk.NORMAL)

    def start_recording(self):
        self.recording_stream = self.audio.open(format=pyaudio.paInt16,
                                                channels=1,
                                                rate=44100,
                                                frames_per_buffer=1024,
                                                input=True)
        self.frames = []

    def stop_recording(self):
        if self.recording_stream:
            self.recording_stream.stop_stream()
            self.recording_stream.close()

    def save_recording(self):
        if len(self.frames) > 0:
            save_path = "recordings"
            os.makedirs(save_path, exist_ok=True)
            filename = os.path.join(save_path, "recording.wav")

            wf = wave.open(filename, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            self.frames = []

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()