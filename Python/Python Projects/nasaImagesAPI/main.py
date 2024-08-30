from io import BytesIO
import os 
import typer
from datetime import datetime
import requests
from config import apiURL, image_dir
from PIL import Image


app = typer.Typer()


default_date = typer.Argument(
    datetime.now().strftime("%Y-%m-%d"),
    formats=['%Y-%m-%d']
)

@app.command()
def fetch_image(date: datetime = default_date, save: bool =False):
    print("sending Images from NASA API.. .")
    dt = str(date.date())
    url_for_date = f"{apiURL}&date={dt}"
    res = requests.get(url_for_date)

    # fetching one image from the API
    res.raise_for_status()
    data = res.json()
    url= data['url']
    title = data['title']
    print("fetching the Image .. ")
    image_res = requests.get(url)
    image = Image.open(BytesIO(image_res.content))

    image.show()
    #  saving into a folder
    if save:
        if not image_dir.exists():
            os.mkdir(image_dir)
            image_name = f"{title}.{image.format}"
        image.save(image_dir / image_name, image.format)
    image.close()
    print("image viewed..!")






if __name__ == "__main__":
    app()
