# Aufgabe 6: Bug finden und bessere Filterparameter wählen

import librosa
import scipy.ndimage
import matplotlib.pyplot as plt

audio_filepath = "./audio.wav"


y, sr = librosa.load(audio_filepath, sr=None)


y_max_filtered = scipy.ndimage.maximum_filter1d(y, size=5000)


threshold = 0.10
segments = []
start = None
for i in range(len(y_max_filtered)):
    if threshold > y_max_filtered[i]:
        if start is None:
            start = i  # Start a new segment
    else:
        if start is not None:
            segments.append((start, i))  # End the current segment
            start = None
        # If we reach the end of the signal and are still in a segment, close it
if start is not None:
            segments.append((start, len(y_max_filtered)))


num_segments = len(segments)
fig = plt.figure(figsize=(14, 6 + 2 * num_segments))

# First row: full signal and max filtered, single axis spanning all columns
ax_main = plt.subplot2grid((2, max(1, num_segments)), (0, 0), colspan=max(1, num_segments))
ax_main.plot(y, label='Original Audio Signal', alpha=0.5)
ax_main.plot(y_max_filtered, label='Maximum Filtered Audio Signal', color='red', alpha=0.7)
ax_main.set_title('Audio Signal and Maximum Filtered Signal')
ax_main.set_xlabel('Sample Index')
ax_main.set_ylabel('Amplitude')
ax_main.legend()
ax_main.grid()

# Second row: each segment in its own subplot
axes_segments = []
for idx, (start, end) in enumerate(segments):
    ax = plt.subplot2grid((2, max(1, num_segments)), (1, idx))
    ax.plot(y[start:end])
    ax.set_title(f'Segment {idx+1}: [{start}, {end})')
    ax.set_xlabel('Sample Index')
    ax.set_ylabel('Amplitude')
    ax.grid()
    axes_segments.append(ax)

plt.tight_layout()
plt.show()

