<h1 align="center">
	Spotify Playlist Downloader
</h1>

<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/cacauisadog/spotify-playlist-downloader?color=blueviolet" />
	<img alt="Number of lines of code" src="https://img.shields.io/tokei/lines/github/cacauisadog/spotify-playlist-downloader?color=blueviolet" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/cacauisadog/spotify-playlist-downloader?color=blue" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/cacauisadog/spotify-playlist-downloader?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/cacauisadog/spotify-playlist-downloader?color=brightgreen" />
</p>

<h3 align="center">
	<a href="#%EF%B8%8F-about">About</a>
	<span> · </span>
	<a href="#%EF%B8%8F-usage">Usage</a>
	<span> · </span>
	<a href="#-testing">Testing</a>
</h3>

---


## 🗣️ About

A simple CLI python module to download songs from a Spotify URL playlist.


## 🛠️ Usage

### Requirements

- python >= 3.7
- `youtube-dl` CLI [installed on your system](https://youtube-dl.org/) and on your `$PATH`

### Instructions

1. Clone this repository;
2. `cd` into it:

```shell
cd spotify-playlist-downloader
```

3. Install requirements:
```shell
pip install -r requirements.txt
```
Note: it's recommended you use a virtual environment to isolate this module's dependencies from your system's.

4. Copy the link to the Spotify playlist of your choice. It should look something like this: `https://open.spotify.com/playlist/3uksUEPCnD79FvjbZJKcpy?si=212cc4a427cd4a6e`
5. On your terminal, run:
```shell
python -m main <playlist-url>
```

It should start downloading from the top of the playlist, song by song, into the `songs` folder.

## 📋 Testing

// TODO
