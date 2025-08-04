# ✨ Simple GIF Maker

Hey there\! This script is a super easy way to turn your photos into a fun animated GIF.

-----

### 🚀 Getting Started

You'll need Python and the `imageio` library. If you don't have `imageio`, just run this command in your terminal:

```bash
pip install imageio
```

-----

### 🎨 Make Your GIF

Follow these three simple steps:

1.  Put all your picture files in the same folder as the script.

2.  Open the script and edit the **`filenames`** list to include your picture names in the order you want them to appear.

3.  Run the script from your terminal:

    ```bash
    python your_script_name.py
    ```

A new file named `monke.gif` will appear in your folder. That's it\!

-----

### ⚙️ How to Customize Your GIF

You can easily change how your GIF looks and behaves by editing these lines in the code:

  * **`filenames = [...]`**: Change this to the names of your pictures. The order you list them is the order they will play.
  * **`'monke.gif'`**: This is the name of your new GIF file. You can change it to whatever you like.
  * **`duration = 500`**: This controls the speed. A duration of `500` means each picture shows for half a second. Use a bigger number for a slower GIF, or a smaller number for a faster one.
  * **`loop = 0`**: This makes the GIF play forever. Change it to `loop = 1` for it to play only once.
