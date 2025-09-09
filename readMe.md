# Image Fetcher

Image Fetcher is a Python project designed to download images from the internet based on user-defined queries or URLs. It streamlines the process of fetching and saving images locally for further use.

## Features

- Download images from URLs or search queries
- Save images to a specified directory
- Simple and intuitive command-line interface
- Error handling for invalid URLs and network issues

## Requirements

- Python 3.7+
- `requests` library
- `Pillow` library (optional, for image processing)

Install dependencies with:

```bash
pip install requests pillow
```

## Usage

### Downloading an Image from a URL

```bash
python image_fetcher.py --url "https://example.com/image.jpg" --output "./images"
```

### Downloading Images by Search Query

```bash
python image_fetcher.py --query "cats" --limit 5 --output "./images"
```

## Arguments

| Argument      | Description                              |
|---------------|------------------------------------------|
| `--url`       | Direct image URL to download             |
| `--query`     | Search term for fetching images          |
| `--limit`     | Number of images to fetch (default: 1)   |
| `--output`    | Output directory for saved images        |


## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.
