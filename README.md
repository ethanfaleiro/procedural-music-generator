# Procedural Music Generator 🎵

A simple Python program music generator that generates melodies using a simple UI built with **Tkinter** and **music21**.

This project was built to explore basic music theory, Python logic, and GUI development. It outputs a `.mid` file that you can play with any MIDI-compatible software.

---

## 🛠️ How to Use

1. **Number of Notes**  
   Enter how many notes you want in your melody.  
   For example: `16` will generate a short melody. Try `32` or `64` for longer music.

2. **Scale** 
   Choose a musical scale to generate notes from. (C D E F G A B).

3. **BPM / Tempo**
   Enter the beats per minute.  
   This affects how fast the song plays.  
   Example: `120` is a standard tempo, `190` is much faster.

---

## 📦 Requirements

Install the required library:

```bash
pip install music21
