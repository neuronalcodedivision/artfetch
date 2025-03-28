# artfetch

## Description

`artfetch` is primarily aimed at automatically adding tags and artwork to single mp3 files, based on existing tags. It's intended to process a whole directory and optionally its subfolders.

## Install

The app can be installed via:

```bash
pip install artfetch
```

## Usage

Use it via:

```bash
artfetch /path/to/music/folder
```

After starting the program, it will go through all the files in the specified folder and present a list of matches for each tagged mp3 file, file after file.
In the list you can choose to view the source or the image of each candidate to make sure they are the correct match. The list will only show results if they have a high enough confidence (above `lower-confidence`). 
It skips the selection list and tags the file automatically if the similarity (`selection-confidence`) of one of the result is high enough (per default any result with 80% or higher similarity)

If you want to use Discogs as a tag source, you need to authenticate the app first with your Discogs account. On first startup, a browser window will open the Discogs OAuth page. After authentication, please copy the code to your clipboard or enter it manually if you use the traditional UI.
If you do not want to use Discogs, disable this source in the config file.



## Configuration

The `config.yaml` file (with an explanation of each setting) can be found at:

*   **Windows:** `%appdata%\\Roaming\\artfetch`
*   **Unix:** `~/.config/app`

## Settings

If you want a more traditional interface or your terminal does not support the default one, a scrolling interface is available with:
`-u` or `ui: standard`

*   **`confidence-score`**: A confidence score (0-1) is used to select the best match based on the ID3 tags. The `selection-confidence` sets a threshold over which the highest-ranking candidate is automatically selected. Set it to `1.0` to disable this feature.
*   **`lower-confidence`**: The `lower-confidence` does the opposite and throws out all results with a lower score than it. This results in the file being skipped if there are no suitable matches.
*   **`auto-mode`**: You can also enable auto mode, which always selects the best matching candidate with an image attached. This also uses `selection-confidence` and skips all matches below it.